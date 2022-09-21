def get_voltage_dict(voltage_value: int) -> dict:
    return {"Voltage": voltage_value}


def get_dict_for_set_gear_pos(gear_1_voltage, gear_2_voltage):
    return {"Pins": [{"PinId": 1, "Voltage": gear_1_voltage}, {"PinId": 2, "Voltage": gear_2_voltage}]}
