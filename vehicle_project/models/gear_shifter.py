from vehicle_project.resources.pins_id import PinsId
from vehicle_project.utils.data_converter_utils import get_voltage_dict, get_dict_for_set_gear_pos
from vehicle_project.utils.vehical_api_utils import execute_post_for_one_pin, execute_post_for_all_pins, \
    execute_get_for_all_pins


class GearShifter:
    """
    Class Gear Shifter with gear positions
    """

    PARK = "Park"
    NEUTRAL = "Neutral"
    REVERSE = "Reverse"
    DRIVE = "Drive"

    POSITIONS = {PARK: (0.67, 3.12), NEUTRAL: (1.48, 2.28), REVERSE: (2.28, 1.48), DRIVE: (3.12, 0.67)}

    @staticmethod
    def set_gear_shifter_by_pos(position: str):
        """
        Sets Gear position
        """
        if position == GearShifter.PARK:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.PARK]))
        elif position == GearShifter.NEUTRAL:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.PARK]))
        elif position == GearShifter.REVERSE:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.PARK]))
        elif position == GearShifter.DRIVE:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.PARK]))
        else:
            raise ValueError("This state is absent")

    @staticmethod
    def get_current_gear_pos() -> tuple:
        """
        Returns current Gear information
        """
        response = execute_get_for_all_pins()
        return response.json()[PinsId.GEAR_1 - 1], response.json()[PinsId.GEAR_2 - 1]
