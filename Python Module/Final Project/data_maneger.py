import json


def load_data():
    try:
        with open('data.json') as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        pass


def upload_data(users_data, products_data):
    data = {"user": users_data, "product": products_data}
    with open('data.json', "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("data saved.")
