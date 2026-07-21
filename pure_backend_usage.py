import requests
import json


def check_get():

    response = requests.get("http://localhost:8001/data")

    print(response.status_code)
    print(response.json())

# check_get()
def check_post():
    new_item = {
        "name": "Alice Johnson",
        "email": "alice.johnson@example.com"
    }

    response = requests.post("http://localhost:8001/data", data=json.dumps(new_item))

    print(response.status_code)
    print(response.json())


# check_post()

def check_put():
    new_item = {
        "name": "Alice Alice",
        "email": "alice.johnson@example.com"
    }

    response = requests.put("http://localhost:8001/data/1", data=json.dumps(new_item))

    print(response.status_code)
    print(response.json())


# check_put()

def check_delete():

    response = requests.delete("http://localhost:8001/data/2")

    print(response.status_code)
    # print(response.json())

# check_delete()
check_get()
