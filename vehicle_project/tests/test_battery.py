import pytest

from framework.utils.asserts import soft_assert_for_lists
from vehicle_project.models.battery import Battery
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.pin import Pin
from vehicle_project.models.signal import Signal


class TestBattery:
    VOLTAGE_BATTERY_VALUES = [800, 799.99, 800.01, 400, 399.99, 400.01, 0, 0.01]

    def test_not_ready_state(self):
        Battery.set_battery_state(Battery.NOT_READY)
        battery_state_signal = Signal.get_obj_from_json(Battery.get_current_battery_signal())
        gear_position_signal = Signal.get_obj_from_json(GearShifter.get_current_gear_pos_signal())
        assert battery_state_signal.Value == Battery.NOT_READY
        assert gear_position_signal.Value == GearShifter.NEUTRAL

    def test_error_state(self):
        Battery.set_battery_state(Battery.ERROR)
        pin_objects_list = Pin.get_obj_from_json(Pin.get_all_pins())
        expected_values_list = [0] * len(pin_objects_list)
        actual_voltage_values_list = [round(pin_object.Voltage) for pin_object in pin_objects_list]
        assert soft_assert_for_lists(expected_values_list, actual_voltage_values_list)

    @pytest.mark.parametrize("voltage", VOLTAGE_BATTERY_VALUES)
    def test_voltage_values(self, voltage):
        battery_state_by_voltage = Battery.get_battery_state_by_voltage(voltage)
        Battery.set_battery_state(battery_state_by_voltage)
        actual_battery_state = Signal.get_obj_from_json(Battery.get_current_battery_signal())
        assert battery_state_by_voltage == actual_battery_state.Value
