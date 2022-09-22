from vehicle_project.models.base_model import BaseModel
from vehicle_project.utils.vehical_api_utils import execute_get_for_one_signal, execute_get_for_all_signals


class Signal(BaseModel):

    @staticmethod
    def get_signal_json_by_id(sig_id: int) -> str:
        return execute_get_for_one_signal(sig_id).json()

    @staticmethod
    def get_all_signals() -> str:
        return execute_get_for_all_signals().json()
