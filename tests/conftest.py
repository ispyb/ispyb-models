from typing import Generator, Any
import os
import pytest

import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.schema


engine = sqlalchemy.create_engine(
    url=os.environ["SQLALCHEMY_DATABASE_URI"],
    connect_args={"use_pure": True},
    isolation_level="READ UNCOMMITTED",
)

_session = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def session() -> Generator[sqlalchemy.orm.Session, Any, None]:
    session = _session()
    try:
        yield session
        session.commit()
    except:  # noqa
        session.rollback()
        raise
    finally:
        session.close()
