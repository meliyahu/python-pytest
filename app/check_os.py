"""
fake check os
"""
from time import sleep


def is_windows():
    """Simulate complex logic checking os"""
    # slow function
    sleep(5)
    return True


def get_operating_system():
    """Return operating system"""
    return "Windows" if is_windows() else "Linux"
