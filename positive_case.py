import requests
import json

def test_positive_booking_submission():
    url = "https://automationintesting.online/booking/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-01",
            "checkout": "2024-07-10"
        },
        "additionalneeds": "Breakfast"
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    
    response_data = response.json()
    assert response_data["firstname"] == payload["firstname"], f"Expected {payload['firstname']}, but got {response_data['firstname']}"
    assert response_data["lastname"] == payload["lastname"], f"Expected {payload['lastname']}, but got {response_data['lastname']}"
    assert response_data["totalprice"] == payload["totalprice"], f"Expected {payload['totalprice']}, but got {response_data['totalprice']}"
    assert response_data["depositpaid"] == payload["depositpaid"], f"Expected {payload['depositpaid']}, but got {response_data['depositpaid']}"
    assert response_data["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"], f"Expected {payload['bookingdates']['checkin']}, but got {response_data['bookingdates']['checkin']}"
    assert response_data["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"], f"Expected {payload['bookingdates']['checkout']}, but got {response_data['bookingdates']['checkout']}"

    print("Positive test case passed!")

test_positive_booking_submission()
