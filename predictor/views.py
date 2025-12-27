from django.shortcuts import render

# Create your views here.

import pandas as pd
import joblib
from django.shortcuts import render

model = joblib.load("model/house_price_prediction.pkl")

def home(request):
    prediction = None
    display_price = None
    price_unit = None
    

    if request.method == "POST":
        bhk = int(request.POST.get("bhk"))
        sqft = int(request.POST.get("squarefeet"))
        areatype = request.POST.get("areatype")
        location = request.POST.get("location")

        user_df = pd.DataFrame([{
            "BHK": bhk,
            "Area_sqft": sqft,
            "Area_Type": areatype,
            "Location": location
        }])

        prediction = model.predict(user_df)[0]
        
        if prediction >= 100:
            display_price = round(prediction / 100, 2)
            price_unit = "Cr"
        else:
            display_price = prediction
            price_unit = "Lakhs"
        

    return render(request, "index.html", {"prediction": display_price, "price_unit": price_unit})
