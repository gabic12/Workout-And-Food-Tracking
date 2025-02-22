import requests
from  datetime import datetime

#API keys
APP_ID = "YOUR ID HERE"
APP_KEY = "YOUR KEY HERE"

SHEETY_ID = "YOUR ID HERE"
SHEETY_KEY = "YOUR KEY HERE"

#Your information
GENDER = "gender"
WEIGHT_KG = 00
HEIGHT_CM = 000
AGE = 00

#API endpoints
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/"

#Date variables
date = str(datetime.now().date())
time = datetime.now().time().strftime("%H:%M:%S")

#API Headers
nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

sheety_header = {
    "Authorization": SHEETY_ID
}

nutritionix_parameters = {
    "query": input("Which exercises did you do?: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_parameters, headers=nutritionix_header)
response.raise_for_status()
data = response.json()["exercises"]

for exercise in data:
    sheet_entry = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=f"{sheety_endpoint}/{SHEETY_KEY}/myWorkouts/workouts", json=sheet_entry, headers=sheety_header)
    response.raise_for_status()
