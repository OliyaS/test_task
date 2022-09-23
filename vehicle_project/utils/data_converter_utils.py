def get_voltage_dict(voltage_value: int) -> dict:
    """
    :param voltage_value: voltage value
    :return: dictionary for setting voltage value on the pin
    """
    return {"Voltage": voltage_value}


def get_dict_for_set_gear_pos(gear_1_voltage, gear_2_voltage):
    """
    :param gear_1_voltage: Gear_1 voltage value
    :param gear_2_voltage: Gear_2 voltage value
    :return: dictionary for setting value for Gear_1 and Gear_2
    """
    return {"Pins": [{"PinId": 1, "Voltage": gear_1_voltage}, {"PinId": 2, "Voltage": gear_2_voltage}]}
