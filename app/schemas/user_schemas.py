from pydantic import BaseModel

class UpdateNameRequest(BaseModel):
    full_name: str
