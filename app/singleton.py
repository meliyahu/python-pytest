"""
Test singleton pattern
"""
class Singleton:

    """
    A class
    """
    __instance = None
    @staticmethod
    def get_instance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

s = Singleton()
print(s)

s = Singleton.get_instance()
print (s)

s = Singleton.get_instance()
print (s)
