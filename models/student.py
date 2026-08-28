from  dataclasses import dataclass

from models.enums import Gender


@dataclass
class Student:
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    gender: Gender | None = None
    mobile: str | None = None
    date_of_birth: str | None = None
    subject : str | None = None
    hobbies : str | None = None
    picture : str | None = None
    current_address : str | None = None
    state : str | None = None
    city : str | None = None





