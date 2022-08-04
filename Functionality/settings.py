import json


def save(new_data):
    with open("Functionality/settings_components.json", 'w') as new_settings:
        json.dump(new_data, indent=4, fp=open("Functionality/settings_components.json", 'w'))


def get_data():
    with open('Functionality/settings_components.json') as settings:
        data = json.load(settings)
    return data