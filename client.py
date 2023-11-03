import requests
body = {
    "step": 1,
    "type": 2,
    "amount": 181,
    "oldbalanceOrg": 181,
    "newbalanceOrig": 0,
    "oldbalanceDest": 0,
    "newbalanceDest": 0,
    "isFlaggedFraud": 1
    }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765}