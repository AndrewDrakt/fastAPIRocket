from typing import Annotated
from fastapi import APIRouter,Depends
from repository import *
from schemas import *

router = APIRouter(
    prefix="/post",
    tags=["Должности"],
)

@router.post("")
async def add_posts(
        post: Annotated[SPostAdd,Depends()],
)->SPostId:
    post_id = await PostRepository.add_one(post)
    return {"ok": True, "post_id": post_id}

@router.get("")
async def get_posts() -> list[SPost]:
    posts = await PostRepository.find_all()
    return posts