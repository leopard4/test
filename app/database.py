from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from urllib.parse import quote_plus

# PostgreSQL 연결 정보 (username, password, dbname 수정)

# DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DB_USER', 'username')}:{quote_plus(os.getenv('DB_PASSWORD', 'password'))}@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'dbname')}"
# Windsurf Cascade 제안사항 // 제안사항.txt에 상세내용 기록

# 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# 세션 로컬 설정
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# 모델 베이스 클래스
Base = declarative_base()

# DB 세션 의존성 설정
async def get_db():
    async with SessionLocal() as session:
        yield session
