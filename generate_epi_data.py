import requests
import random
from datetime import datetime, timedelta
import uuid
import time

API_URL = "https://7rubhz63lh.execute-api.us-east-1.amazonaws.com/report"

locations = ["Atlanta", "New York", "Chicago", "Houston"]
symptoms_list = [["fever"], ["rash"], ["fever", "rash"], ["headache"]]

for i in range(300):
    payload = {
    "patient_id": str(uuid.uuid4()),
    "age": random.randint(18, 70),
    "location": random.choice(locations),
    "symptoms": random.choice(symptoms_list),
    "disease": "mpox",
    "vaccinated": random.choice([True, False]),
    "report_time": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
}

    r = requests.post(API_URL, json=payload)
    print(i, r.status_code)
    time.sleep(0.2)

print("Done sending data")
