"""Test"""
# import pytest
from app.check_os import get_operating_system


class TestCheckOs:
    """Test Check Os functions"""

    # 'mocker' is fixture provided by pytest-mock
    def test_get_operating_system_is_windows(self, mocker):
        """test"""
        # Mock the slow function and return True always
        mocker.patch('app.check_os.is_windows', return_value=True)
        assert get_operating_system() == "Windows"

    def test_get_operating_system_is_linux(self, mocker):
        """test"""
        # Mock the slow function and return True always
        mocker.patch('app.check_os.is_windows', return_value=False)
        assert get_operating_system() == "Linux"
