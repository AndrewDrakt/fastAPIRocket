from pydantic import BaseModel

class SPostAdd(BaseModel):
    name: str
    description: str | None

class SPost(SPostAdd):
    id: int

class SPostId(BaseModel):
    ok: bool=True
    post_id: int