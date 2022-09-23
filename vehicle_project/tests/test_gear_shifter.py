import pytest

from vehicle_project.models.battery import Battery
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.signal import Signal


class TestGearShifter:
    @pytest.mark.parametrize("battery_state", [Battery.ERROR, Battery.NOT_READY])
    @pytest.mark.parametrize("gear_pos", [GearShifter.PARK, GearShifter.REVERSE, GearShifter.DRIVE])
    def test_with_battery_error_and_not_ready(self, battery_state, gear_pos):
        Battery.set_battery_state(battery_state)
        battery_state_signal = Signal.get_obj_from_json(Battery.get_current_battery_signal())
        assert battery_state_signal.Value == battery_state
        GearShifter.set_gear_shifter_by_pos(gear_pos)
        gear_position_signal = Signal.get_obj_from_json(GearShifter.get_current_gear_pos_signal())
        assert gear_position_signal.Value == GearShifter.NEUTRAL
