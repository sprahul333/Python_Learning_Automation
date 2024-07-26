import allure
import pytest

import requests


@allure.title("Create Booking CRUD")
@allure.description("TC#1 --> Verify the Create Booking")
@pytest.mark.crud
def test_booking_positive_test_case():
    base_url = "https://restful-booker.herokuapp.com/"
    endpoint = "booking"

    URL = base_url + endpoint

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "firstname": "Bronny",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-03"
        },
        "additionalneeds": "Breakfast"
    }

    response=requests.post(url=URL, json=payload, headers=headers)

    print(response.text)

    print(response.status_code)

    print(response.headers)

    assert response.status_code == 200, "Failed to create booking"

    assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"

    assert response.json()["booking"]["firstname"] == "Bronny", "Wrong first name"

    assert response.json()["booking"]["lastname"] == "Brown", "Wrong last name"

    assert response.json()["booking"]["totalprice"] == 111, "Wrong total price"

    assert response.json()["bookingid"] is not None, "Booking ID is missing"

    assert  type(response.json()["bookingid"]) == int, "Booking ID is not an integer"

@allure.title("Create Booking CRUD - Empty Payload")
@allure.description("TC#2 --> Negative Testing of Create Booking by passing empty Load")
@pytest.mark.crud
def test_booking_empty_pay_load_test_case():
    base_url = "https://restful-booker.herokuapp.com/"
    endpoint = "booking"

    URL = base_url + endpoint

    headers = {
        "Content-Type": "application/json"
    }

    payload ={}

    response=requests.post(url=URL, json=payload, headers=headers)

    print(response.text)

    print(response.status_code)

    assert response.status_code == 500, "Failed to create booking"



@allure.title("Create Booking CRUD - Empty Payload")
@allure.description("TC#2 --> Negative Testing of Create Booking by passing empty Load")
@pytest.mark.crud
def test_booking_positive_test_case():
    base_url = "https://restful-booker.herokuapp.com/"
    endpoint = "booking"

    URL = base_url + endpoint

    headers = {
        "Content-Type": "application/json"
    }

    payload ={}

    response=requests.post(url=URL, json=payload, headers=headers)

    allure.step("Capturing Response Text")
    print(response.text)

    print(response.status_code)

    allure.attach("Validating the Response Code", "Response Text", attachment_type=allure.attachment_type.TEXT)

    assert response.status_code == 500, "Failed to create booking"
