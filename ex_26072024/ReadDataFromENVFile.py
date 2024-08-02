import pandas
from dotenv import find_dotenv, load_dotenv

import os


def test_data_update_req():
    load_dotenv()
    url= os.getenv("URL")
    username=os.getenv("UserName")
    print(url)
    print(username)
    print(type(url))
    print(type(username))


test_data_update_req()
