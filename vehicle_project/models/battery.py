from vehicle_project.resources.pins_id import PinsId
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict
from vehicle_project.utils.vehical_api_utils import execute_post_for_one_pin, execute_get_for_one_pin, \
    execute_get_for_one_signal


class Battery:
    """
    Class Battery with states and methods
    """
    READY = "Ready"
    NOT_READY = "NotReady"
    ERROR = "Error"

    STATES = {READY: 600, NOT_READY: 200, ERROR: 0}

    @staticmethod
    def get_battery_state_by_voltage(voltage: int) -> str:
        """
        :param voltage: battery voltage value
        :return: battery state by voltage
        """
        if 800 >= voltage > 400:
            return Battery.READY
        elif 0 < voltage <= 400:
            return Battery.NOT_READY
        else:
            return Battery.ERROR

    @staticmethod
    def set_battery_state(state: str):
        """
        Sets battery state on the pin
        :param state: battery state value
        """
        if state == Battery.READY:
            execute_post_for_one_pin(PinsId.BATTERY, get_voltage_dict(Battery.STATES[Battery.READY]))
        elif state == Battery.NOT_READY:
            execute_post_for_one_pin(PinsId.BATTERY, get_voltage_dict(Battery.STATES[Battery.NOT_READY]))
        elif state == Battery.ERROR:
            execute_post_for_one_pin(PinsId.BATTERY, get_voltage_dict(Battery.STATES[Battery.ERROR]))
        else:
            raise ValueError("This state is absent")

    @staticmethod
    def get_current_battery_state() -> str:
        """
        :return: current battery information
        """
        return execute_get_for_one_pin(PinsId.BATTERY).json()

    @staticmethod
    def get_current_battery_signal() -> str:
        """
        :return: current battery signal information
        """
        return execute_get_for_one_signal(SignalsId.BATTERY).json()
