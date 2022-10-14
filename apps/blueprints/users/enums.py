from enum import Enum, unique


@unique
class GenderEnum(Enum):
    MALE = 'male'
    FEMALE = 'female'


@unique
class StatusEnum(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
