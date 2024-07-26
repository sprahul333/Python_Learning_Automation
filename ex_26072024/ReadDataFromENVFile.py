
from dotenv import find_dotenv, load_dotenv

import os


def test_data_update_req():
    load_dotenv()
    url= os.getenv("URL")
    print(url)