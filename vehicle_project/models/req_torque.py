from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.utils.vehical_api_utils import execute_get_for_one_signal


class ReqTorque:
    """
    Class ReqTorque with states and methods
    """
    NM_0 = "0 Nm"
    NM_3000 = "3000 Nm"
    NM_5000 = "5000 Nm"
    NM_10000 = "10000 Nm"

    @staticmethod
    def get_req_torque_by_acc_pedal_pos(acc_pedal_pos: str) -> str:
        """
        :param acc_pedal_pos: acceleration pedal position value
        :return: requested torque value by percent
        """
        if acc_pedal_pos == AccelerationPedal.ERROR:
            return ReqTorque.NM_0
        elif acc_pedal_pos == AccelerationPedal.PERCENT_0:
            return ReqTorque.NM_0
        elif acc_pedal_pos == AccelerationPedal.PERCENT_30:
            return ReqTorque.NM_3000
        elif acc_pedal_pos == AccelerationPedal.PERCENT_50:
            return ReqTorque.NM_5000
        elif acc_pedal_pos == AccelerationPedal.PERCENT_100:
            return ReqTorque.NM_10000

    @staticmethod
    def get_current_req_torque_signal() -> str:
        """
        :return: current ReqTorque signal information
        """
        return execute_get_for_one_signal(SignalsId.REQ_TORQUE).json()