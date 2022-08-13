from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True


class Time:
    pass
