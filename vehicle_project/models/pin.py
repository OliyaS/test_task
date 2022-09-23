from vehicle_project.models.base_model import BaseModel
from vehicle_project.utils.vehical_api_utils import execute_get_for_all_pins, execute_get_for_one_pin


class Pin(BaseModel):

    @staticmethod
    def get_pin_json_by_id(pin_id: int) -> str:
        return execute_get_for_one_pin(pin_id).json()

    @staticmethod
    def get_all_pins() -> str:
        return execute_get_for_all_pins().json()
