from django.shortcuts import render

# Create your views here.

from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
import pandas as pd
import joblib
from django.shortcuts import render

def home(request):
    return render(request, "home.html")


house_model = joblib.load("model/house_price_prediction.pkl")

def house_predict(request):
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

        prediction = house_model.predict(user_df)[0]
        
        if prediction >= 100:
            display_price = round(prediction / 100, 2)
            price_unit = "Cr"
        else:
            display_price = prediction
            price_unit = "Lakhs"
        

    return render(request, "house_price.html", {"prediction": display_price, "price_unit": price_unit})


# Load model & scaler
student_model = joblib.load("model/student_pass_fail_predict.pkl")
scaler = joblib.load("model/scaler.pkl")


def predict_student(request):
    result = None
    
    if request.method == "POST":
        hours = float(request.POST["hours"])
        attendance = float(request.POST["attendance"])
        past_score = float(request.POST["past_score"])

        # Convert to DataFrame
        user_data = pd.DataFrame(
            [[hours, attendance, past_score]],
            columns=["Hours_of_Study", "Attendance", "Past_Exam_Score"]
        )

        # Scale input
        user_data_scaled = scaler.transform(user_data)

        # Predict
        prediction = student_model.predict(user_data_scaled)

        result = "PASS ✅" if prediction[0] == 1 else "FAIL ❌"
        

    return render(request, "pass_fail.html", {"result": result})



# def send_student_email(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         result = request.POST["result"]
#         hours = request.POST["hours"]
#         attendance = request.POST["attendance"]
#         past_score = request.POST["past_score"]

#         message = f"""
#             Student Prediction Result

#             Hours of Study:{hours}
#             Attendance: {attendance}%
#             Past Exam Score: {past_score}

#             Final Result: {result}

#             (This is an ML-based prediction)
#             """

#         send_mail(
#             subject="Student Result Prediction",
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[email],
#             fail_silently=False,
#         )

#     return redirect("predict_student")


