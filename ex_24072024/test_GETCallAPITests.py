#For making a GET API Call
import allure
import pytest
import requests


#Request from client to server
#URL ->
#Auth-> No
#Payload -> No
#Content-Type or header -> No
#Query Param-> No
#Path Param -> Yes /1


#Response
#Body - Verify-> Assert
#Status Code -> Verify
#-> Assert
#Header -> Verify-> Assert
#Cookie -> Verify-> Assert
#Content-Type -> Verify-> Assert
#Validate JSON Schema and XML Schema


# Installating Requests module in python:
# pip install requests

@allure.title("GET Request - Get Single Request By ID")
@allure.description("TC#1 --> Verify that GET Request with ID Works")
@allure.tag("Regression", "Smoke")
@allure.label("owner_type","Rahul")
@allure.testcase("TC#1", "Verify that GET Request with ID Works")
@allure.feature("GET Request")

@pytest.mark.smoke
def test_get_single_request_by_id():
    responseData=requests.get("https://restful-booker.herokuapp.com/booking/1")
    print(responseData.text)

    #Printing the Headers
    print(responseData.headers)

    #Printing the cookies
    print(responseData.cookies)

    #Print the response in JSON Format
    print(responseData.json())

    print(responseData.status_code)
    assert responseData.status_code==200, "Status Code is not 200"


@allure.title("GET Request - Get Single Request By ID -> Invalid Booking ID")
@allure.description("TC#1 --> Verify that GET Request with ID Works with invalid booking ID")
@allure.tag("Regression", "Smoke")
@allure.label("owner_type","Rahul")
@allure.testcase("TC#2", "Verify that GET Request with ID Works with invalid booking ID")
@allure.feature("GET Request")

@pytest.mark.smoke
def test_get_single_request_by_id_negative_test_case():
    responseData=requests.get("https://restful-booker.herokuapp.com/booking/invalid")
    print(responseData.text)

    print(responseData.status_code)
    assert responseData.status_code==404, "Status Code is not 404"



@allure.title("GET Request - Get Single Request By ID -> Invalid Booking ID --> Response Code Validation")
@allure.description("TC#1 --> Verify that GET Request with ID Works with invalid booking ID and validate response code")
@allure.tag("Regression", "Smoke")
@allure.label("owner_type","Rahul")
@allure.testcase("TC#3", "Verify that GET Request with ID Works with invalid booking ID and validate response code")
@allure.feature("GET Request")

@pytest.mark.smoke
def test_get_single_request_by_id_negative_test_case_second():
    responseData=requests.get("https://restful-booker.herokuapp.com/booking/invalid")
    print(responseData.text)

    print(responseData.status_code)
    assert responseData.status_code==200, "Status Code is not 200"
