from vehicle_project.models.base_model import BaseModel
from vehicle_project.utils.vehical_api_utils import execute_get_for_one_signal


class Signal(BaseModel):

    @staticmethod
    def get_signal_json_by_id(sig_id: int) -> BaseModel:
        return execute_get_for_one_signal(sig_id).json()
