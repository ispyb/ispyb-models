from sqlalchemy.orm import relationship

from ._auto_db_schema import *  # noqa F403
from ._auto_db_schema import UserGroup, Proposal, BLSession

__version__ = "1.0.2"


UserGroup.Permission = relationship(
    "Permission", secondary="UserGroup_has_Permission", back_populates="UserGroup"
)
UserGroup.Person = relationship(
    "Person", secondary="UserGroup_has_Person", back_populates="UserGroup"
)
Proposal.ProposalHasPerson = relationship(
    "ProposalHasPerson", back_populates="Proposal"
)
BLSession.SessionHasPerson = relationship(
    "SessionHasPerson", back_populates="BLSession"
)
