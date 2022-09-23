from vehicle_project.resources.pins_id import PinsId
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict
from vehicle_project.utils.vehical_api_utils import execute_post_for_one_pin, execute_get_for_one_pin, \
    execute_get_for_one_signal


class BrakePedal:
    """
    Class Brake Pedal with states and methods
    """
    ERROR = "Error"
    PRESSED = "Pressed"
    RELEASED = "Released"

    STATES = {ERROR: 0, PRESSED: 1.5, RELEASED: 2.5}

    @staticmethod
    def get_brake_pedal_state_by_voltage(voltage: int) -> str:
        """
        :param voltage: brake pedal voltage value
        :return: brake pedal state by voltage
        """
        if 1 <= voltage < 2:
            return BrakePedal.PRESSED
        elif 2 <= voltage < 3:
            return BrakePedal.RELEASED
        else:
            return BrakePedal.ERROR

    @staticmethod
    def set_brake_pedal_state(state: str):
        """
        Sets brake pedal state on the pin
        :param state: brake pedal state value
        """
        if state == BrakePedal.ERROR:
            execute_post_for_one_pin(PinsId.BRAKE_PEDAL, get_voltage_dict(BrakePedal.STATES[BrakePedal.ERROR]))
        elif state == BrakePedal.PRESSED:
            execute_post_for_one_pin(PinsId.BRAKE_PEDAL, get_voltage_dict(BrakePedal.STATES[BrakePedal.PRESSED]))
        elif state == BrakePedal.RELEASED:
            execute_post_for_one_pin(PinsId.BRAKE_PEDAL, get_voltage_dict(BrakePedal.STATES[BrakePedal.RELEASED]))
        else:
            raise ValueError("This state is absent")

    @staticmethod
    def get_current_brake_pedal_state() -> str:
        """
        :return: current brake pedal information
        """
        return execute_get_for_one_pin(PinsId.BRAKE_PEDAL).json()

    @staticmethod
    def get_current_brake_pedal_signal() -> str:
        """
        :return: current brake pedal signal information
        """
        return execute_get_for_one_signal(SignalsId.BRAKE_PEDAL).json()
