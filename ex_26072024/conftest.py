import pytest
import requests


#All the Fixtures will be defined here
#for the test cases in this folder

#Promotes Reusability

print("First File that i will be running automatically")
# @allure.title("Create Token")
# @allure.description("This test case is to create a token for performing different API Calls")
# @allure.tag("Sanity")
# @allure.severity(allure.severity_level.NORMAL)
@pytest.fixture()
def create_token():
    # token
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token

# @allure.title("Create Booking")
# @allure.description("This test case is to create a booking details")
# @allure.tag("Smoke")
# @allure.severity(allure.severity_level.NORMAL)
@pytest.fixture()
def create_booking():
    # Booking ID
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # print(type(URL))
    # print(type(headers))
    # print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id

@pytest.fixture()
def launch_chrome_browser():
    print("Launching a Chrome browser")
    return "Chrome"

@pytest.fixture()
def close_browser():
    print("Close Browser")
