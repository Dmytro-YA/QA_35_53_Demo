
from enum import Enum

class Gender(Enum):
    MALE = "gender-radio-1"
    FEMALE = "gender-radio-2"
    OTHER = "gender-radio-3"

    @property
    def locator(self) -> str:
        return self.value

class Hobbies(Enum):
    SPORTS = "hobbies-checkbox-1"
    READING = "hobbies-checkbox-2"
    MUSIC = "hobbies-checkbox-3"

    @property
    def locator(self) -> str:
        return self.value

class StateCity(Enum):
    NCR = ("NCR",("Delhi", "Gurgaon", "Noida"))
    UTTAR_PRADESH = ("Uttar Pradesh", ("Agra", "Lucknow", "Merrut"))
    HARYANA = ("Haryana", ("Karnal", "Panipat"))
    RAJASTHAN = ("Rajasthan", ("Jaipur", "Jaiselmer"))

    def __init__(self, state:str, cities:tuple[str, ...]):
        self.state = state
        self.cities = cities

