from sqlalchemy import select

from database import *
from schemas import *


class PostRepository:
    @classmethod
    async def add_one(cls,data: SPostAdd) -> int:
        async with new_session() as session:
            post_dict=data.model_dump()
            post=PostTbl(**post_dict)
            session.add(post_dict)
            await session.flush()
            await session.commit()
            return post.id

    @classmethod
    async def find_all(cls) -> list[SPost]:
        async with new_session() as session:
            query=select(PostTbl)
            result=await session.execute(query)
            post_models=result.scalars().all()
            post_schemas=[SPost.model_validate(post_model) for post_model in post_models]
            return post_schemas