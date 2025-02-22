import requests
from  datetime import datetime

#API keys
APP_ID = "6fe05d6d"
APP_KEY = "0b48a2936f6c21713e7c309ea0a2924a"

SHEETY_ID = "Basic Z2FiaTpsZGtmdXI3NGdnYXM2ZTE0NGc1MmNzMjMyNA=="
SHEETY_KEY = "1fc1f1d31063c088fd93bd895d862de0"

#API endpoints
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
sheety_endpoint = "https://api.sheety.co"

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
    "query": input("What did you do ate?: "),
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_parameters, headers=nutritionix_header)
response.raise_for_status()
data = response.json()["foods"]

for food in data:
    sheet_entry = {
        "food": {
            "date": date,
            "time": time,
            "food": food["food_name"].title(),
            "quantity": f"{food["serving_weight_grams"]} g",
            "calories": food["nf_calories"],
            "protein": food["nf_protein"],
            "sugar": food["nf_sugars"]
        }
    }

    response = requests.post(url=f"{sheety_endpoint}/{SHEETY_KEY}/myWorkouts/food", json=sheet_entry, headers=sheety_header)
    response.raise_for_status()