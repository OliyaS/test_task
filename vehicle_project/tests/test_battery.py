from vehicle_project.models.battery import Battery
from vehicle_project.models.gear_shifter import GearShifter
from vehicle_project.models.signal import Signal


class TestBattery:
    def test_not_ready_state(self):
        Battery.set_battery_state(Battery.NOT_READY)
        battery_state_signal = Signal.get_obj_from_json(Battery.get_current_battery_signal())
        gear_position_signal = Signal.get_obj_from_json(GearShifter.get_current_gear_pos_signal())
        assert battery_state_signal.Value == Battery.NOT_READY
        assert gear_position_signal.Value == GearShifter.NEUTRAL
