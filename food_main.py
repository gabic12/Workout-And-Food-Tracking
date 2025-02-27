import requests
from  datetime import datetime

#API keys
APP_ID = "YOUR ID HERE"
APP_KEY = "YOUR KEY HERE"

SHEETY_ID = "YOUR ID HERE"
SHEETY_KEY = "YOUR KEY HERE"

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
