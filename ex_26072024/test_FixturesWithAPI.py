# PUT
# URL
# Path - Bookinf ID
# Token - Auth
# Payload
import allure
import pytest
import requests  # pip install requests
#
# # @allure.title("Create Token")
# # @allure.description("This test case is to create a token for performing different API Calls")
# # @allure.tag("Sanity")
# # @allure.severity(allure.severity_level.NORMAL)
# @pytest.fixture()
# def create_token():
#     # token
#     url = "https://restful-booker.herokuapp.com/auth"
#     headers = {"Content-Type": "application/json"}
#     json_payload = {
#         "username": "admin",
#         "password": "password123"
#     }
#     response = requests.post(url=url, headers=headers, json=json_payload)
#     token = response.json()["token"]
#     print(token)
#     return token
#
# # @allure.title("Create Booking")
# # @allure.description("This test case is to create a booking details")
# # @allure.tag("Smoke")
# # @allure.severity(allure.severity_level.NORMAL)
# @pytest.fixture()
# def create_booking():
#     # Booking ID
#     print("Create Booking Testcase")
#     URL = "https://restful-booker.herokuapp.com/booking"
#     headers = {"Content-Type": "application/json"}
#     json_payload = {
#         "firstname": "Amit",
#         "lastname": "Brown",
#         "totalprice": 111,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2018-01-01",
#             "checkout": "2019-01-01"
#         },
#         "additionalneeds": "Breakfast"
#     }
#     response = requests.post(url=URL, headers=headers, json=json_payload)
#
#     print(type(URL))
#     print(type(headers))
#     print(type(json_payload))
#
#     # Assertions
#     assert response.status_code == 200
#     # get the reponse Body and Verify the JSON, Booking ID is not None
#     data = response.json()
#     booking_id = data["bookingid"]
#     return booking_id


@allure.title("Perform Put Request")
@allure.description("Modifying the Booking Details once the booking ID is generated")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.NORMAL)
def test_put_request_postive(create_booking,create_token):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking)
    PUT_URL = base_url+base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Pramod"



@allure.title("Perform Delete Request")
@allure.description("Deleting the Booking Details once the booking ID is generated")
@allure.tag("Smoke")
@allure.severity(allure.severity_level.NORMAL)
def test_delete(create_booking,create_token):
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)