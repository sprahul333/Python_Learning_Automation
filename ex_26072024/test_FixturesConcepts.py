# Fixtures ---> Concept of Python
# Provides context to the test case ---> similar to pre and post conditions in TESTNG
#Pre and Post conditions for a test case
import pytest


# Alternatively we can use setup and teardown ---> Before and after the test suite executions

@pytest.fixture()
def is_Married():
    return True


# Here we have injected the is_Married method into this function
def test_need_confirmation(is_Married):
    # if is_Married:
    #     print("I will get married")
    # else:
    #     print("I will not get married")
    assert is_Married == True


@pytest.fixture()
def sample_data():
    return [1, 2, 3, 4, 5]


@pytest.fixture()
def sample_data2():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_sample_data(sample_data, sample_data2):
    assert sample_data == [1, 2, 3, 4, 5]
    assert sample_data2 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
