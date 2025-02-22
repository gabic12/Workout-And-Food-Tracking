 This application was developed using Pyton v3.13 and it has has 2 functionalities:
 - it  prompts you to enter the exercises you performed,
 - it will ask for what food you ate and, with the inputs, it will call Nutritionix APIs to process the data and save the result in a Google Sheet.

This app calls 2 APIs:
- Nutritionix Nutrition & Exercise API (https://www.nutritionix.com/business/api)
- Sheety API (https://sheety.co/)

Before starting the app,you need to:
 - set up a Google Sheet, like the one from the print screens
 - connect to Sheety with your Google account

Both APIs require an authorization key - please refer to the links above for details.
The Nutritionix API employs Natural Language Processing (NLP) to interpret user input. It supports entries such as: 'walked for 40 minutes and ran 3 km', 'weight lifting for 60 mintues and light cardio for 30 minutes', '1 beef burger and 1 serving of French potatoes', '20g oates, 10g hemp seeds, 10g flax seeds, 2 teaspoons of honey'.
