import pytest
from app.core.database import Base, get_db
from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Cria um banco de dados em memória APENAS para testes
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """Cria uma nova sessão de banco para cada teste."""
    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Limpa todas as tabelas após o teste
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    """Cria um cliente de teste com banco de dados limpo."""

    def override_get_db():
        try:
            yield db
        finally:
            pass

    # Sobrescreve a dependência get_db para usar a sessão de teste
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    # Remove a sobrescrita após o teste
    app.dependency_overrides.clear()
