import requests
from datetime import datetime
import os


GENDER = 'male'
WEIGHT_KG = 90
HEIGHT_CM = 178
AGE = 49
SHEETY_ENDPOINT = 'https://api.sheety.co/83f756b5b637bb7aaefd61fc0a250dde/myWorkouts/workouts'
exercise_end_point = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_USERNAME = 'aad3rinto'
SHEETY_PASSWORD = 'NDA4585'
exercise_text = input('Tell me what exercise you performed today: ')
headers = {
    'x-app-id': 'acee296d',
    'x-app-key': 'd45c505b3a2b9a3fd0bbb5a017e26abf',
}

parameters = {
    'query': exercise_text,
    'gender':GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=exercise_end_point, json=parameters, headers=headers)
result = response.json()

# ################ START OF OUTPUT TO GOOGLESHEET
today_date = datetime.now().strftime('%d/%m/%Y')
time_now = datetime.now().strftime('%X')

for exercise in result['exercises']:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': time_now,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']

        }

    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_inputs,
        auth=(
            SHEETY_USERNAME,
            SHEETY_PASSWORD
        )
    )

    print(sheet_response.text)
