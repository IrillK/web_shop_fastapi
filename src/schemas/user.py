from pydantic import BaseModel


class UserSchemaName(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True
