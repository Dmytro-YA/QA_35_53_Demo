
from enum import Enum

class Gender(Enum):
    MALE = "gender-radio-1"
    FEMALE = "gender-radio-2"
    OTHER = "gender-radio-3"

    @property
    def locator(self) -> str:
        return self.value