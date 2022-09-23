from vehicle_project.resources.pins_id import PinsId
from vehicle_project.resources.signals_id import SignalsId
from vehicle_project.utils.data_converter_utils import get_dict_for_set_gear_pos
from vehicle_project.utils.vehical_api_utils import execute_post_for_all_pins, \
    execute_get_for_all_pins, execute_get_for_one_signal


class GearShifter:
    """
    Class Gear Shifter with gear positions and methods
    """

    PARK = "Park"
    NEUTRAL = "Neutral"
    REVERSE = "Reverse"
    DRIVE = "Drive"

    POSITIONS = {PARK: (0.67, 3.12), NEUTRAL: (1.48, 2.28), REVERSE: (2.28, 1.48), DRIVE: (3.12, 0.67)}

    @staticmethod
    def set_gear_shifter_by_pos(position: str):
        """
        Sets gear position
        :param position: gear position value
        """
        if position == GearShifter.PARK:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.PARK]))
        elif position == GearShifter.NEUTRAL:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.NEUTRAL]))
        elif position == GearShifter.REVERSE:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.REVERSE]))
        elif position == GearShifter.DRIVE:
            execute_post_for_all_pins(get_dict_for_set_gear_pos(*GearShifter.POSITIONS[GearShifter.DRIVE]))
        else:
            raise ValueError("This state is absent")

    @staticmethod
    def get_current_gear_pos() -> tuple:
        """
        :return: current gear information
        """
        response = execute_get_for_all_pins()
        return response.json()[PinsId.GEAR_1 - 1], response.json()[PinsId.GEAR_2 - 1]

    @staticmethod
    def get_current_gear_pos_signal() -> str:
        """
        :return: current gear position signal information
        """
        return execute_get_for_one_signal(SignalsId.GEAR_POSITION).json()
