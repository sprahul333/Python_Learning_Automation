import allure
import pytest

print("First Test Case Executed")

@allure.title("Verify #TC1 ---> Verify the addition of two numbers")
@allure.description("This test case verifies the addition of two numbers which is sanity test case")
@pytest.mark.sanity
def test_addition():
        print("\n Hello World");
        assert 1+1 == 2;  "1+1 should equal 2 but didn't"

print("Second Test Case Executed")

@pytest.mark.smoke
def test_subtraction():
        assert 1-1 == 0;  "1-1 should equal 0 but didn't"


print("Third Test Case Executed")

@pytest.mark.smoke
def test_multiplication():
        assert 1*1 == 1;  "1*1 should equal 1 but didn't"


print("Fourth Test Case Executed")

@pytest.mark.skip(reason="Not working, skip it")
def test_division():
        assert 1/1 == 1;  "1/1 should equal 1 but didn't"




