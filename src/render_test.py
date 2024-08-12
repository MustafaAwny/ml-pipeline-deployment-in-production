import requests


df = {
    "age": 31,
    "workclass": "Private",
    "education": "Masters",
    "maritalStatus": "Never-married",
    "occupation": "Prof-speciality",
    "relationship": "Not-in-family",
    "race": "White",
    "sex": "Male",
    "hoursPerWeek": 40,
    "nativeCountry": "United-States"
    }
r = requests.post('https://ml-pipeline-deployment-in-production.onrender.com', json=df)

assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())
