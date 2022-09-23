import pytest

from vehicle_project.resources.system_state_settings import SystemState
from vehicle_project.utils.vehical_api_utils import execute_post_for_all_pins


@pytest.fixture(autouse=True)
def set_default_state_of_system():
    """
    Pytest fixture for installing default system settings
    """
    execute_post_for_all_pins(SystemState.DEFAULT)
