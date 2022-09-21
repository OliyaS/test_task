from vehicle_project.resources.pins_id import PinsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict
from vehicle_project.utils.vehical_api_utils import execute_post_for_one_pin


class AccelerationPedal:
    """
    Class Acceleration Pedal with states and methods
    """
    ERROR = "Error"
    PERCENT_0 = "0 %"
    PERCENT_30 = "30 %"
    PERCENT_50 = "50 %"
    PERCENT_100 = "100 %"

    NM_0 = "0 Nm"
    NM_3000 = "3000 Nm"
    NM_5000 = "5000 Nm"
    NM_10000 = "10000 Nm"

    POSITIONS = {ERROR: 0, PERCENT_0: 1.5, PERCENT_30: 2.25, PERCENT_50: 2.75, PERCENT_100: 3.25}

    @staticmethod
    def get_acc_pedal_pos_by_voltage(voltage) -> str:
        """
        Returns Acceleration Pedal state by voltage
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
    def get_req_torque_by_acc_pedal_pos(acc_pedal_pos: str) -> str:
        """
        Returns Requested Torque value by percent
        """
        if acc_pedal_pos == AccelerationPedal.ERROR:
            return AccelerationPedal.NM_0
        elif acc_pedal_pos == AccelerationPedal.PERCENT_0:
            return AccelerationPedal.NM_0
        elif acc_pedal_pos == AccelerationPedal.PERCENT_30:
            return AccelerationPedal.NM_3000
        elif acc_pedal_pos == AccelerationPedal.PERCENT_50:
            return AccelerationPedal.NM_5000
        elif acc_pedal_pos == AccelerationPedal.PERCENT_100:
            return AccelerationPedal.NM_10000

    @staticmethod
    def set_acc_pedal_pos(position: str):
        """
        Sets Acceleration Pedal position
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
