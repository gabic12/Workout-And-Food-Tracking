import requests
from  datetime import datetime

#API keys
APP_ID = "6fe05d6d"
APP_KEY = "0b48a2936f6c21713e7c309ea0a2924a"

SHEETY_ID = "Basic Z2FiaTpsZGtmdXI3NGdnYXM2ZTE0NGc1MmNzMjMyNA=="
SHEETY_KEY = "1fc1f1d31063c088fd93bd895d862de0"

#Your information
GENDER = "male"
WEIGHT_KG = 62
HEIGHT_CM = 173
AGE = 31

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