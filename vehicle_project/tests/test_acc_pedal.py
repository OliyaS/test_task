import pytest

from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.models.brake_pedal import BrakePedal
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.req_torque import ReqTorque
from vehicle_project.models.signal import Signal
from vehicle_project.resources.signals_id import SignalsId


class TestAccPedal:
    """
    Class contains tests for AccPedal and ReqTorque
    """
    VOLTAGE_ACC_PEDAL_VALUES = [3.5, 3.49, 3.51, 3, 2.99, 3.01, 2.5, 2.49, 2.51, 2, 1.99, 2.01, 1, 0.99, 0]

    @pytest.mark.parametrize("voltage", VOLTAGE_ACC_PEDAL_VALUES)
    @pytest.mark.skip
    def test_voltage_values(self, voltage):
        acc_pedal_by_voltage = AccelerationPedal.get_acc_pedal_pos_by_voltage(voltage)
        AccelerationPedal.set_acc_pedal_pos(acc_pedal_by_voltage)
        acc_pedal_pos_signal = Signal.get_obj_from_json(AccelerationPedal.get_current_acc_pedal_signal())
        assert acc_pedal_by_voltage == acc_pedal_pos_signal.Value

    @pytest.mark.parametrize("gear_pos", [GearShifter.DRIVE, GearShifter.REVERSE])
    @pytest.mark.parametrize("acc_pedal_pos", AccelerationPedal.POSITIONS)
    @pytest.mark.skip
    def test_req_torque_by_acc_pedal_pos(self, gear_pos, acc_pedal_pos):
        BrakePedal.set_brake_pedal_state(BrakePedal.PRESSED)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        BrakePedal.set_brake_pedal_state(BrakePedal.RELEASED)
        AccelerationPedal.set_acc_pedal_pos(acc_pedal_pos)
        current_req_torque_signal = Signal.get_obj_from_json(Signal.get_signal_json_by_id(SignalsId.REQ_TORQUE))
        req_torque_value_by_acc_pedal = ReqTorque.get_req_torque_by_acc_pedal_pos(acc_pedal_pos)
        assert current_req_torque_signal.Value == req_torque_value_by_acc_pedal
