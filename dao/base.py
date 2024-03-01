from sqlalchemy import select, insert
from database import async_session_maker


class BaseDao:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def insert_row(cls, **data):
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**data)
            await session.execute(stmt)
            await session.commit()