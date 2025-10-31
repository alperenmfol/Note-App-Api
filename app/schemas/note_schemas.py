from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteCreateRequest(BaseModel):
    title: str
    content: Optional[str] = None
    pinned: bool = False
    favorite: bool = False
    created_at: datetime
    updated_at: datetime
