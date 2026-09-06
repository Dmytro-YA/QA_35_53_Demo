from dataclasses import dataclass, field

from models.enums import Gender, Hobbies


@dataclass
class Student:
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    gender: Gender | None = None
    mobile: str | None = None
    date_of_birth: str | None = None
    subject : str | None = None
    hobbies : list[Hobbies] = field(default_factory=list)
    picture : str | None = None
    current_address : str | None = None
    state : str | None = None
    city : str | None = None





