from sqlalchemy.future import select
from .models import User

# 이메일로 유저 조회
async def get_user_by_email(db, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

# 새 유저 생성
async def create_user(db, user_data):
    db_user = User(**user_data)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
