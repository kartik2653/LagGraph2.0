import requests
from dotenv import load_dotenv
load_dotenv()
import os
QASE_API_KEY = os.getenv('QASE_API_KEY')

url = "https://api.qase.io/v1/case/GA/bulk"
def add_bulk_to_qase(test_cases):
    print('TEST CASES',test_cases)
    test_case_payload = []
    for test_case in test_cases:
        obj = {
            "description": test_case.description,
            "preconditions": test_case.preconditions,
            "postconditions": test_case.postconditions,
            "title": test_case.test_title,
            "severity": test_case.severity,
            "priority": test_case.priority
        }
        test_case_payload.append(obj)

    payload = {'cases':test_case_payload}
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": f"{QASE_API_KEY}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)

    except Exception as e :
        print(e)




