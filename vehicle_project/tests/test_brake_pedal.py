import pytest

from framework.utils.asserts import soft_assert_for_lists
from vehicle_project.models.acceleration_pedal import AccelerationPedal
from vehicle_project.models.battery import Battery
from vehicle_project.models.brake_pedal import BrakePedal
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.req_torque import ReqTorque
from vehicle_project.models.signal import Signal


class TestBrakePedal:
    VOLTAGE_BRAKE_PEDAL_VALUES = [3, 2.99, 3.01, 2, 1.99, 2.01, 1, 0.99, 1.01, 0]

    @pytest.mark.parametrize("gear_pos", GearShifter.POSITIONS.keys())
    def test_gear_with_error_state(self, gear_pos):
        BrakePedal.set_brake_pedal_state(BrakePedal.ERROR)
        gear_position_signal = Signal.get_obj_from_json(GearShifter.get_current_gear_pos_signal())
        req_torque_signal = Signal.get_obj_from_json(ReqTorque.get_current_req_torque_signal())
        assert gear_position_signal.Value == GearShifter.NEUTRAL
        assert req_torque_signal.Value == ReqTorque.NM_0

        GearShifter.set_gear_shifter_by_pos(gear_pos)
        gear_signal_after_switch = Signal.get_obj_from_json(GearShifter.get_current_gear_pos_signal())
        assert gear_signal_after_switch.Value == GearShifter.NEUTRAL

    @pytest.mark.parametrize("brake_pedal_state", [BrakePedal.ERROR, BrakePedal.PRESSED])
    @pytest.mark.parametrize("gear_pos", [GearShifter.DRIVE, GearShifter.REVERSE])
    @pytest.mark.parametrize("acc_pedal_pos",
                             [AccelerationPedal.PERCENT_0, AccelerationPedal.PERCENT_30, AccelerationPedal.PERCENT_50,
                              AccelerationPedal.PERCENT_100])
    def test_req_torque_with_error_and_pressed(self, gear_pos, acc_pedal_pos, brake_pedal_state):
        BrakePedal.set_brake_pedal_state(BrakePedal.PRESSED)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        BrakePedal.set_brake_pedal_state(BrakePedal.RELEASED)
        AccelerationPedal.set_acc_pedal_pos(acc_pedal_pos)
        all_signal_objects_list = Signal.get_obj_from_json(Signal.get_all_signals())
        expected_signal_values = [gear_pos, acc_pedal_pos, BrakePedal.RELEASED,
                                  ReqTorque.get_req_torque_by_acc_pedal_pos(acc_pedal_pos), Battery.READY]
        actual_signal_values = [signal_object.Value for signal_object in all_signal_objects_list]
        BrakePedal.set_brake_pedal_state(brake_pedal_state)
        req_torque_signal = Signal.get_obj_from_json(ReqTorque.get_current_req_torque_signal())
        assert req_torque_signal.Value == ReqTorque.NM_0
        assert soft_assert_for_lists(expected_signal_values, actual_signal_values)

    @pytest.mark.parametrize("gear_pos", [GearShifter.PARK, GearShifter.REVERSE, GearShifter.DRIVE])
    def test_gear_with_released_state(self, gear_pos):
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        gear_position_signal = Signal.get_obj_from_json(GearShifter.get_current_gear_pos_signal())
        assert gear_position_signal.Value == GearShifter.NEUTRAL

    @pytest.mark.parametrize("gear_pos", GearShifter.POSITIONS.keys())
    def test_gear_with_pressed_state(self, gear_pos):
        BrakePedal.set_brake_pedal_state(BrakePedal.PRESSED)
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        gear_position_signal = Signal.get_obj_from_json(GearShifter.get_current_gear_pos_signal())
        assert gear_position_signal.Value == gear_pos

    @pytest.mark.parametrize("voltage", VOLTAGE_BRAKE_PEDAL_VALUES)
    def test_voltage_values(self, voltage):
        brake_pedal_state_by_voltage = BrakePedal.get_brake_pedal_state_by_voltage(voltage)
        BrakePedal.set_brake_pedal_state(brake_pedal_state_by_voltage)
        actual_brake_pedal_state = Signal.get_obj_from_json(BrakePedal.get_current_brake_pedal_signal())
        assert brake_pedal_state_by_voltage == actual_brake_pedal_state.Value
