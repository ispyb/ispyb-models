from sqlalchemy.orm import relationship

from ._auto_db_schema import *  # noqa F403
from ._auto_db_schema import UserGroup

__version__ = "1.0.0"


UserGroup.Permission = relationship(
    "Permission", secondary="UserGroup_has_Permission", back_populates="UserGroup"
)
