from vehicle_project.resources.pins_id import PinsId
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict
from vehicle_project.utils.vehical_api_utils import execute_post_for_one_pin, execute_get_for_one_signal


class AccelerationPedal:
    """
    Class Acceleration Pedal with positions and methods
    """
    ERROR = "Error"
    PERCENT_0 = "0 %"
    PERCENT_30 = "30 %"
    PERCENT_50 = "50 %"
    PERCENT_100 = "100 %"

    POSITIONS = {ERROR: 0, PERCENT_0: 1.5, PERCENT_30: 2.25, PERCENT_50: 2.75, PERCENT_100: 3.25}

    @staticmethod
    def get_acc_pedal_pos_by_voltage(voltage: int) -> str:
        """
        :param voltage: acceleration pedal voltage value
        :return: acceleration pedal state by voltage
        """
        if 1 <= voltage < 2:
            return AccelerationPedal.PERCENT_0
        elif 2 <= voltage < 2.5:
            return AccelerationPedal.PERCENT_30
        elif 2.5 <= voltage < 3:
            return AccelerationPedal.PERCENT_50
        elif 3 <= voltage < 3.5:
            return AccelerationPedal.PERCENT_100
        else:
            return AccelerationPedal.ERROR

    @staticmethod
    def set_acc_pedal_pos(position: str):
        """
        Sets Acceleration Pedal position
        :param position: acceleration pedal position value
        """
        if position == AccelerationPedal.ERROR:
            execute_post_for_one_pin(PinsId.ACC_PEDAL,
                                     get_voltage_dict(AccelerationPedal.POSITIONS[AccelerationPedal.ERROR]))
        elif position == AccelerationPedal.PERCENT_0:
            execute_post_for_one_pin(PinsId.ACC_PEDAL,
                                     get_voltage_dict(AccelerationPedal.POSITIONS[AccelerationPedal.PERCENT_0]))
        elif position == AccelerationPedal.PERCENT_30:
            execute_post_for_one_pin(PinsId.ACC_PEDAL,
                                     get_voltage_dict(AccelerationPedal.POSITIONS[AccelerationPedal.PERCENT_30]))
        elif position == AccelerationPedal.PERCENT_50:
            execute_post_for_one_pin(PinsId.ACC_PEDAL,
                                     get_voltage_dict(AccelerationPedal.POSITIONS[AccelerationPedal.PERCENT_50]))
        elif position == AccelerationPedal.PERCENT_100:
            execute_post_for_one_pin(PinsId.ACC_PEDAL,
                                     get_voltage_dict(AccelerationPedal.POSITIONS[AccelerationPedal.PERCENT_100]))
        else:
            raise ValueError("This position is absent")

    @staticmethod
    def get_current_acc_pedal_signal() -> str:
        """
        :return: current acceleration pedal signal information
        """
        return execute_get_for_one_signal(SignalsId.ACC_PEDAL).json()
