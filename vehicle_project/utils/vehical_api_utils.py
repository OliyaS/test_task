import requests

from vehicle_project.resources.config_data import ConfigData

GET_ONE_PIN = "/api/pins/{pin_id}"
GET_ALL_PINS = "/api/pins"
POST_ONE_PIN = "/api/pins/{pin_id}/update_pin"
POST_ALL_PINS = "/api/pins/update_pins"
GET_ONE_SIGNAL = "/api/signals/{sig_id} "
GET_ALL_SIGNALS = "/api/signals"


def execute_get_for_one_pin(pin_number: int):
    return requests.get(ConfigData.URL + GET_ONE_PIN.format(pin_id=pin_number))


def execute_get_for_all_pins():
    return requests.get(ConfigData.URL + GET_ALL_PINS)


def execute_get_for_one_signal(signal_number: int):
    return requests.get(ConfigData.URL + GET_ONE_SIGNAL.format(sig_id=signal_number))


def execute_get_for_all_signals():
    return requests.get(ConfigData.URL + GET_ALL_SIGNALS)


def execute_post_for_one_pin(pin_number: int, data_dict: dict):
    return requests.post(ConfigData.URL + POST_ONE_PIN.format(pin_id=pin_number), data=data_dict)


def execute_post_for_all_pins(data_dict: dict):
    return requests.post(ConfigData.URL + POST_ALL_PINS, json=data_dict)
