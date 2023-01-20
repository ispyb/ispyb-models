from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property

from ._auto_db_schema import *  # noqa F403
from ._auto_db_schema import (
    AutoProcProgram,
    AutoProcIntegration,
    AutoProcScaling,
    DataCollection,
    DataCollectionGroup,
    GridInfo,
    # ProcessingJob,
    Screening,
    ScreeningStrategy,
    ScreeningOutput,
    ScreeningStrategyWedge,
    UserGroup,
    BLSubSample,
    BLSession,
    Protein,
    Proposal,
    Workflow,
    SSXDataCollection,
    CrystalComposition,
    Crystal,
    SampleComposition,
    BLSample,
    Event,
    EventChain,
)

__version__ = "1.1.0"

DataCollection.GridInfo = relationship(
    "GridInfo", secondary="DataCollectionGroup", back_populates="DataCollection"
)
DataCollectionGroup.Workflow = relationship(
    "Workflow", back_populates="DataCollectionGroup"
)
Workflow.DataCollectionGroup = relationship(
    "DataCollectionGroup", back_populates="Workflow"
)

GridInfo.DataCollection = relationship(
    "DataCollection", secondary="DataCollectionGroup", back_populates="GridInfo"
)
AutoProcProgram.AutoProcIntegration = relationship(
    "AutoProcIntegration", back_populates="AutoProcProgram"
)
AutoProcIntegration.AutoProcScalingHasInt = relationship(
    "AutoProcScalingHasInt", back_populates="AutoProcIntegration"
)
AutoProcScaling.AutoProcScalingStatistics = relationship(
    "AutoProcScalingStatistics", back_populates="AutoProcScaling"
)
AutoProcProgram.AutoProcProgramAttachments = relationship(
    "AutoProcProgramAttachment", back_populates="AutoProcProgram"
)
AutoProcScaling.AutoProcScalingStatistics = relationship(
    "AutoProcScalingStatistics", back_populates="AutoProcScaling"
)
# ProcessingJob.ProcessingJobParameters = relationship(
#     "ProcessingJobParameter", back_populates="ProcessingJob"
# )
# ProcessingJob.ProcessingJobImageSweeps = relationship(
#     "ProcessingJobImageSweep", back_populates="ProcessingJob"
# )

Screening.ScreeningOutput = relationship("ScreeningOutput", back_populates="Screening")
ScreeningOutput.ScreeningStrategy = relationship(
    "ScreeningStrategy", back_populates="ScreeningOutput"
)
ScreeningOutput.ScreeningOutputLattice = relationship(
    "ScreeningOutputLattice", back_populates="ScreeningOutput"
)
ScreeningStrategy.ScreeningStrategyWedge = relationship(
    "ScreeningStrategyWedge", back_populates="ScreeningStrategy"
)
ScreeningStrategyWedge.ScreeningStrategySubWedge = relationship(
    "ScreeningStrategySubWedge", back_populates="ScreeningStrategyWedge"
)

UserGroup.Permission = relationship(
    "Permission", secondary="UserGroup_has_Permission", back_populates="UserGroup"
)
UserGroup.Person = relationship(
    "Person", secondary="UserGroup_has_Person", back_populates="UserGroup"
)

Protein.ConcentrationType = relationship(
    "ConcentrationType",
    foreign_keys=[Protein.concentrationTypeId],
    primaryjoin="Protein.concentrationTypeId == ConcentrationType.concentrationTypeId",
)

BLSubSample.Position1 = relationship("Position", foreign_keys=[BLSubSample.positionId])

BLSubSample.Position2 = relationship("Position", foreign_keys=[BLSubSample.position2Id])


class ModifiedProposal(Proposal):
    BLSession = relationship("BLSession", back_populates="Proposal")
    ProposalHasPerson = relationship("ProposalHasPerson", back_populates="Proposal")

    @hybrid_property
    def proposal(self):
        return self.proposalCode + self.proposalNumber


Proposal = ModifiedProposal


class ModifiedBLSession(BLSession):
    SessionHasPerson = relationship("SessionHasPerson", back_populates="BLSession")

    SessionType = relationship("SessionType", back_populates="BLSession")

    @hybrid_property
    def session(self):
        if self.Proposal:
            return (
                self.Proposal.proposalCode
                + self.Proposal.proposalNumber
                + "-"
                + str(self.visit_number)
            )
        else:
            return None

    @session.expression
    def session(cls):
        return func.concat(
            Proposal.proposalCode, Proposal.proposalNumber, "-", cls.visit_number
        )

    @hybrid_property
    def proposal(self):
        if self.Proposal:
            return self.Proposal.proposalCode + self.Proposal.proposalNumber
        else:
            return None

    @proposal.expression
    def proposal(cls):
        return func.concat(Proposal.proposalCode, Proposal.proposalNumber)


BLSession = ModifiedBLSession

SSXDataCollection.DataCollection = relationship(
    "DataCollection", back_populates="SSXDataCollection"
)
DataCollection.SSXDataCollection = relationship(
    "SSXDataCollection", back_populates="DataCollection", uselist=False
)

CrystalComposition.Crystal = relationship(
    "Crystal",
    back_populates="crystal_compositions",
)

Crystal.crystal_compositions = relationship(
    "CrystalComposition",
    back_populates="Crystal",
    cascade="all, delete-orphan",
)

SampleComposition.BLSample = relationship(
    "BLSample",
    back_populates="sample_compositions",
)

BLSample.sample_compositions = relationship(
    "SampleComposition",
    back_populates="BLSample",
    cascade="all, delete-orphan",
)

Event.EventChain = relationship(
    "EventChain",
    back_populates="events",
)

EventChain.events = relationship(
    "Event",
    back_populates="EventChain",
    cascade="all, delete-orphan",
)
