# coding: utf-8
from sqlalchemy import (
    BINARY,
    Column,
    Date,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Index,
    LargeBinary,
    String,
    TIMESTAMP,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.mysql import (
    BIGINT,
    INTEGER,
    LONGBLOB,
    MEDIUMINT,
    MEDIUMTEXT,
    SMALLINT,
    TINYINT,
    TINYTEXT,
    VARCHAR,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .base import CustomBase


Base = declarative_base(cls=CustomBase)
metadata = Base.metadata


class Additive(Base):
    __tablename__ = "Additive"

    additiveId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    additiveType = Column(String(45))
    comments = Column(String(512))
    chemFormulaHead = Column(String(25), server_default=text("''"))
    chemFormulaTail = Column(String(25), server_default=text("''"))


class AdminActivity(Base):
    __tablename__ = "AdminActivity"

    adminActivityId = Column(INTEGER(11), primary_key=True)
    username = Column(
        String(45), nullable=False, unique=True, server_default=text("''")
    )
    action = Column(String(45), index=True)
    comments = Column(String(100))
    dateTime = Column(DateTime)


class AdminVar(Base):
    __tablename__ = "AdminVar"
    __table_args__ = {"comment": "ISPyB administration values"}

    varId = Column(INTEGER(11), primary_key=True)
    name = Column(String(32), index=True)
    value = Column(String(1024), index=True)


class Aperture(Base):
    __tablename__ = "Aperture"

    apertureId = Column(INTEGER(10), primary_key=True)
    sizeX = Column(Float)


class AutoProc(Base):
    __tablename__ = "AutoProc"

    autoProcId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcProgramId = Column(INTEGER(10), index=True, comment="Related program item")
    spaceGroup = Column(String(45), comment="Space group")
    refinedCell_a = Column(Float, comment="Refined cell")
    refinedCell_b = Column(Float, comment="Refined cell")
    refinedCell_c = Column(Float, comment="Refined cell")
    refinedCell_alpha = Column(Float, comment="Refined cell")
    refinedCell_beta = Column(Float, comment="Refined cell")
    refinedCell_gamma = Column(Float, comment="Refined cell")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")


class BFAutomationError(Base):
    __tablename__ = "BF_automationError"

    automationErrorId = Column(INTEGER(10), primary_key=True)
    errorType = Column(String(40), nullable=False)
    solution = Column(Text)


class BFSystem(Base):
    __tablename__ = "BF_system"

    systemId = Column(INTEGER(10), primary_key=True)
    name = Column(String(100))
    description = Column(String(200))


class BLSampleGroup(Base):
    __tablename__ = "BLSampleGroup"

    blSampleGroupId = Column(INTEGER(10), primary_key=True)
    name = Column(String(100), comment="Human-readable name")


class BLSampleImageScore(Base):
    __tablename__ = "BLSampleImageScore"

    blSampleImageScoreId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))
    score = Column(Float)
    colour = Column(String(15))


class BeamLineSetup(Base):
    __tablename__ = "BeamLineSetup"

    beamLineSetupId = Column(INTEGER(10), primary_key=True)
    synchrotronMode = Column(String(255))
    undulatorType1 = Column(String(45))
    undulatorType2 = Column(String(45))
    undulatorType3 = Column(String(45))
    focalSpotSizeAtSample = Column(Float)
    focusingOptic = Column(String(255))
    beamDivergenceHorizontal = Column(Float)
    beamDivergenceVertical = Column(Float)
    polarisation = Column(Float)
    monochromatorType = Column(String(255))
    setupDate = Column(DateTime)
    synchrotronName = Column(String(255))
    maxExpTimePerDataCollection = Column(Float(asdecimal=True))
    minExposureTimePerImage = Column(Float(asdecimal=True))
    goniostatMaxOscillationSpeed = Column(Float(asdecimal=True))
    goniostatMinOscillationWidth = Column(Float(asdecimal=True))
    minTransmission = Column(Float(asdecimal=True))
    CS = Column(Float)
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )


class BeamlineStats(Base):
    __tablename__ = "BeamlineStats"

    beamlineStatsId = Column(INTEGER(10), primary_key=True)
    beamline = Column(String(10))
    recordTimeStamp = Column(DateTime)
    ringCurrent = Column(Float)
    energy = Column(Float)
    gony = Column(Float)
    beamW = Column(Float)
    beamH = Column(Float)
    flux = Column(Float(asdecimal=True))
    scanFileW = Column(String(255))
    scanFileH = Column(String(255))


class CTF(Base):
    __tablename__ = "CTF"

    CTFid = Column(INTEGER(11), primary_key=True)
    motionCorrectionId = Column(INTEGER(11), nullable=False, index=True)
    spectraImageThumbnailFullPath = Column(String(512))
    spectraImageFullPath = Column(String(512))
    defocusU = Column(String(45))
    defocusV = Column(String(45))
    angle = Column(String(45))
    crossCorrelationCoefficient = Column(String(45))
    resolutionLimit = Column(String(45))
    estimatedBfactor = Column(String(45))
    logFilePath = Column(String(512))
    createdTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )


class CalendarHash(Base):
    __tablename__ = "CalendarHash"
    __table_args__ = {
        "comment": "Lets people get to their calendars without logging in using a private (hash) url"
    }

    calendarHashId = Column(INTEGER(10), primary_key=True)
    ckey = Column(String(50))
    hash = Column(String(128))
    beamline = Column(TINYINT(1))


class ComponentSubType(Base):
    __tablename__ = "ComponentSubType"

    componentSubTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(31), nullable=False)
    hasPh = Column(TINYINT(1), server_default=text("0"))


class ComponentType(Base):
    __tablename__ = "ComponentType"

    componentTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(31), nullable=False)


class ConcentrationType(Base):
    __tablename__ = "ConcentrationType"

    concentrationTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(31), nullable=False)
    symbol = Column(String(8), nullable=False)


class CryoemInitialModel(Base):
    __tablename__ = "CryoemInitialModel"
    __table_args__ = {"comment": "Initial cryo-EM model generation results"}

    cryoemInitialModelId = Column(INTEGER(10), primary_key=True)
    resolution = Column(Float, comment="Unit: Angstroms")
    numberOfParticles = Column(INTEGER(10))

    ParticleClassification = relationship(
        "ParticleClassification",
        secondary="ParticleClassification_has_CryoemInitialModel",
    )


class DataAcquisition(Base):
    __tablename__ = "DataAcquisition"

    dataAcquisitionId = Column(INTEGER(11), primary_key=True)
    sampleCellId = Column(INTEGER(11), nullable=False)
    framesCount = Column(String(45))
    energy = Column(String(45))
    waitTime = Column(String(45))
    detectorDistance = Column(String(45))


class DataReductionStatus(Base):
    __tablename__ = "DataReductionStatus"

    dataReductionStatusId = Column(INTEGER(10), primary_key=True)
    dataCollectionId = Column(INTEGER(10), nullable=False)
    status = Column(String(15))
    filename = Column(String(255))
    message = Column(String(255))


class DatamatrixInSampleChanger(Base):
    __tablename__ = "DatamatrixInSampleChanger"

    datamatrixInSampleChangerId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(
        INTEGER(10), nullable=False, index=True, server_default=text("0")
    )
    beamLineName = Column(String(45))
    datamatrixCode = Column(String(45))
    locationInContainer = Column(INTEGER(11))
    containerLocationInSC = Column(INTEGER(11))
    containerDatamatrixCode = Column(String(45))
    bltimeStamp = Column(TIMESTAMP)


class Detector(Base):
    __tablename__ = "Detector"
    __table_args__ = (
        Index(
            "Detector_FKIndex1",
            "detectorType",
            "detectorManufacturer",
            "detectorModel",
            "detectorPixelSizeHorizontal",
            "detectorPixelSizeVertical",
        ),
        {"comment": "Detector table is linked to a dataCollection"},
    )

    detectorId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    detectorType = Column(String(255))
    detectorManufacturer = Column(String(255))
    detectorModel = Column(String(255))
    detectorPixelSizeHorizontal = Column(Float)
    detectorPixelSizeVertical = Column(Float)
    detectorSerialNumber = Column(String(30), unique=True)
    detectorDistanceMin = Column(Float(asdecimal=True))
    detectorDistanceMax = Column(Float(asdecimal=True))
    trustedPixelValueRangeLower = Column(Float(asdecimal=True))
    trustedPixelValueRangeUpper = Column(Float(asdecimal=True))
    sensorThickness = Column(Float)
    overload = Column(Float)
    XGeoCorr = Column(String(255))
    YGeoCorr = Column(String(255))
    detectorMode = Column(String(255))
    detectorMaxResolution = Column(Float)
    detectorMinResolution = Column(Float)
    CS = Column(Float, comment="Unit: mm")
    density = Column(Float)
    composition = Column(String(16))
    localName = Column(String(40), comment="Colloquial name for the detector")


class DewarLocation(Base):
    __tablename__ = "DewarLocation"
    __table_args__ = {"comment": "ISPyB Dewar location table"}

    eventId = Column(INTEGER(10), primary_key=True)
    dewarNumber = Column(String(128), nullable=False, comment="Dewar number")
    userId = Column(String(128), comment="User who locates the dewar")
    dateTime = Column(DateTime, comment="Date and time of locatization")
    locationName = Column(String(128), comment="Location of the dewar")
    courierName = Column(
        String(128), comment="Carrier name who's shipping back the dewar"
    )
    courierTrackingNumber = Column(
        String(128), comment="Tracking number of the shippment"
    )


class DewarLocationList(Base):
    __tablename__ = "DewarLocationList"
    __table_args__ = {"comment": "List of locations for dewars"}

    locationId = Column(INTEGER(10), primary_key=True)
    locationName = Column(
        String(128), nullable=False, server_default=text("''"), comment="Location"
    )


class DiffractionPlan(Base):
    __tablename__ = "DiffractionPlan"

    diffractionPlanId = Column(INTEGER(10), primary_key=True)
    xmlDocumentId = Column(INTEGER(10))
    experimentKind = Column(
        Enum(
            "Default",
            "MXPressE",
            "MXPressF",
            "MXPressO",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressI",
            "MXPressE_SAD",
            "MXScore",
            "MXPressM",
            "MAD",
            "SAD",
            "Fixed",
            "Ligand binding",
            "Refinement",
            "OSC",
            "MAD - Inverse Beam",
            "SAD - Inverse Beam",
        )
    )
    observedResolution = Column(Float)
    minimalResolution = Column(Float)
    exposureTime = Column(Float)
    oscillationRange = Column(Float)
    maximalResolution = Column(Float)
    screeningResolution = Column(Float)
    radiationSensitivity = Column(Float)
    anomalousScatterer = Column(String(255))
    preferredBeamSizeX = Column(Float)
    preferredBeamSizeY = Column(Float)
    preferredBeamDiameter = Column(Float)
    comments = Column(String(1024))
    aimedCompleteness = Column(Float(asdecimal=True))
    aimedIOverSigmaAtHighestRes = Column(Float(asdecimal=True))
    aimedMultiplicity = Column(Float(asdecimal=True))
    aimedResolution = Column(Float(asdecimal=True))
    anomalousData = Column(TINYINT(1), server_default=text("0"))
    complexity = Column(String(45))
    estimateRadiationDamage = Column(TINYINT(1), server_default=text("0"))
    forcedSpaceGroup = Column(String(45))
    requiredCompleteness = Column(Float(asdecimal=True))
    requiredMultiplicity = Column(Float(asdecimal=True))
    requiredResolution = Column(Float(asdecimal=True))
    strategyOption = Column(String(45))
    kappaStrategyOption = Column(String(45))
    numberOfPositions = Column(INTEGER(11))
    minDimAccrossSpindleAxis = Column(
        Float(asdecimal=True), comment="minimum dimension accross the spindle axis"
    )
    maxDimAccrossSpindleAxis = Column(
        Float(asdecimal=True), comment="maximum dimension accross the spindle axis"
    )
    radiationSensitivityBeta = Column(Float(asdecimal=True))
    radiationSensitivityGamma = Column(Float(asdecimal=True))
    minOscWidth = Column(Float)
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    diffractionPlanUUID = Column(String(1000))
    dataCollectionPlanGroupId = Column(INTEGER(10))
    detectorId = Column(INTEGER(11))
    distance = Column(Float(asdecimal=True))
    orientation = Column(Float(asdecimal=True))
    monoBandwidth = Column(Float(asdecimal=True))
    monochromator = Column(String(8), comment="DMM or DCM")
    energy = Column(Float, comment="eV")
    transmission = Column(Float, comment="Decimal fraction in range [0,1]")
    boxSizeX = Column(Float, comment="microns")
    boxSizeY = Column(Float, comment="microns")
    kappaStart = Column(Float, comment="degrees")
    axisStart = Column(Float, comment="degrees")
    axisRange = Column(Float, comment="degrees")
    numberOfImages = Column(MEDIUMINT(9), comment="The number of images requested")
    presetForProposalId = Column(
        INTEGER(10),
        comment="Indicates this plan is available to all sessions on given proposal",
    )
    beamLineName = Column(
        String(45),
        comment="Indicates this plan is available to all sessions on given beamline",
    )
    userPath = Column(
        String(100),
        comment='User-specified relative "root" path inside the session directory to be used for holding collected data',
    )


class EMMicroscope(Base):
    __tablename__ = "EMMicroscope"

    emMicroscopeId = Column(INTEGER(10), primary_key=True)
    instrumentName = Column(String(100), nullable=False)
    voltage = Column(Float)
    CS = Column(Float, comment="Unit: mm")
    detectorPixelSize = Column(Float)
    C2aperture = Column(Float)
    ObjAperture = Column(Float)
    C2lens = Column(Float)


class Frame(Base):
    __tablename__ = "Frame"

    frameId = Column(INTEGER(11), primary_key=True)
    filePath = Column(String(255), index=True)
    comments = Column(String(45))
    creationDate = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    frameSetId = Column(INTEGER(10))


class FrameList(Base):
    __tablename__ = "FrameList"

    frameListId = Column(INTEGER(11), primary_key=True)
    comments = Column(INTEGER(11))


class GeometryClassname(Base):
    __tablename__ = "GeometryClassname"

    geometryClassnameId = Column(INTEGER(10), primary_key=True)
    geometryClassname = Column(String(45))
    geometryOrder = Column(INTEGER(11), nullable=False)


class Imager(Base):
    __tablename__ = "Imager"

    imagerId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45), nullable=False)
    temperature = Column(Float)
    serial = Column(String(45))
    capacity = Column(SMALLINT(6))


class InitialModel(Base):
    __tablename__ = "InitialModel"
    __table_args__ = {"comment": "Initial model generation results"}

    initialModelId = Column(INTEGER(10), primary_key=True)
    resolution = Column(Float, comment="Unit: Angstroms")
    numberOfParticles = Column(INTEGER(10))


class InputParameterWorkflow(Base):
    __tablename__ = "InputParameterWorkflow"

    inputParameterId = Column(INTEGER(11), primary_key=True)
    workflowId = Column(INTEGER(11), nullable=False)
    parameterType = Column(String(255))
    name = Column(String(255))
    value = Column(String(255))
    comments = Column(String(2048))


class InspectionType(Base):
    __tablename__ = "InspectionType"

    inspectionTypeId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))


class InstructionSet(Base):
    __tablename__ = "InstructionSet"

    instructionSetId = Column(INTEGER(11), primary_key=True)
    type = Column(String(50))


class IspybAutoProcAttachment(Base):
    __tablename__ = "IspybAutoProcAttachment"
    __table_args__ = {"comment": "ISPyB autoProcAttachment files values"}

    autoProcAttachmentId = Column(INTEGER(11), primary_key=True)
    fileName = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    step = Column(
        Enum("XDS", "XSCALE", "SCALA", "SCALEPACK", "TRUNCATE", "DIMPLE"),
        server_default=text("'XDS'"),
        comment="step where the file is generated",
    )
    fileCategory = Column(
        Enum("input", "output", "log", "correction"), server_default=text("'output'")
    )
    hasGraph = Column(TINYINT(1), nullable=False, server_default=text("0"))


class IspybCrystalClass(Base):
    __tablename__ = "IspybCrystalClass"
    __table_args__ = {"comment": "ISPyB crystal class values"}

    crystalClassId = Column(INTEGER(11), primary_key=True)
    crystalClass_code = Column(String(20), nullable=False)
    crystalClass_name = Column(String(255), nullable=False)


class IspybReference(Base):
    __tablename__ = "IspybReference"

    referenceId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    referenceName = Column(String(255), comment="reference name")
    referenceUrl = Column(String(1024), comment="url of the reference")
    referenceBibtext = Column(LargeBinary, comment="bibtext value of the reference")
    beamline = Column(
        Enum(
            "All",
            "ID14-4",
            "ID23-1",
            "ID23-2",
            "ID29",
            "ID30A-1",
            "ID30A-2",
            "XRF",
            "AllXRF",
            "Mesh",
        ),
        comment="beamline involved",
    )


class Laboratory(Base):
    __tablename__ = "Laboratory"

    laboratoryId = Column(INTEGER(10), primary_key=True)
    laboratoryUUID = Column(String(45))
    name = Column(String(45))
    address = Column(String(255))
    city = Column(String(45))
    country = Column(String(45))
    url = Column(String(255))
    organization = Column(String(45))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    laboratoryExtPk = Column(INTEGER(11))


class Log4Stat(Base):
    __tablename__ = "Log4Stat"

    id = Column(INTEGER(11), primary_key=True)
    priority = Column(String(15))
    timestamp = Column(DateTime)
    msg = Column(String(255))
    detail = Column(String(255))
    value = Column(String(255))


class Login(Base):
    __tablename__ = "Login"

    loginId = Column(INTEGER(11), primary_key=True)
    token = Column(String(45), nullable=False, index=True)
    username = Column(String(45), nullable=False)
    roles = Column(String(1024), nullable=False)
    siteId = Column(String(45))
    authorized = Column(String(1024))
    expirationTime = Column(DateTime, nullable=False)


class MeasurementUnit(Base):
    __tablename__ = "MeasurementUnit"

    measurementUnitId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    unitType = Column(String(45))


class Model(Base):
    __tablename__ = "Model"

    modelId = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    pdbFile = Column(String(255))
    fitFile = Column(String(255))
    firFile = Column(String(255))
    logFile = Column(String(255))
    rFactor = Column(String(45))
    chiSqrt = Column(String(45))
    volume = Column(String(45))
    rg = Column(String(45))
    dMax = Column(String(45))


class ModelList(Base):
    __tablename__ = "ModelList"

    modelListId = Column(INTEGER(11), primary_key=True)
    nsdFilePath = Column(String(255))
    chi2RgFilePath = Column(String(255))


class MotorPosition(Base):
    __tablename__ = "MotorPosition"

    motorPositionId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phiX = Column(Float(asdecimal=True))
    phiY = Column(Float(asdecimal=True))
    phiZ = Column(Float(asdecimal=True))
    sampX = Column(Float(asdecimal=True))
    sampY = Column(Float(asdecimal=True))
    omega = Column(Float(asdecimal=True))
    kappa = Column(Float(asdecimal=True))
    phi = Column(Float(asdecimal=True))
    chi = Column(Float(asdecimal=True))
    gridIndexY = Column(INTEGER(11))
    gridIndexZ = Column(INTEGER(11))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )


class PDB(Base):
    __tablename__ = "PDB"

    pdbId = Column(INTEGER(10), primary_key=True)
    name = Column(String(255))
    contents = Column(MEDIUMTEXT)
    code = Column(String(4))


class PHPSession(Base):
    __tablename__ = "PHPSession"

    id = Column(String(50), primary_key=True)
    accessDate = Column(DateTime)
    data = Column(String(4000))


class Permission(Base):
    __tablename__ = "Permission"

    permissionId = Column(INTEGER(10), primary_key=True)
    type = Column(String(15), nullable=False)
    description = Column(String(100))

    UserGroup = relationship("UserGroup", secondary="UserGroup_has_Permission")


class PhasingAnalysis(Base):
    __tablename__ = "PhasingAnalysis"

    phasingAnalysisId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")


class PhasingProgramRun(Base):
    __tablename__ = "PhasingProgramRun"

    phasingProgramRunId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingCommandLine = Column(String(255), comment="Command line for phasing")
    phasingPrograms = Column(String(255), comment="Phasing programs (comma separated)")
    phasingStatus = Column(TINYINT(1), comment="success (1) / fail (0)")
    phasingMessage = Column(String(255), comment="warning, error,...")
    phasingStartTime = Column(DateTime, comment="Processing start time")
    phasingEndTime = Column(DateTime, comment="Processing end time")
    phasingEnvironment = Column(String(255), comment="Cpus, Nodes,...")
    phasingDirectory = Column(String(255), comment="Directory of execution")
    recordTimeStamp = Column(
        TIMESTAMP,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )


class PlateGroup(Base):
    __tablename__ = "PlateGroup"

    plateGroupId = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    storageTemperature = Column(String(45))


class PlateType(Base):
    __tablename__ = "PlateType"

    PlateTypeId = Column(INTEGER(11), primary_key=True)
    experimentId = Column(INTEGER(11), index=True)
    name = Column(String(45))
    description = Column(String(45))
    shape = Column(String(45))
    rowCount = Column(INTEGER(11))
    columnCount = Column(INTEGER(11))


class Position(Base):
    __tablename__ = "Position"

    positionId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    relativePositionId = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="relative position, null otherwise",
    )
    posX = Column(Float(asdecimal=True))
    posY = Column(Float(asdecimal=True))
    posZ = Column(Float(asdecimal=True))
    scale = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    parent = relationship("Position", remote_side=[positionId])


class RigidBodyModeling(Base):
    __tablename__ = "RigidBodyModeling"

    rigidBodyModelingId = Column(INTEGER(11), primary_key=True)
    subtractionId = Column(INTEGER(11), nullable=False, index=True)
    fitFilePath = Column(String(255))
    rigidBodyModelFilePath = Column(String(255))
    logFilePath = Column(String(255))
    curveConfigFilePath = Column(String(255))
    subUnitConfigFilePath = Column(String(255))
    crossCorrConfigFilePath = Column(String(255))
    contactDescriptionFilePath = Column(String(255))
    symmetry = Column(String(255))
    creationDate = Column(String(45))


class Run(Base):
    __tablename__ = "Run"

    runId = Column(INTEGER(11), primary_key=True)
    timePerFrame = Column(String(45))
    timeStart = Column(String(45))
    timeEnd = Column(String(45))
    storageTemperature = Column(String(45))
    exposureTemperature = Column(String(45))
    spectrophotometer = Column(String(45))
    energy = Column(String(45))
    creationDate = Column(DateTime)
    frameAverage = Column(String(45))
    frameCount = Column(String(45))
    transmission = Column(String(45))
    beamCenterX = Column(String(45))
    beamCenterY = Column(String(45))
    pixelSizeX = Column(String(45))
    pixelSizeY = Column(String(45))
    radiationRelative = Column(String(45))
    radiationAbsolute = Column(String(45))
    normalization = Column(String(45))


class SafetyLevel(Base):
    __tablename__ = "SafetyLevel"

    safetyLevelId = Column(INTEGER(11), primary_key=True)
    code = Column(String(45))
    description = Column(String(45))


class ScanParametersService(Base):
    __tablename__ = "ScanParametersService"

    scanParametersServiceId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))
    description = Column(String(45))


class Schedule(Base):
    __tablename__ = "Schedule"

    scheduleId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))


class SchemaStatus(Base):
    __tablename__ = "SchemaStatus"

    schemaStatusId = Column(INTEGER(11), primary_key=True)
    scriptName = Column(String(100), nullable=False, unique=True)
    schemaStatus = Column(String(10))
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )


class ScreeningRankSet(Base):
    __tablename__ = "ScreeningRankSet"

    screeningRankSetId = Column(INTEGER(10), primary_key=True)
    rankEngine = Column(String(255))
    rankingProjectFileName = Column(String(255))
    rankingSummaryFileName = Column(String(255))


class Superposition(Base):
    __tablename__ = "Superposition"

    superpositionId = Column(INTEGER(11), primary_key=True)
    subtractionId = Column(INTEGER(11), nullable=False, index=True)
    abinitioModelPdbFilePath = Column(String(255))
    aprioriPdbFilePath = Column(String(255))
    alignedPdbFilePath = Column(String(255))
    creationDate = Column(DateTime)


class UserGroup(Base):
    __tablename__ = "UserGroup"

    userGroupId = Column(INTEGER(10), primary_key=True)
    name = Column(String(31), nullable=False, unique=True)


t_V_AnalysisInfo = Table(
    "V_AnalysisInfo",
    metadata,
    Column("experimentCreationDate", DateTime),
    Column("timeStart", String(45)),
    Column("dataCollectionId", INTEGER(11), server_default=text("'0'")),
    Column("measurementId", INTEGER(11), server_default=text("'0'")),
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("priorityLevelId", INTEGER(11)),
    Column("code", String(100)),
    Column("exposureTemperature", String(45)),
    Column("transmission", String(45)),
    Column("measurementComments", String(512)),
    Column("experimentComments", String(512)),
    Column("experimentId", INTEGER(11), server_default=text("'0'")),
    Column("experimentType", String(128)),
    Column("conc", String(45)),
    Column("bufferAcronym", String(45)),
    Column("macromoleculeAcronym", String(45)),
    Column("bufferId", INTEGER(11), server_default=text("'0'")),
    Column("macromoleculeId", INTEGER(11), server_default=text("'0'")),
    Column("subtractedFilePath", String(255)),
    Column("rgGuinier", String(45)),
    Column("firstPointUsed", String(45)),
    Column("lastPointUsed", String(45)),
    Column("I0", String(45)),
    Column("isagregated", String(45)),
    Column("subtractionId", INTEGER(11)),
    Column("rgGnom", String(45)),
    Column("total", String(45)),
    Column("dmax", String(45)),
    Column("volume", String(45)),
    Column("i0stdev", String(45)),
    Column("quality", String(45)),
    Column("substractionCreationTime", DateTime),
    Column("bufferBeforeMeasurementId", INTEGER(11)),
    Column("bufferAfterMeasurementId", INTEGER(11)),
    Column("bufferBeforeFramesMerged", String(45)),
    Column("bufferBeforeMergeId", INTEGER(11)),
    Column("bufferBeforeAverageFilePath", String(255)),
    Column("sampleMeasurementId", INTEGER(11)),
    Column("sampleMergeId", INTEGER(11)),
    Column("averageFilePath", String(255)),
    Column("framesMerge", String(45)),
    Column("framesCount", String(45)),
    Column("bufferAfterFramesMerged", String(45)),
    Column("bufferAfterMergeId", INTEGER(11)),
    Column("bufferAfterAverageFilePath", String(255)),
    Column("modelListId1", INTEGER(11)),
    Column("nsdFilePath", String(255)),
    Column("modelListId2", INTEGER(11)),
    Column("chi2RgFilePath", String(255)),
    Column("averagedModel", String(255)),
    Column("averagedModelId", INTEGER(11)),
    Column("rapidShapeDeterminationModel", String(255)),
    Column("rapidShapeDeterminationModelId", INTEGER(11)),
    Column("shapeDeterminationModel", String(255)),
    Column("shapeDeterminationModelId", INTEGER(11)),
    Column("abInitioModelId", INTEGER(11)),
    Column("comments", String(512)),
)


class Workflow(Base):
    __tablename__ = "Workflow"

    workflowId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    workflowTitle = Column(String(255))
    workflowType = Column(
        Enum(
            "Characterisation",
            "Undefined",
            "BioSAXS Post Processing",
            "EnhancedCharacterisation",
            "LineScan",
            "MeshScan",
            "Dehydration",
            "KappaReorientation",
            "BurnStrategy",
            "XrayCentering",
            "DiffractionTomography",
            "TroubleShooting",
            "VisualReorientation",
            "HelicalCharacterisation",
            "GroupedProcessing",
            "MXPressE",
            "MXPressO",
            "MXPressL",
            "MXScore",
            "MXPressI",
            "MXPressM",
            "MXPressA",
            "CollectAndSpectra",
            "LowDoseDC",
            "EnergyInterleavedMAD",
            "MXPressF",
            "MXPressH",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressR",
            "MXPressR_180",
            "MXPressR_dehydration",
            "MeshAndCollect",
            "MeshAndCollectFromFile",
        )
    )
    workflowTypeId = Column(INTEGER(11))
    comments = Column(String(1024))
    status = Column(String(255))
    resultFilePath = Column(String(255))
    logFilePath = Column(String(255))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")


class WorkflowType(Base):
    __tablename__ = "WorkflowType"

    workflowTypeId = Column(INTEGER(11), primary_key=True)
    workflowTypeName = Column(String(45))
    comments = Column(String(2048))
    recordTimeStamp = Column(TIMESTAMP)


class XRFFluorescenceMappingROI(Base):
    __tablename__ = "XRFFluorescenceMappingROI"

    xrfFluorescenceMappingROIId = Column(INTEGER(10), primary_key=True)
    startEnergy = Column(Float, nullable=False)
    endEnergy = Column(Float, nullable=False)
    element = Column(String(2))
    edge = Column(String(2), comment="In future may be changed to enum(K, L)")
    r = Column(TINYINT(3), comment="R colour component")
    g = Column(TINYINT(3), comment="G colour component")
    b = Column(TINYINT(3), comment="B colour component")


t_v_Log4Stat = Table(
    "v_Log4Stat",
    metadata,
    Column("id", INTEGER(11), server_default=text("'0'")),
    Column("priority", String(15)),
    Column("timestamp", DateTime),
    Column("msg", String(255)),
    Column("detail", String(255)),
    Column("value", String(255)),
)


t_v_datacollection = Table(
    "v_datacollection",
    metadata,
    Column("dataCollectionId", INTEGER(10), server_default=text("'0'")),
    Column("dataCollectionGroupId", INTEGER(11)),
    Column("strategySubWedgeOrigId", INTEGER(10)),
    Column("detectorId", INTEGER(11)),
    Column("blSubSampleId", INTEGER(10)),
    Column("dataCollectionNumber", INTEGER(10)),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("runStatus", String(45)),
    Column("axisStart", Float),
    Column("axisEnd", Float),
    Column("axisRange", Float),
    Column("overlap", Float),
    Column("numberOfImages", INTEGER(10)),
    Column("startImageNumber", INTEGER(10)),
    Column("numberOfPasses", INTEGER(10)),
    Column("exposureTime", Float),
    Column("imageDirectory", String(255)),
    Column("imagePrefix", String(100)),
    Column("imageSuffix", String(45)),
    Column("fileTemplate", String(255)),
    Column("wavelength", Float),
    Column("resolution", Float),
    Column("detectorDistance", Float),
    Column("xBeam", Float),
    Column("yBeam", Float),
    Column("xBeamPix", Float),
    Column("yBeamPix", Float),
    Column("comments", String(1024)),
    Column("printableForReport", TINYINT(3), server_default=text("'1'")),
    Column("slitGapVertical", Float),
    Column("slitGapHorizontal", Float),
    Column("transmission", Float),
    Column("synchrotronMode", String(20)),
    Column("xtalSnapshotFullPath1", String(255)),
    Column("xtalSnapshotFullPath2", String(255)),
    Column("xtalSnapshotFullPath3", String(255)),
    Column("xtalSnapshotFullPath4", String(255)),
    Column("rotationAxis", Enum("Omega", "Kappa", "Phi")),
    Column("phiStart", Float),
    Column("kappaStart", Float),
    Column("omegaStart", Float),
    Column("resolutionAtCorner", Float),
    Column("detector2Theta", Float),
    Column("undulatorGap1", Float),
    Column("undulatorGap2", Float),
    Column("undulatorGap3", Float),
    Column("beamSizeAtSampleX", Float),
    Column("beamSizeAtSampleY", Float),
    Column("centeringMethod", String(255)),
    Column("averageTemperature", Float),
    Column("actualCenteringPosition", String(255)),
    Column("beamShape", String(45)),
    Column("flux", Float(asdecimal=True)),
    Column("flux_end", Float(asdecimal=True)),
    Column("totalAbsorbedDose", Float(asdecimal=True)),
    Column("bestWilsonPlotPath", String(255)),
    Column("imageQualityIndicatorsPlotPath", String(512)),
    Column("imageQualityIndicatorsCSVPath", String(512)),
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("workflowId", INTEGER(10)),
    Column("AutoProcIntegration_dataCollectionId", INTEGER(10)),
    Column("autoProcScalingId", INTEGER(10), server_default=text("'0'")),
    Column("cell_a", Float),
    Column("cell_b", Float),
    Column("cell_c", Float),
    Column("cell_alpha", Float),
    Column("cell_beta", Float),
    Column("cell_gamma", Float),
    Column("anomalous", TINYINT(1), server_default=text("'0'")),
    Column(
        "scalingStatisticsType",
        Enum("overall", "innerShell", "outerShell"),
        server_default=text("'overall'"),
    ),
    Column("resolutionLimitHigh", Float),
    Column("resolutionLimitLow", Float),
    Column("completeness", Float),
    Column("AutoProc_spaceGroup", String(45)),
    Column("autoProcId", INTEGER(10), server_default=text("'0'")),
    Column("rMerge", Float),
    Column("ccHalf", Float),
    Column("meanIOverSigI", Float),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("AutoProcProgram_processingPrograms", String(255)),
    Column(
        "AutoProcProgram_processingStatus",
        Enum("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column(
        "AutoProcProgram_autoProcProgramId", INTEGER(10), server_default=text("'0'")
    ),
    Column("ScreeningOutput_rankingResolution", Float(asdecimal=True)),
)


t_v_datacollection_autoprocintegration = Table(
    "v_datacollection_autoprocintegration",
    metadata,
    Column(
        "v_datacollection_summary_phasing_autoProcIntegrationId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("v_datacollection_summary_phasing_dataCollectionId", INTEGER(10)),
    Column("v_datacollection_summary_phasing_cell_a", Float),
    Column("v_datacollection_summary_phasing_cell_b", Float),
    Column("v_datacollection_summary_phasing_cell_c", Float),
    Column("v_datacollection_summary_phasing_cell_alpha", Float),
    Column("v_datacollection_summary_phasing_cell_beta", Float),
    Column("v_datacollection_summary_phasing_cell_gamma", Float),
    Column(
        "v_datacollection_summary_phasing_anomalous",
        TINYINT(1),
        server_default=text("'0'"),
    ),
    Column("v_datacollection_summary_phasing_autoproc_space_group", String(45)),
    Column(
        "v_datacollection_summary_phasing_autoproc_autoprocId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "v_datacollection_summary_phasing_autoProcScalingId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("v_datacollection_processingPrograms", String(255)),
    Column(
        "v_datacollection_summary_phasing_autoProcProgramId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "v_datacollection_processingStatus",
        Enum("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column("v_datacollection_processingStartTime", DateTime),
    Column("v_datacollection_processingEndTime", DateTime),
    Column(
        "v_datacollection_summary_session_sessionId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "v_datacollection_summary_session_proposalId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("AutoProcIntegration_dataCollectionId", INTEGER(10)),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "PhasingStep_phasing_phasingStepType",
        Enum(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("SpaceGroup_spaceGroupShortName", String(45)),
    Column("Protein_proteinId", INTEGER(10), server_default=text("'0'")),
    Column("Protein_acronym", String(45)),
    Column("BLSample_name", String(100)),
    Column("DataCollection_dataCollectionNumber", INTEGER(10)),
    Column("DataCollection_imagePrefix", String(100)),
)


t_v_datacollection_phasing = Table(
    "v_datacollection_phasing",
    metadata,
    Column("phasingStepId", INTEGER(10), server_default=text("'0'")),
    Column("previousPhasingStepId", INTEGER(10)),
    Column("phasingAnalysisId", INTEGER(10)),
    Column("autoProcIntegrationId", INTEGER(10), server_default=text("'0'")),
    Column("dataCollectionId", INTEGER(10)),
    Column("anomalous", TINYINT(1), server_default=text("'0'")),
    Column("spaceGroup", String(45)),
    Column("autoProcId", INTEGER(10), server_default=text("'0'")),
    Column(
        "phasingStepType",
        Enum(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("method", String(45)),
    Column("solventContent", String(45)),
    Column("enantiomorph", String(45)),
    Column("lowRes", String(45)),
    Column("highRes", String(45)),
    Column("autoProcScalingId", INTEGER(10), server_default=text("'0'")),
    Column("spaceGroupShortName", String(45)),
    Column("processingPrograms", String(255)),
    Column("processingStatus", Enum("RUNNING", "FAILED", "SUCCESS", "0", "1")),
    Column("phasingPrograms", String(255)),
    Column("phasingStatus", TINYINT(1)),
    Column("phasingStartTime", DateTime),
    Column("phasingEndTime", DateTime),
    Column("sessionId", INTEGER(10)),
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("blSampleId", INTEGER(10), server_default=text("'0'")),
    Column("name", String(100)),
    Column("code", String(45)),
    Column("acronym", String(45)),
    Column("proteinId", INTEGER(10), server_default=text("'0'")),
)


t_v_datacollection_phasing_program_run = Table(
    "v_datacollection_phasing_program_run",
    metadata,
    Column("phasingStepId", INTEGER(10), server_default=text("'0'")),
    Column("previousPhasingStepId", INTEGER(10)),
    Column("phasingAnalysisId", INTEGER(10)),
    Column("autoProcIntegrationId", INTEGER(10), server_default=text("'0'")),
    Column("dataCollectionId", INTEGER(10)),
    Column("autoProcId", INTEGER(10), server_default=text("'0'")),
    Column(
        "phasingStepType",
        Enum(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("method", String(45)),
    Column("autoProcScalingId", INTEGER(10), server_default=text("'0'")),
    Column("spaceGroupShortName", String(45)),
    Column("phasingPrograms", String(255)),
    Column("phasingStatus", TINYINT(1)),
    Column("sessionId", INTEGER(10)),
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("blSampleId", INTEGER(10), server_default=text("'0'")),
    Column("name", String(100)),
    Column("code", String(45)),
    Column("acronym", String(45)),
    Column("proteinId", INTEGER(10), server_default=text("'0'")),
    Column("phasingProgramAttachmentId", INTEGER(10), server_default=text("'0'")),
    Column(
        "fileType",
        Enum(
            "DSIGMA_RESOLUTION",
            "OCCUPANCY_SITENUMBER",
            "CONTRAST_CYCLE",
            "CCALL_CCWEAK",
            "IMAGE",
            "Map",
            "Logfile",
            "PDB",
            "CSV",
            "INS",
            "RES",
            "TXT",
        ),
    ),
    Column("fileName", String(45)),
    Column("filePath", String(255)),
)


t_v_datacollection_summary = Table(
    "v_datacollection_summary",
    metadata,
    Column(
        "DataCollectionGroup_dataCollectionGroupId",
        INTEGER(11),
        server_default=text("'0'"),
    ),
    Column("DataCollectionGroup_blSampleId", INTEGER(10)),
    Column("DataCollectionGroup_sessionId", INTEGER(10)),
    Column("DataCollectionGroup_workflowId", INTEGER(10)),
    Column(
        "DataCollectionGroup_experimentType",
        Enum(
            "EM",
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "Still",
        ),
    ),
    Column("DataCollectionGroup_startTime", DateTime),
    Column("DataCollectionGroup_endTime", DateTime),
    Column("DataCollectionGroup_comments", String(1024)),
    Column("DataCollectionGroup_actualSampleBarcode", String(45)),
    Column("DataCollectionGroup_xtalSnapshotFullPath", String(255)),
    Column("DataCollectionGroup_crystalClass", String(20)),
    Column("BLSample_blSampleId", INTEGER(10), server_default=text("'0'")),
    Column("BLSample_crystalId", INTEGER(10)),
    Column("BLSample_name", String(100)),
    Column("BLSample_code", String(45)),
    Column("BLSample_location", String(45)),
    Column("BLSample_blSampleStatus", String(20)),
    Column("BLSample_comments", String(1024)),
    Column("Container_containerId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_sessionId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_proposalId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_protectedData", String(1024)),
    Column("Dewar_dewarId", INTEGER(10), server_default=text("'0'")),
    Column("Dewar_code", String(45)),
    Column("Dewar_storageLocation", String(45)),
    Column("Container_containerType", String(20)),
    Column("Container_code", String(45)),
    Column("Container_capacity", INTEGER(10)),
    Column("Container_beamlineLocation", String(20)),
    Column("Container_sampleChangerLocation", String(20)),
    Column("Protein_proteinId", INTEGER(10), server_default=text("'0'")),
    Column("Protein_name", String(255)),
    Column("Protein_acronym", String(45)),
    Column("DataCollection_dataCollectionId", INTEGER(10), server_default=text("'0'")),
    Column("DataCollection_dataCollectionGroupId", INTEGER(11)),
    Column("DataCollection_startTime", DateTime),
    Column("DataCollection_endTime", DateTime),
    Column("DataCollection_runStatus", String(45)),
    Column("DataCollection_numberOfImages", INTEGER(10)),
    Column("DataCollection_startImageNumber", INTEGER(10)),
    Column("DataCollection_numberOfPasses", INTEGER(10)),
    Column("DataCollection_exposureTime", Float),
    Column("DataCollection_imageDirectory", String(255)),
    Column("DataCollection_wavelength", Float),
    Column("DataCollection_resolution", Float),
    Column("DataCollection_detectorDistance", Float),
    Column("DataCollection_xBeam", Float),
    Column("transmission", Float),
    Column("DataCollection_yBeam", Float),
    Column("DataCollection_imagePrefix", String(100)),
    Column("DataCollection_comments", String(1024)),
    Column("DataCollection_xtalSnapshotFullPath1", String(255)),
    Column("DataCollection_xtalSnapshotFullPath2", String(255)),
    Column("DataCollection_xtalSnapshotFullPath3", String(255)),
    Column("DataCollection_xtalSnapshotFullPath4", String(255)),
    Column("DataCollection_phiStart", Float),
    Column("DataCollection_kappaStart", Float),
    Column("DataCollection_omegaStart", Float),
    Column("DataCollection_flux", Float(asdecimal=True)),
    Column("DataCollection_flux_end", Float(asdecimal=True)),
    Column("DataCollection_resolutionAtCorner", Float),
    Column("DataCollection_bestWilsonPlotPath", String(255)),
    Column("DataCollection_dataCollectionNumber", INTEGER(10)),
    Column("DataCollection_axisRange", Float),
    Column("DataCollection_axisStart", Float),
    Column("DataCollection_axisEnd", Float),
    Column("DataCollection_rotationAxis", Enum("Omega", "Kappa", "Phi")),
    Column("DataCollection_undulatorGap1", Float),
    Column("DataCollection_undulatorGap2", Float),
    Column("DataCollection_undulatorGap3", Float),
    Column("beamSizeAtSampleX", Float),
    Column("beamSizeAtSampleY", Float),
    Column("DataCollection_slitGapVertical", Float),
    Column("DataCollection_slitGapHorizontal", Float),
    Column("DataCollection_beamShape", String(45)),
    Column("DataCollection_voltage", Float),
    Column("DataCollection_xBeamPix", Float),
    Column("Workflow_workflowTitle", String(255)),
    Column(
        "Workflow_workflowType",
        Enum(
            "Characterisation",
            "Undefined",
            "BioSAXS Post Processing",
            "EnhancedCharacterisation",
            "LineScan",
            "MeshScan",
            "Dehydration",
            "KappaReorientation",
            "BurnStrategy",
            "XrayCentering",
            "DiffractionTomography",
            "TroubleShooting",
            "VisualReorientation",
            "HelicalCharacterisation",
            "GroupedProcessing",
            "MXPressE",
            "MXPressO",
            "MXPressL",
            "MXScore",
            "MXPressI",
            "MXPressM",
            "MXPressA",
            "CollectAndSpectra",
            "LowDoseDC",
            "EnergyInterleavedMAD",
            "MXPressF",
            "MXPressH",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressR",
            "MXPressR_180",
            "MXPressR_dehydration",
            "MeshAndCollect",
            "MeshAndCollectFromFile",
        ),
    ),
    Column("Workflow_status", String(255)),
    Column("Workflow_workflowId", INTEGER(10), server_default=text("'0'")),
    Column("AutoProcIntegration_dataCollectionId", INTEGER(10)),
    Column("autoProcScalingId", INTEGER(10), server_default=text("'0'")),
    Column("cell_a", Float),
    Column("cell_b", Float),
    Column("cell_c", Float),
    Column("cell_alpha", Float),
    Column("cell_beta", Float),
    Column("cell_gamma", Float),
    Column("anomalous", TINYINT(1), server_default=text("'0'")),
    Column(
        "scalingStatisticsType",
        Enum("overall", "innerShell", "outerShell"),
        server_default=text("'overall'"),
    ),
    Column("resolutionLimitHigh", Float),
    Column("resolutionLimitLow", Float),
    Column("completeness", Float),
    Column("AutoProc_spaceGroup", String(45)),
    Column("autoProcId", INTEGER(10), server_default=text("'0'")),
    Column("rMerge", Float),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("AutoProcProgram_processingPrograms", String(255)),
    Column(
        "AutoProcProgram_processingStatus",
        Enum("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column(
        "AutoProcProgram_autoProcProgramId", INTEGER(10), server_default=text("'0'")
    ),
    Column("Screening_screeningId", INTEGER(10), server_default=text("'0'")),
    Column("Screening_dataCollectionId", INTEGER(10)),
    Column("Screening_dataCollectionGroupId", INTEGER(11)),
    Column("ScreeningOutput_strategySuccess", TINYINT(1), server_default=text("'0'")),
    Column("ScreeningOutput_indexingSuccess", TINYINT(1), server_default=text("'0'")),
    Column("ScreeningOutput_rankingResolution", Float(asdecimal=True)),
    Column("ScreeningOutput_mosaicity", Float),
    Column("ScreeningOutputLattice_spaceGroup", String(45)),
    Column("ScreeningOutputLattice_unitCell_a", Float),
    Column("ScreeningOutputLattice_unitCell_b", Float),
    Column("ScreeningOutputLattice_unitCell_c", Float),
    Column("ScreeningOutputLattice_unitCell_alpha", Float),
    Column("ScreeningOutputLattice_unitCell_beta", Float),
    Column("ScreeningOutputLattice_unitCell_gamma", Float),
    Column("ScreeningOutput_totalExposureTime", Float(asdecimal=True)),
    Column("ScreeningOutput_totalRotationRange", Float(asdecimal=True)),
    Column("ScreeningOutput_totalNumberOfImages", INTEGER(11)),
    Column("ScreeningStrategySubWedge_exposureTime", Float),
    Column("ScreeningStrategySubWedge_transmission", Float),
    Column("ScreeningStrategySubWedge_oscillationRange", Float),
    Column("ScreeningStrategySubWedge_numberOfImages", INTEGER(10)),
    Column("ScreeningStrategySubWedge_multiplicity", Float),
    Column("ScreeningStrategySubWedge_completeness", Float),
    Column("ScreeningStrategySubWedge_axisStart", Float),
    Column("Shipping_shippingId", INTEGER(10), server_default=text("'0'")),
    Column("Shipping_shippingName", String(45)),
    Column("Shipping_shippingStatus", String(45)),
    Column("diffractionPlanId", INTEGER(10), server_default=text("'0'")),
    Column(
        "experimentKind",
        Enum(
            "Default",
            "MXPressE",
            "MXPressF",
            "MXPressO",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressI",
            "MXPressE_SAD",
            "MXScore",
            "MXPressM",
            "MAD",
            "SAD",
            "Fixed",
            "Ligand binding",
            "Refinement",
            "OSC",
            "MAD - Inverse Beam",
            "SAD - Inverse Beam",
        ),
    ),
    Column("observedResolution", Float),
    Column("minimalResolution", Float),
    Column("exposureTime", Float),
    Column("oscillationRange", Float),
    Column("maximalResolution", Float),
    Column("screeningResolution", Float),
    Column("radiationSensitivity", Float),
    Column("anomalousScatterer", String(255)),
    Column("preferredBeamSizeX", Float),
    Column("preferredBeamSizeY", Float),
    Column("preferredBeamDiameter", Float),
    Column("DiffractipnPlan_comments", String(1024)),
    Column("aimedCompleteness", Float(asdecimal=True)),
    Column("aimedIOverSigmaAtHighestRes", Float(asdecimal=True)),
    Column("aimedMultiplicity", Float(asdecimal=True)),
    Column("aimedResolution", Float(asdecimal=True)),
    Column("anomalousData", TINYINT(1), server_default=text("'0'")),
    Column("complexity", String(45)),
    Column("estimateRadiationDamage", TINYINT(1), server_default=text("'0'")),
    Column("forcedSpaceGroup", String(45)),
    Column("requiredCompleteness", Float(asdecimal=True)),
    Column("requiredMultiplicity", Float(asdecimal=True)),
    Column("requiredResolution", Float(asdecimal=True)),
    Column("strategyOption", String(45)),
    Column("kappaStrategyOption", String(45)),
    Column("numberOfPositions", INTEGER(11)),
    Column("minDimAccrossSpindleAxis", Float(asdecimal=True)),
    Column("maxDimAccrossSpindleAxis", Float(asdecimal=True)),
    Column("radiationSensitivityBeta", Float(asdecimal=True)),
    Column("radiationSensitivityGamma", Float(asdecimal=True)),
    Column("minOscWidth", Float),
    Column("Detector_detectorType", String(255)),
    Column("Detector_detectorManufacturer", String(255)),
    Column("Detector_detectorModel", String(255)),
    Column("Detector_detectorPixelSizeHorizontal", Float),
    Column("Detector_detectorPixelSizeVertical", Float),
    Column("Detector_detectorSerialNumber", String(30)),
    Column("Detector_detectorDistanceMin", Float(asdecimal=True)),
    Column("Detector_detectorDistanceMax", Float(asdecimal=True)),
    Column("Detector_trustedPixelValueRangeLower", Float(asdecimal=True)),
    Column("Detector_trustedPixelValueRangeUpper", Float(asdecimal=True)),
    Column("Detector_sensorThickness", Float),
    Column("Detector_overload", Float),
    Column("Detector_XGeoCorr", String(255)),
    Column("Detector_YGeoCorr", String(255)),
    Column("Detector_detectorMode", String(255)),
    Column("BeamLineSetup_undulatorType1", String(45)),
    Column("BeamLineSetup_undulatorType2", String(45)),
    Column("BeamLineSetup_undulatorType3", String(45)),
    Column("BeamLineSetup_synchrotronName", String(255)),
    Column("BeamLineSetup_synchrotronMode", String(255)),
    Column("BeamLineSetup_polarisation", Float),
    Column("BeamLineSetup_focusingOptic", String(255)),
    Column("BeamLineSetup_beamDivergenceHorizontal", Float),
    Column("BeamLineSetup_beamDivergenceVertical", Float),
    Column("BeamLineSetup_monochromatorType", String(255)),
)


t_v_datacollection_summary_autoprocintegration = Table(
    "v_datacollection_summary_autoprocintegration",
    metadata,
    Column("AutoProcIntegration_dataCollectionId", INTEGER(10)),
    Column("cell_a", Float),
    Column("cell_b", Float),
    Column("cell_c", Float),
    Column("cell_alpha", Float),
    Column("cell_beta", Float),
    Column("cell_gamma", Float),
    Column("anomalous", TINYINT(1), server_default=text("'0'")),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "v_datacollection_summary_autoprocintegration_processingPrograms", String(255)
    ),
    Column(
        "AutoProcProgram_autoProcProgramId", INTEGER(10), server_default=text("'0'")
    ),
    Column(
        "v_datacollection_summary_autoprocintegration_processingStatus",
        Enum("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column("AutoProcIntegration_phasing_dataCollectionId", INTEGER(10)),
    Column(
        "PhasingStep_phasing_phasingStepType",
        Enum(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("SpaceGroup_spaceGroupShortName", String(45)),
    Column("autoProcId", INTEGER(10), server_default=text("'0'")),
    Column("AutoProc_spaceGroup", String(45)),
    Column(
        "scalingStatisticsType",
        Enum("overall", "innerShell", "outerShell"),
        server_default=text("'overall'"),
    ),
    Column("resolutionLimitHigh", Float),
    Column("resolutionLimitLow", Float),
    Column("rMerge", Float),
    Column("meanIOverSigI", Float),
    Column("ccHalf", Float),
    Column("completeness", Float),
    Column("autoProcScalingId", INTEGER(10), server_default=text("'0'")),
)


t_v_datacollection_summary_datacollectiongroup = Table(
    "v_datacollection_summary_datacollectiongroup",
    metadata,
    Column(
        "DataCollectionGroup_dataCollectionGroupId",
        INTEGER(11),
        server_default=text("'0'"),
    ),
    Column("DataCollectionGroup_blSampleId", INTEGER(10)),
    Column("DataCollectionGroup_sessionId", INTEGER(10)),
    Column("DataCollectionGroup_workflowId", INTEGER(10)),
    Column(
        "DataCollectionGroup_experimentType",
        Enum(
            "EM",
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "Still",
        ),
    ),
    Column("DataCollectionGroup_startTime", DateTime),
    Column("DataCollectionGroup_endTime", DateTime),
    Column("DataCollectionGroup_comments", String(1024)),
    Column("DataCollectionGroup_actualSampleBarcode", String(45)),
    Column("DataCollectionGroup_xtalSnapshotFullPath", String(255)),
    Column("BLSample_blSampleId", INTEGER(10), server_default=text("'0'")),
    Column("BLSample_crystalId", INTEGER(10)),
    Column("BLSample_name", String(100)),
    Column("BLSample_code", String(45)),
    Column("BLSession_sessionId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_proposalId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_protectedData", String(1024)),
    Column("Protein_proteinId", INTEGER(10), server_default=text("'0'")),
    Column("Protein_name", String(255)),
    Column("Protein_acronym", String(45)),
    Column("DataCollection_dataCollectionId", INTEGER(10), server_default=text("'0'")),
    Column("DataCollection_dataCollectionGroupId", INTEGER(11)),
    Column("DataCollection_startTime", DateTime),
    Column("DataCollection_endTime", DateTime),
    Column("DataCollection_runStatus", String(45)),
    Column("DataCollection_numberOfImages", INTEGER(10)),
    Column("DataCollection_startImageNumber", INTEGER(10)),
    Column("DataCollection_numberOfPasses", INTEGER(10)),
    Column("DataCollection_exposureTime", Float),
    Column("DataCollection_imageDirectory", String(255)),
    Column("DataCollection_wavelength", Float),
    Column("DataCollection_resolution", Float),
    Column("DataCollection_detectorDistance", Float),
    Column("DataCollection_xBeam", Float),
    Column("DataCollection_yBeam", Float),
    Column("DataCollection_comments", String(1024)),
    Column("DataCollection_xtalSnapshotFullPath1", String(255)),
    Column("DataCollection_xtalSnapshotFullPath2", String(255)),
    Column("DataCollection_xtalSnapshotFullPath3", String(255)),
    Column("DataCollection_xtalSnapshotFullPath4", String(255)),
    Column("DataCollection_phiStart", Float),
    Column("DataCollection_kappaStart", Float),
    Column("DataCollection_omegaStart", Float),
    Column("DataCollection_resolutionAtCorner", Float),
    Column("DataCollection_bestWilsonPlotPath", String(255)),
    Column("DataCollection_dataCollectionNumber", INTEGER(10)),
    Column("DataCollection_axisRange", Float),
    Column("DataCollection_axisStart", Float),
    Column("DataCollection_axisEnd", Float),
    Column("Workflow_workflowTitle", String(255)),
    Column(
        "Workflow_workflowType",
        Enum(
            "Characterisation",
            "Undefined",
            "BioSAXS Post Processing",
            "EnhancedCharacterisation",
            "LineScan",
            "MeshScan",
            "Dehydration",
            "KappaReorientation",
            "BurnStrategy",
            "XrayCentering",
            "DiffractionTomography",
            "TroubleShooting",
            "VisualReorientation",
            "HelicalCharacterisation",
            "GroupedProcessing",
            "MXPressE",
            "MXPressO",
            "MXPressL",
            "MXScore",
            "MXPressI",
            "MXPressM",
            "MXPressA",
            "CollectAndSpectra",
            "LowDoseDC",
            "EnergyInterleavedMAD",
            "MXPressF",
            "MXPressH",
            "MXPressP",
            "MXPressP_SAD",
            "MXPressR",
            "MXPressR_180",
            "MXPressR_dehydration",
            "MeshAndCollect",
            "MeshAndCollectFromFile",
        ),
    ),
    Column("Workflow_status", String(255)),
)


t_v_datacollection_summary_phasing = Table(
    "v_datacollection_summary_phasing",
    metadata,
    Column(
        "v_datacollection_summary_phasing_autoProcIntegrationId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("v_datacollection_summary_phasing_dataCollectionId", INTEGER(10)),
    Column("v_datacollection_summary_phasing_cell_a", Float),
    Column("v_datacollection_summary_phasing_cell_b", Float),
    Column("v_datacollection_summary_phasing_cell_c", Float),
    Column("v_datacollection_summary_phasing_cell_alpha", Float),
    Column("v_datacollection_summary_phasing_cell_beta", Float),
    Column("v_datacollection_summary_phasing_cell_gamma", Float),
    Column(
        "v_datacollection_summary_phasing_anomalous",
        TINYINT(1),
        server_default=text("'0'"),
    ),
    Column("v_datacollection_summary_phasing_autoproc_space_group", String(45)),
    Column(
        "v_datacollection_summary_phasing_autoproc_autoprocId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "v_datacollection_summary_phasing_autoProcScalingId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("v_datacollection_summary_phasing_processingPrograms", String(255)),
    Column(
        "v_datacollection_summary_phasing_autoProcProgramId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "v_datacollection_summary_phasing_processingStatus",
        Enum("RUNNING", "FAILED", "SUCCESS", "0", "1"),
    ),
    Column(
        "v_datacollection_summary_session_sessionId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column(
        "v_datacollection_summary_session_proposalId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
)


t_v_datacollection_summary_screening = Table(
    "v_datacollection_summary_screening",
    metadata,
    Column("Screening_screeningId", INTEGER(10), server_default=text("'0'")),
    Column("Screening_dataCollectionId", INTEGER(10)),
    Column("Screening_dataCollectionGroupId", INTEGER(11)),
    Column("ScreeningOutput_strategySuccess", TINYINT(1), server_default=text("'0'")),
    Column("ScreeningOutput_indexingSuccess", TINYINT(1), server_default=text("'0'")),
    Column("ScreeningOutput_rankingResolution", Float(asdecimal=True)),
    Column(
        "ScreeningOutput_mosaicityEstimated", TINYINT(1), server_default=text("'0'")
    ),
    Column("ScreeningOutput_mosaicity", Float),
    Column("ScreeningOutput_totalExposureTime", Float(asdecimal=True)),
    Column("ScreeningOutput_totalRotationRange", Float(asdecimal=True)),
    Column("ScreeningOutput_totalNumberOfImages", INTEGER(11)),
    Column("ScreeningOutputLattice_spaceGroup", String(45)),
    Column("ScreeningOutputLattice_unitCell_a", Float),
    Column("ScreeningOutputLattice_unitCell_b", Float),
    Column("ScreeningOutputLattice_unitCell_c", Float),
    Column("ScreeningOutputLattice_unitCell_alpha", Float),
    Column("ScreeningOutputLattice_unitCell_beta", Float),
    Column("ScreeningOutputLattice_unitCell_gamma", Float),
    Column("ScreeningStrategySubWedge_exposureTime", Float),
    Column("ScreeningStrategySubWedge_transmission", Float),
    Column("ScreeningStrategySubWedge_oscillationRange", Float),
    Column("ScreeningStrategySubWedge_numberOfImages", INTEGER(10)),
    Column("ScreeningStrategySubWedge_multiplicity", Float),
    Column("ScreeningStrategySubWedge_completeness", Float),
    Column("ScreeningStrategySubWedge_axisStart", Float),
    Column("ScreeningStrategySubWedge_axisEnd", Float),
    Column("ScreeningStrategySubWedge_rotationAxis", String(45)),
)


t_v_dewar = Table(
    "v_dewar",
    metadata,
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("shippingId", INTEGER(10), server_default=text("'0'")),
    Column("shippingName", String(45)),
    Column("dewarId", INTEGER(10), server_default=text("'0'")),
    Column("dewarName", String(45)),
    Column("dewarStatus", String(45)),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("creationDate", DateTime),
    Column("shippingType", String(45)),
    Column("barCode", String(45)),
    Column("shippingStatus", String(45)),
    Column("beamLineName", String(45)),
    Column("nbEvents", BIGINT(21), server_default=text("'0'")),
    Column("storesin", BIGINT(21), server_default=text("'0'")),
    Column("nbSamples", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarBeamline = Table(
    "v_dewarBeamline",
    metadata,
    Column("beamLineName", String(45)),
    Column("COUNT(*)", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarBeamlineByWeek = Table(
    "v_dewarBeamlineByWeek",
    metadata,
    Column("Week", String(23)),
    Column("ID14", BIGINT(21), server_default=text("'0'")),
    Column("ID23", BIGINT(21), server_default=text("'0'")),
    Column("ID29", BIGINT(21), server_default=text("'0'")),
    Column("BM14", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarByWeek = Table(
    "v_dewarByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Dewars Tracked", BIGINT(21), server_default=text("'0'")),
    Column("Dewars Non-Tracked", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarByWeekTotal = Table(
    "v_dewarByWeekTotal",
    metadata,
    Column("Week", String(23)),
    Column("Dewars Tracked", BIGINT(21), server_default=text("'0'")),
    Column("Dewars Non-Tracked", BIGINT(21), server_default=text("'0'")),
    Column("Total", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarList = Table(
    "v_dewarList",
    metadata,
    Column("proposal", String(90)),
    Column("shippingName", String(45)),
    Column("dewarName", String(45)),
    Column("barCode", String(45)),
    Column("creationDate", String(10)),
    Column("shippingType", String(45)),
    Column("nbEvents", BIGINT(21), server_default=text("'0'")),
    Column("dewarStatus", String(45)),
    Column("shippingStatus", String(45)),
    Column("nbSamples", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarProposalCode = Table(
    "v_dewarProposalCode",
    metadata,
    Column("proposalCode", String(45)),
    Column("COUNT(*)", BIGINT(21), server_default=text("'0'")),
)


t_v_dewarProposalCodeByWeek = Table(
    "v_dewarProposalCodeByWeek",
    metadata,
    Column("Week", String(23)),
    Column("MX", BIGINT(21), server_default=text("'0'")),
    Column("FX", BIGINT(21), server_default=text("'0'")),
    Column("BM14U", BIGINT(21), server_default=text("'0'")),
    Column("BM161", BIGINT(21), server_default=text("'0'")),
    Column("BM162", BIGINT(21), server_default=text("'0'")),
    Column("Others", BIGINT(21), server_default=text("'0'")),
)


t_v_dewar_summary = Table(
    "v_dewar_summary",
    metadata,
    Column("shippingName", String(45)),
    Column("deliveryAgent_agentName", String(45)),
    Column("deliveryAgent_shippingDate", Date),
    Column("deliveryAgent_deliveryDate", Date),
    Column("deliveryAgent_agentCode", String(45)),
    Column("deliveryAgent_flightCode", String(45)),
    Column("shippingStatus", String(45)),
    Column("bltimeStamp", DateTime),
    Column("laboratoryId", INTEGER(10)),
    Column("isStorageShipping", TINYINT(1), server_default=text("'0'")),
    Column("creationDate", DateTime),
    Column("Shipping_comments", String(255)),
    Column("sendingLabContactId", INTEGER(10)),
    Column("returnLabContactId", INTEGER(10)),
    Column("returnCourier", String(45)),
    Column("dateOfShippingToUser", DateTime),
    Column("shippingType", String(45)),
    Column("dewarId", INTEGER(10), server_default=text("'0'")),
    Column("shippingId", INTEGER(10)),
    Column("dewarCode", String(45)),
    Column("comments", TINYTEXT),
    Column("storageLocation", String(45)),
    Column("dewarStatus", String(45)),
    Column("isStorageDewar", TINYINT(1), server_default=text("'0'")),
    Column("barCode", String(45)),
    Column("firstExperimentId", INTEGER(10)),
    Column("customsValue", INTEGER(10)),
    Column("transportValue", INTEGER(10)),
    Column("trackingNumberToSynchrotron", String(30)),
    Column("trackingNumberFromSynchrotron", String(30)),
    Column("type", Enum("Dewar", "Toolbox"), server_default=text("'Dewar'")),
    Column("isReimbursed", TINYINT(1), server_default=text("'0'")),
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("beamlineName", String(45)),
    Column("sessionStartDate", DateTime),
    Column("sessionEndDate", DateTime),
    Column("beamLineOperator", String(255)),
    Column("nbReimbDewars", INTEGER(11)),
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("containerId", INTEGER(10), server_default=text("'0'")),
    Column("containerType", String(20)),
    Column("capacity", INTEGER(10)),
    Column("beamlineLocation", String(20)),
    Column("sampleChangerLocation", String(20)),
    Column("containerStatus", String(45)),
    Column("containerCode", String(45)),
)


t_v_em_2dclassification = Table(
    "v_em_2dclassification",
    metadata,
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("imageDirectory", String(255)),
    Column("particlePickerId", INTEGER(10), server_default=text("'0'")),
    Column("particleClassificationGroupId", INTEGER(10), server_default=text("'0'")),
    Column("particleClassificationId", INTEGER(10), server_default=text("'0'")),
    Column("classNumber", INTEGER(10)),
    Column("classImageFullPath", String(255)),
)


t_v_em_classification = Table(
    "v_em_classification",
    metadata,
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("imageDirectory", String(255)),
    Column("particlePickerId", INTEGER(10), server_default=text("'0'")),
    Column("numberOfParticles", INTEGER(10)),
    Column("particleClassificationGroupId", INTEGER(10), server_default=text("'0'")),
    Column("particleClassificationId", INTEGER(10), server_default=text("'0'")),
    Column("classNumber", INTEGER(10)),
    Column("classImageFullPath", String(255)),
    Column("particlesPerClass", INTEGER(10)),
    Column("classDistribution", Float),
    Column("rotationAccuracy", Float),
    Column("translationAccuracy", Float),
    Column("estimatedResolution", Float),
    Column("overallFourierCompleteness", Float),
)


t_v_em_movie = Table(
    "v_em_movie",
    metadata,
    Column("Movie_movieId", INTEGER(11), server_default=text("'0'")),
    Column("Movie_dataCollectionId", INTEGER(10)),
    Column("Movie_movieNumber", INTEGER(11)),
    Column("Movie_movieFullPath", String(255)),
    Column("Movie_positionX", String(45)),
    Column("Movie_positionY", String(45)),
    Column("Movie_micrographFullPath", String(255)),
    Column("Movie_micrographSnapshotFullPath", String(255)),
    Column("Movie_xmlMetaDataFullPath", String(255)),
    Column("Movie_dosePerImage", String(45)),
    Column(
        "Movie_createdTimeStamp",
        TIMESTAMP,
        server_default=text("'current_timestamp()'"),
    ),
    Column(
        "MotionCorrection_motionCorrectionId", INTEGER(11), server_default=text("'0'")
    ),
    Column("MotionCorrection_movieId", INTEGER(11)),
    Column("MotionCorrection_firstFrame", String(45)),
    Column("MotionCorrection_lastFrame", String(45)),
    Column("MotionCorrection_dosePerFrame", String(45)),
    Column("MotionCorrection_doseWeight", String(45)),
    Column("MotionCorrection_totalMotion", String(45)),
    Column("MotionCorrection_averageMotionPerFrame", String(45)),
    Column("MotionCorrection_driftPlotFullPath", String(512)),
    Column("MotionCorrection_micrographFullPath", String(512)),
    Column("MotionCorrection_micrographSnapshotFullPath", String(512)),
    Column("MotionCorrection_correctedDoseMicrographFullPath", String(512)),
    Column("MotionCorrection_patchesUsed", String(45)),
    Column("MotionCorrection_logFileFullPath", String(512)),
    Column("CTF_CTFid", INTEGER(11), server_default=text("'0'")),
    Column("CTF_motionCorrectionId", INTEGER(11)),
    Column("CTF_spectraImageThumbnailFullPath", String(512)),
    Column("CTF_spectraImageFullPath", String(512)),
    Column("CTF_defocusU", String(45)),
    Column("CTF_defocusV", String(45)),
    Column("CTF_angle", String(45)),
    Column("CTF_crossCorrelationCoefficient", String(45)),
    Column("CTF_resolutionLimit", String(45)),
    Column("CTF_estimatedBfactor", String(45)),
    Column("CTF_logFilePath", String(512)),
    Column(
        "CTF_createdTimeStamp", TIMESTAMP, server_default=text("'current_timestamp()'")
    ),
    Column("Proposal_proposalId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_sessionId", INTEGER(10), server_default=text("'0'")),
)


t_v_em_stats = Table(
    "v_em_stats",
    metadata,
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("imageDirectory", String(255)),
    Column("movieId", INTEGER(11), server_default=text("'0'")),
    Column("movieNumber", INTEGER(11)),
    Column("createdTimeStamp", TIMESTAMP, server_default=text("'current_timestamp()'")),
    Column("motionCorrectionId", INTEGER(11), server_default=text("'0'")),
    Column("dataCollectionId", INTEGER(10), server_default=text("'0'")),
    Column("totalMotion", String(45)),
    Column("averageMotionPerFrame", String(45)),
    Column("lastFrame", String(45)),
    Column("dosePerFrame", String(45)),
    Column("defocusU", String(45)),
    Column("defocusV", String(45)),
    Column("resolutionLimit", String(45)),
    Column("estimatedBfactor", String(45)),
    Column("angle", String(45)),
)


t_v_energyScan = Table(
    "v_energyScan",
    metadata,
    Column("energyScanId", INTEGER(10), server_default=text("'0'")),
    Column("sessionId", INTEGER(10)),
    Column("blSampleId", INTEGER(10)),
    Column("fluorescenceDetector", String(255)),
    Column("scanFileFullPath", String(255)),
    Column("choochFileFullPath", String(255)),
    Column("jpegChoochFileFullPath", String(255)),
    Column("element", String(45)),
    Column("startEnergy", Float),
    Column("endEnergy", Float),
    Column("transmissionFactor", Float),
    Column("exposureTime", Float),
    Column("synchrotronCurrent", Float),
    Column("temperature", Float),
    Column("peakEnergy", Float),
    Column("peakFPrime", Float),
    Column("peakFDoublePrime", Float),
    Column("inflectionEnergy", Float),
    Column("inflectionFPrime", Float),
    Column("inflectionFDoublePrime", Float),
    Column("xrayDose", Float),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("edgeEnergy", String(255)),
    Column("filename", String(255)),
    Column("beamSizeVertical", Float),
    Column("beamSizeHorizontal", Float),
    Column("crystalClass", String(20)),
    Column("comments", String(1024)),
    Column("flux", Float(asdecimal=True)),
    Column("flux_end", Float(asdecimal=True)),
    Column("remoteEnergy", Float),
    Column("remoteFPrime", Float),
    Column("remoteFDoublePrime", Float),
    Column("BLSample_sampleId", INTEGER(10), server_default=text("'0'")),
    Column("name", String(100)),
    Column("code", String(45)),
    Column("acronym", String(45)),
    Column("BLSession_proposalId", INTEGER(10), server_default=text("'0'")),
)


t_v_hour = Table("v_hour", metadata, Column("num", String(18)))


t_v_logonByHour = Table(
    "v_logonByHour",
    metadata,
    Column("Hour", String(7)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByMonthDay = Table(
    "v_logonByMonthDay",
    metadata,
    Column("Day", String(5)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByWeek = Table(
    "v_logonByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_logonByWeekDay = Table(
    "v_logonByWeekDay",
    metadata,
    Column("Day", String(64)),
    Column("Distinct logins", BIGINT(21), server_default=text("'0'")),
    Column("Total logins", BIGINT(22), server_default=text("'0'")),
)


t_v_monthDay = Table("v_monthDay", metadata, Column("num", String(10)))


t_v_mx_autoprocessing_stats = Table(
    "v_mx_autoprocessing_stats",
    metadata,
    Column("autoProcScalingStatisticsId", INTEGER(10), server_default=text("'0'")),
    Column("autoProcScalingId", INTEGER(10)),
    Column(
        "scalingStatisticsType",
        Enum("overall", "innerShell", "outerShell"),
        server_default=text("'overall'"),
    ),
    Column("resolutionLimitLow", Float),
    Column("resolutionLimitHigh", Float),
    Column("rMerge", Float),
    Column("rMeasWithinIPlusIMinus", Float),
    Column("rMeasAllIPlusIMinus", Float),
    Column("rPimWithinIPlusIMinus", Float),
    Column("rPimAllIPlusIMinus", Float),
    Column("fractionalPartialBias", Float),
    Column("nTotalObservations", INTEGER(11)),
    Column("nTotalUniqueObservations", INTEGER(11)),
    Column("meanIOverSigI", Float),
    Column("completeness", Float),
    Column("multiplicity", Float),
    Column("anomalousCompleteness", Float),
    Column("anomalousMultiplicity", Float),
    Column("recordTimeStamp", DateTime),
    Column("anomalous", TINYINT(1), server_default=text("'0'")),
    Column("ccHalf", Float),
    Column("ccAno", Float),
    Column("sigAno", String(45)),
    Column("ISA", String(45)),
    Column("dataCollectionId", INTEGER(10), server_default=text("'0'")),
    Column("strategySubWedgeOrigId", INTEGER(10)),
    Column("detectorId", INTEGER(11)),
    Column("blSubSampleId", INTEGER(10)),
    Column("dataCollectionNumber", INTEGER(10)),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("beamLineName", String(45)),
)


t_v_mx_experiment_stats = Table(
    "v_mx_experiment_stats",
    metadata,
    Column("startTime", DateTime),
    Column("Images", INTEGER(10)),
    Column("Transmission", Float),
    Column("Res. (corner)", Float),
    Column("En. (Wave.)", Float),
    Column("Omega start (total)", Float),
    Column("Exposure Time", Float),
    Column("Flux", Float(asdecimal=True)),
    Column("Flux End", Float(asdecimal=True)),
    Column("Detector Distance", Float),
    Column("X Beam", Float),
    Column("Y Beam", Float),
    Column("Kappa", Float),
    Column("Phi", Float),
    Column("Axis Start", Float),
    Column("Axis End", Float),
    Column("Axis Range", Float),
    Column("Beam Size X", Float),
    Column("Beam Size Y", Float),
    Column("beamLineName", String(45)),
    Column("comments", String(1024)),
    Column("proposalNumber", String(45)),
)


t_v_mx_sample = Table(
    "v_mx_sample",
    metadata,
    Column("BLSample_blSampleId", INTEGER(10), server_default=text("'0'")),
    Column("BLSample_diffractionPlanId", INTEGER(10)),
    Column("BLSample_crystalId", INTEGER(10)),
    Column("BLSample_containerId", INTEGER(10)),
    Column("BLSample_name", String(100)),
    Column("BLSample_code", String(45)),
    Column("BLSample_location", String(45)),
    Column("BLSample_holderLength", Float(asdecimal=True)),
    Column("BLSample_loopLength", Float(asdecimal=True)),
    Column("BLSample_loopType", String(45)),
    Column("BLSample_wireWidth", Float(asdecimal=True)),
    Column("BLSample_comments", String(1024)),
    Column("BLSample_completionStage", String(45)),
    Column("BLSample_structureStage", String(45)),
    Column("BLSample_publicationStage", String(45)),
    Column("BLSample_publicationComments", String(255)),
    Column("BLSample_blSampleStatus", String(20)),
    Column("BLSample_isInSampleChanger", TINYINT(1)),
    Column("BLSample_lastKnownCenteringPosition", String(255)),
    Column(
        "BLSample_recordTimeStamp",
        TIMESTAMP,
        server_default=text("'current_timestamp()'"),
    ),
    Column("BLSample_SMILES", String(400)),
    Column("Protein_proteinId", INTEGER(10), server_default=text("'0'")),
    Column("Protein_name", String(255)),
    Column("Protein_acronym", String(45)),
    Column("Protein_proteinType", String(45)),
    Column("Protein_proposalId", INTEGER(10), server_default=text("'0'")),
    Column("Person_personId", INTEGER(10), server_default=text("'0'")),
    Column("Person_familyName", String(100)),
    Column("Person_givenName", String(45)),
    Column("Person_emailAddress", String(60)),
    Column("Container_containerId", INTEGER(10), server_default=text("'0'")),
    Column("Container_code", String(45)),
    Column("Container_containerType", String(20)),
    Column("Container_containerStatus", String(45)),
    Column("Container_beamlineLocation", String(20)),
    Column("Container_sampleChangerLocation", String(20)),
    Column("Dewar_code", String(45)),
    Column("Dewar_dewarId", INTEGER(10), server_default=text("'0'")),
    Column("Dewar_storageLocation", String(45)),
    Column("Dewar_dewarStatus", String(45)),
    Column("Dewar_barCode", String(45)),
    Column("Shipping_shippingId", INTEGER(10), server_default=text("'0'")),
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_startDate", DateTime),
    Column("BLSession_beamLineName", String(45)),
)


t_v_phasing = Table(
    "v_phasing",
    metadata,
    Column("BLSample_blSampleId", INTEGER(10), server_default=text("'0'")),
    Column(
        "AutoProcIntegration_autoProcIntegrationId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("AutoProcIntegration_dataCollectionId", INTEGER(10)),
    Column("AutoProcIntegration_autoProcProgramId", INTEGER(10)),
    Column("AutoProcIntegration_startImageNumber", INTEGER(10)),
    Column("AutoProcIntegration_endImageNumber", INTEGER(10)),
    Column("AutoProcIntegration_refinedDetectorDistance", Float),
    Column("AutoProcIntegration_refinedXBeam", Float),
    Column("AutoProcIntegration_refinedYBeam", Float),
    Column("AutoProcIntegration_rotationAxisX", Float),
    Column("AutoProcIntegration_rotationAxisY", Float),
    Column("AutoProcIntegration_rotationAxisZ", Float),
    Column("AutoProcIntegration_beamVectorX", Float),
    Column("AutoProcIntegration_beamVectorY", Float),
    Column("AutoProcIntegration_beamVectorZ", Float),
    Column("AutoProcIntegration_cell_a", Float),
    Column("AutoProcIntegration_cell_b", Float),
    Column("AutoProcIntegration_cell_c", Float),
    Column("AutoProcIntegration_cell_alpha", Float),
    Column("AutoProcIntegration_cell_beta", Float),
    Column("AutoProcIntegration_cell_gamma", Float),
    Column("AutoProcIntegration_recordTimeStamp", DateTime),
    Column("AutoProcIntegration_anomalous", TINYINT(1), server_default=text("'0'")),
    Column("SpaceGroup_spaceGroupId", INTEGER(10), server_default=text("'0'")),
    Column("SpaceGroup_geometryClassnameId", INTEGER(10)),
    Column("SpaceGroup_spaceGroupNumber", INTEGER(10)),
    Column("SpaceGroup_spaceGroupShortName", String(45)),
    Column("SpaceGroup_spaceGroupName", String(45)),
    Column("SpaceGroup_bravaisLattice", String(45)),
    Column("SpaceGroup_bravaisLatticeName", String(45)),
    Column("SpaceGroup_pointGroup", String(45)),
    Column("SpaceGroup_MX_used", TINYINT(1), server_default=text("'0'")),
    Column("PhasingStep_phasingStepId", INTEGER(10), server_default=text("'0'")),
    Column("PhasingStep_previousPhasingStepId", INTEGER(10)),
    Column("PhasingStep_programRunId", INTEGER(10)),
    Column("PhasingStep_spaceGroupId", INTEGER(10)),
    Column("PhasingStep_autoProcScalingId", INTEGER(10)),
    Column("PhasingStep_phasingAnalysisId", INTEGER(10)),
    Column(
        "PhasingStep_phasingStepType",
        Enum(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        ),
    ),
    Column("PhasingStep_method", String(45)),
    Column("PhasingStep_solventContent", String(45)),
    Column("PhasingStep_enantiomorph", String(45)),
    Column("PhasingStep_lowRes", String(45)),
    Column("PhasingStep_highRes", String(45)),
    Column(
        "PhasingStep_recordTimeStamp",
        TIMESTAMP,
        server_default=text("'current_timestamp()'"),
    ),
    Column("DataCollection_dataCollectionId", INTEGER(10), server_default=text("'0'")),
    Column("DataCollection_dataCollectionGroupId", INTEGER(11)),
    Column("DataCollection_strategySubWedgeOrigId", INTEGER(10)),
    Column("DataCollection_detectorId", INTEGER(11)),
    Column("DataCollection_blSubSampleId", INTEGER(10)),
    Column("DataCollection_dataCollectionNumber", INTEGER(10)),
    Column("DataCollection_startTime", DateTime),
    Column("DataCollection_endTime", DateTime),
    Column("DataCollection_runStatus", String(45)),
    Column("DataCollection_axisStart", Float),
    Column("DataCollection_axisEnd", Float),
    Column("DataCollection_axisRange", Float),
    Column("DataCollection_overlap", Float),
    Column("DataCollection_numberOfImages", INTEGER(10)),
    Column("DataCollection_startImageNumber", INTEGER(10)),
    Column("DataCollection_numberOfPasses", INTEGER(10)),
    Column("DataCollection_exposureTime", Float),
    Column("DataCollection_imageDirectory", String(255)),
    Column("DataCollection_imagePrefix", String(100)),
    Column("DataCollection_imageSuffix", String(45)),
    Column("DataCollection_fileTemplate", String(255)),
    Column("DataCollection_wavelength", Float),
    Column("DataCollection_resolution", Float),
    Column("DataCollection_detectorDistance", Float),
    Column("DataCollection_xBeam", Float),
    Column("DataCollection_yBeam", Float),
    Column("DataCollection_xBeamPix", Float),
    Column("DataCollection_yBeamPix", Float),
    Column("DataCollection_comments", String(1024)),
    Column("DataCollection_printableForReport", TINYINT(3), server_default=text("'1'")),
    Column("DataCollection_slitGapVertical", Float),
    Column("DataCollection_slitGapHorizontal", Float),
    Column("DataCollection_transmission", Float),
    Column("DataCollection_synchrotronMode", String(20)),
    Column("DataCollection_xtalSnapshotFullPath1", String(255)),
    Column("DataCollection_xtalSnapshotFullPath2", String(255)),
    Column("DataCollection_xtalSnapshotFullPath3", String(255)),
    Column("DataCollection_xtalSnapshotFullPath4", String(255)),
    Column("DataCollection_rotationAxis", Enum("Omega", "Kappa", "Phi")),
    Column("DataCollection_phiStart", Float),
    Column("DataCollection_kappaStart", Float),
    Column("DataCollection_omegaStart", Float),
    Column("DataCollection_resolutionAtCorner", Float),
    Column("DataCollection_detector2Theta", Float),
    Column("DataCollection_undulatorGap1", Float),
    Column("DataCollection_undulatorGap2", Float),
    Column("DataCollection_undulatorGap3", Float),
    Column("DataCollection_beamSizeAtSampleX", Float),
    Column("DataCollection_beamSizeAtSampleY", Float),
    Column("DataCollection_centeringMethod", String(255)),
    Column("DataCollection_averageTemperature", Float),
    Column("DataCollection_actualCenteringPosition", String(255)),
    Column("DataCollection_beamShape", String(45)),
    Column("DataCollection_flux", Float(asdecimal=True)),
    Column("DataCollection_flux_end", Float(asdecimal=True)),
    Column("DataCollection_totalAbsorbedDose", Float(asdecimal=True)),
    Column("DataCollection_bestWilsonPlotPath", String(255)),
    Column("DataCollection_imageQualityIndicatorsPlotPath", String(512)),
    Column("DataCollection_imageQualityIndicatorsCSVPath", String(512)),
    Column(
        "PhasingProgramRun_phasingProgramRunId", INTEGER(10), server_default=text("'0'")
    ),
    Column("PhasingProgramRun_phasingCommandLine", String(255)),
    Column("PhasingProgramRun_phasingPrograms", String(255)),
    Column("PhasingProgramRun_phasingStatus", TINYINT(1)),
    Column("PhasingProgramRun_phasingMessage", String(255)),
    Column("PhasingProgramRun_phasingStartTime", DateTime),
    Column("PhasingProgramRun_phasingEndTime", DateTime),
    Column("PhasingProgramRun_phasingEnvironment", String(255)),
    Column("PhasingProgramRun_phasingDirectory", String(255)),
    Column(
        "PhasingProgramRun_recordTimeStamp",
        TIMESTAMP,
        server_default=text("'current_timestamp()'"),
    ),
    Column("Protein_proteinId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_sessionId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_proposalId", INTEGER(10), server_default=text("'0'")),
    Column(
        "PhasingStatistics_phasingStatisticsId", INTEGER(10), server_default=text("'0'")
    ),
    Column(
        "PhasingStatistics_metric",
        Enum(
            "Rcullis",
            "Average Fragment Length",
            "Chain Count",
            "Residues Count",
            "CC",
            "PhasingPower",
            "FOM",
            '<d"/sig>',
            "Best CC",
            "CC(1/2)",
            "Weak CC",
            "CFOM",
            "Pseudo_free_CC",
            "CC of partial model",
            "Start R-work",
            "Start R-free",
            "Final R-work",
            "Final R-free",
        ),
    ),
    Column("PhasingStatistics_statisticsValue", Float(asdecimal=True)),
)


t_v_sample = Table(
    "v_sample",
    metadata,
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("shippingId", INTEGER(10), server_default=text("'0'")),
    Column("dewarId", INTEGER(10), server_default=text("'0'")),
    Column("containerId", INTEGER(10), server_default=text("'0'")),
    Column("blSampleId", INTEGER(10), server_default=text("'0'")),
    Column("proposalCode", String(45)),
    Column("proposalNumber", String(45)),
    Column("creationDate", DateTime),
    Column("shippingType", String(45)),
    Column("barCode", String(45)),
    Column("shippingStatus", String(45)),
)


t_v_sampleByWeek = Table(
    "v_sampleByWeek",
    metadata,
    Column("Week", String(23)),
    Column("Samples", BIGINT(21)),
)


t_v_saxs_datacollection = Table(
    "v_saxs_datacollection",
    metadata,
    Column("Subtraction_subtractionId", INTEGER(11), server_default=text("'0'")),
    Column("MeasurementToDataCollection_dataCollectionId", INTEGER(11)),
    Column("MeasurementToDataCollection_dataCollectionOrder", INTEGER(11)),
    Column(
        "MeasurementToDataCollection_measurementToDataCollectionId",
        INTEGER(11),
        server_default=text("'0'"),
    ),
    Column("Specimen_specimenId", INTEGER(11), server_default=text("'0'")),
    Column("Measurement_code", String(100)),
    Column("Measurement_measurementId", INTEGER(11), server_default=text("'0'")),
    Column("Buffer_bufferId", INTEGER(11), server_default=text("'0'")),
    Column("Buffer_proposalId", INTEGER(11), server_default=text("'-1'")),
    Column("Buffer_safetyLevelId", INTEGER(11)),
    Column("Buffer_name", String(45)),
    Column("Buffer_acronym", String(45)),
    Column("Buffer_pH", String(45)),
    Column("Buffer_composition", String(45)),
    Column("Buffer_comments", String(512)),
    Column("Macromolecule_macromoleculeId", INTEGER(11), server_default=text("'0'")),
    Column("Macromolecule_proposalId", INTEGER(10)),
    Column("Macromolecule_safetyLevelId", INTEGER(11)),
    Column("Macromolecule_name", String(45)),
    Column("Macromolecule_acronym", String(45)),
    Column("Macromolecule_extintionCoefficient", String(45)),
    Column("Macromolecule_molecularMass", String(45)),
    Column("Macromolecule_sequence", String(1000)),
    Column("Macromolecule_contactsDescriptionFilePath", String(255)),
    Column("Macromolecule_symmetry", String(45)),
    Column("Macromolecule_comments", String(1024)),
    Column("Macromolecule_refractiveIndex", String(45)),
    Column("Macromolecule_solventViscosity", String(45)),
    Column("Macromolecule_creationDate", DateTime),
    Column("Specimen_experimentId", INTEGER(11)),
    Column("Specimen_bufferId", INTEGER(11)),
    Column("Specimen_samplePlatePositionId", INTEGER(11)),
    Column("Specimen_safetyLevelId", INTEGER(11)),
    Column("Specimen_stockSolutionId", INTEGER(11)),
    Column("Specimen_code", String(255)),
    Column("Specimen_concentration", String(45)),
    Column("Specimen_volume", String(45)),
    Column("Specimen_comments", String(5120)),
    Column(
        "SamplePlatePosition_samplePlatePositionId",
        INTEGER(11),
        server_default=text("'0'"),
    ),
    Column("SamplePlatePosition_samplePlateId", INTEGER(11)),
    Column("SamplePlatePosition_rowNumber", INTEGER(11)),
    Column("SamplePlatePosition_columnNumber", INTEGER(11)),
    Column("SamplePlatePosition_volume", String(45)),
    Column("samplePlateId", INTEGER(11), server_default=text("'0'")),
    Column("experimentId", INTEGER(11)),
    Column("plateGroupId", INTEGER(11)),
    Column("plateTypeId", INTEGER(11)),
    Column("instructionSetId", INTEGER(11)),
    Column("SamplePlate_boxId", INTEGER(10)),
    Column("SamplePlate_name", String(45)),
    Column("SamplePlate_slotPositionRow", String(45)),
    Column("SamplePlate_slotPositionColumn", String(45)),
    Column("SamplePlate_storageTemperature", String(45)),
    Column("Experiment_experimentId", INTEGER(11), server_default=text("'0'")),
    Column("Experiment_sessionId", INTEGER(10)),
    Column("Experiment_proposalId", INTEGER(11)),
    Column("Experiment_name", String(255)),
    Column("Experiment_creationDate", DateTime),
    Column("Experiment_experimentType", String(128)),
    Column("Experiment_sourceFilePath", String(256)),
    Column("Experiment_dataAcquisitionFilePath", String(256)),
    Column("Experiment_status", String(45)),
    Column("Experiment_comments", String(512)),
    Column("Measurement_priorityLevelId", INTEGER(11)),
    Column("Measurement_exposureTemperature", String(45)),
    Column("Measurement_viscosity", String(45)),
    Column("Measurement_flow", TINYINT(1)),
    Column("Measurement_extraFlowTime", String(45)),
    Column("Measurement_volumeToLoad", String(45)),
    Column("Measurement_waitTime", String(45)),
    Column("Measurement_transmission", String(45)),
    Column("Measurement_comments", String(512)),
    Column("Measurement_imageDirectory", String(512)),
    Column("Run_runId", INTEGER(11), server_default=text("'0'")),
    Column("Run_timePerFrame", String(45)),
    Column("Run_timeStart", String(45)),
    Column("Run_timeEnd", String(45)),
    Column("Run_storageTemperature", String(45)),
    Column("Run_exposureTemperature", String(45)),
    Column("Run_spectrophotometer", String(45)),
    Column("Run_energy", String(45)),
    Column("Run_creationDate", DateTime),
    Column("Run_frameAverage", String(45)),
    Column("Run_frameCount", String(45)),
    Column("Run_transmission", String(45)),
    Column("Run_beamCenterX", String(45)),
    Column("Run_beamCenterY", String(45)),
    Column("Run_pixelSizeX", String(45)),
    Column("Run_pixelSizeY", String(45)),
    Column("Run_radiationRelative", String(45)),
    Column("Run_radiationAbsolute", String(45)),
    Column("Run_normalization", String(45)),
    Column("Merge_mergeId", INTEGER(11), server_default=text("'0'")),
    Column("Merge_measurementId", INTEGER(11)),
    Column("Merge_frameListId", INTEGER(11)),
    Column("Merge_discardedFrameNameList", String(1024)),
    Column("Merge_averageFilePath", String(255)),
    Column("Merge_framesCount", String(45)),
    Column("Merge_framesMerge", String(45)),
    Column("Merge_creationDate", DateTime),
    Column("Subtraction_dataCollectionId", INTEGER(11)),
    Column("Subtraction_rg", String(45)),
    Column("Subtraction_rgStdev", String(45)),
    Column("Subtraction_I0", String(45)),
    Column("Subtraction_I0Stdev", String(45)),
    Column("Subtraction_firstPointUsed", String(45)),
    Column("Subtraction_lastPointUsed", String(45)),
    Column("Subtraction_quality", String(45)),
    Column("Subtraction_isagregated", String(45)),
    Column("Subtraction_concentration", String(45)),
    Column("Subtraction_gnomFilePath", String(255)),
    Column("Subtraction_rgGuinier", String(45)),
    Column("Subtraction_rgGnom", String(45)),
    Column("Subtraction_dmax", String(45)),
    Column("Subtraction_total", String(45)),
    Column("Subtraction_volume", String(45)),
    Column("Subtraction_creationTime", DateTime),
    Column("Subtraction_kratkyFilePath", String(255)),
    Column("Subtraction_scatteringFilePath", String(255)),
    Column("Subtraction_guinierFilePath", String(255)),
    Column("Subtraction_substractedFilePath", String(255)),
    Column("Subtraction_gnomFilePathOutput", String(255)),
    Column("Subtraction_sampleOneDimensionalFiles", INTEGER(11)),
    Column("Subtraction_bufferOnedimensionalFiles", INTEGER(11)),
    Column("Subtraction_sampleAverageFilePath", String(255)),
    Column("Subtraction_bufferAverageFilePath", String(255)),
)


t_v_session = Table(
    "v_session",
    metadata,
    Column("sessionId", INTEGER(10), server_default=text("'0'")),
    Column("expSessionPk", INTEGER(10)),
    Column("beamLineSetupId", INTEGER(10)),
    Column("proposalId", INTEGER(10), server_default=text("'0'")),
    Column("projectCode", String(45)),
    Column("BLSession_startDate", DateTime),
    Column("BLSession_endDate", DateTime),
    Column("beamLineName", String(45)),
    Column("scheduled", TINYINT(1)),
    Column("nbShifts", INTEGER(10)),
    Column("comments", String(2000)),
    Column("beamLineOperator", String(255)),
    Column("visit_number", INTEGER(10), server_default=text("'0'")),
    Column("bltimeStamp", TIMESTAMP, server_default=text("'current_timestamp()'")),
    Column("usedFlag", TINYINT(1)),
    Column("sessionTitle", String(255)),
    Column("structureDeterminations", Float),
    Column("dewarTransport", Float),
    Column("databackupFrance", Float),
    Column("databackupEurope", Float),
    Column("operatorSiteNumber", String(10)),
    Column(
        "BLSession_lastUpdate", TIMESTAMP, server_default=text("'0000-00-00 00:00:00'")
    ),
    Column("BLSession_protectedData", String(1024)),
    Column("Proposal_title", String(200)),
    Column("Proposal_proposalCode", String(45)),
    Column("Proposal_ProposalNumber", String(45)),
    Column("Proposal_ProposalType", String(2)),
    Column("Person_personId", INTEGER(10), server_default=text("'0'")),
    Column("Person_familyName", String(100)),
    Column("Person_givenName", String(45)),
    Column("Person_emailAddress", String(60)),
)


t_v_tracking_shipment_history = Table(
    "v_tracking_shipment_history",
    metadata,
    Column("Dewar_dewarId", INTEGER(10), server_default=text("'0'")),
    Column("Dewar_code", String(45)),
    Column("Dewar_comments", TINYTEXT),
    Column("Dewar_dewarStatus", String(45)),
    Column("Dewar_barCode", String(45)),
    Column("Dewar_firstExperimentId", INTEGER(10)),
    Column("Dewar_trackingNumberToSynchrotron", String(30)),
    Column("Dewar_trackingNumberFromSynchrotron", String(30)),
    Column("Dewar_type", Enum("Dewar", "Toolbox"), server_default=text("'Dewar'")),
    Column("Shipping_shippingId", INTEGER(10), server_default=text("'0'")),
    Column("Shipping_proposalId", INTEGER(10), server_default=text("'0'")),
    Column("Shipping_shippingName", String(45)),
    Column("deliveryAgent_agentName", String(45)),
    Column("Shipping_deliveryAgent_shippingDate", Date),
    Column("Shipping_deliveryAgent_deliveryDate", Date),
    Column("Shipping_shippingStatus", String(45)),
    Column("Shipping_returnCourier", String(45)),
    Column("Shipping_dateOfShippingToUser", DateTime),
    Column(
        "DewarTransportHistory_DewarTransportHistoryId",
        INTEGER(10),
        server_default=text("'0'"),
    ),
    Column("DewarTransportHistory_dewarStatus", String(45)),
    Column("DewarTransportHistory_storageLocation", String(45)),
    Column("DewarTransportHistory_arrivalDate", DateTime),
)


t_v_week = Table("v_week", metadata, Column("num", String(7)))


t_v_weekDay = Table("v_weekDay", metadata, Column("day", String(10)))


t_v_xfeFluorescenceSpectrum = Table(
    "v_xfeFluorescenceSpectrum",
    metadata,
    Column("xfeFluorescenceSpectrumId", INTEGER(10), server_default=text("'0'")),
    Column("sessionId", INTEGER(10)),
    Column("blSampleId", INTEGER(10)),
    Column("fittedDataFileFullPath", String(255)),
    Column("scanFileFullPath", String(255)),
    Column("jpegScanFileFullPath", String(255)),
    Column("startTime", DateTime),
    Column("endTime", DateTime),
    Column("filename", String(255)),
    Column("energy", Float),
    Column("exposureTime", Float),
    Column("beamTransmission", Float),
    Column("annotatedPymcaXfeSpectrum", String(255)),
    Column("beamSizeVertical", Float),
    Column("beamSizeHorizontal", Float),
    Column("crystalClass", String(20)),
    Column("comments", String(1024)),
    Column("flux", Float(asdecimal=True)),
    Column("flux_end", Float(asdecimal=True)),
    Column("workingDirectory", String(512)),
    Column("BLSample_sampleId", INTEGER(10), server_default=text("'0'")),
    Column("BLSession_proposalId", INTEGER(10), server_default=text("'0'")),
)


class AbInitioModel(Base):
    __tablename__ = "AbInitioModel"

    abInitioModelId = Column(INTEGER(11), primary_key=True)
    modelListId = Column(
        ForeignKey("ModelList.modelListId", ondelete="CASCADE"), index=True
    )
    averagedModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), index=True
    )
    rapidShapeDeterminationModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), index=True
    )
    shapeDeterminationModelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), index=True
    )
    comments = Column(String(512))
    creationTime = Column(DateTime)

    AveragedModel = relationship(
        "Model", primaryjoin="AbInitioModel.averagedModelId == Model.modelId"
    )
    ModelList = relationship("ModelList")
    RapidShapeDeterminationModel = relationship(
        "Model",
        primaryjoin="AbInitioModel.rapidShapeDeterminationModelId == Model.modelId",
    )
    ShapeDeterminationModel = relationship(
        "Model", primaryjoin="AbInitioModel.shapeDeterminationModelId == Model.modelId"
    )


class AutoProcScaling(Base):
    __tablename__ = "AutoProcScaling"
    __table_args__ = (Index("AutoProcScalingIdx1", "autoProcScalingId", "autoProcId"),)

    autoProcScalingId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcId = Column(
        ForeignKey("AutoProc.autoProcId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related autoProc item (used by foreign key)",
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    resolutionEllipsoidAxis11 = Column(
        Float, comment="Eigenvector for first diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis12 = Column(
        Float, comment="Eigenvector for first diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis13 = Column(
        Float, comment="Eigenvector for first diffraction limit, coord 3"
    )
    resolutionEllipsoidAxis21 = Column(
        Float, comment="Eigenvector for second diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis22 = Column(
        Float, comment="Eigenvector for second diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis23 = Column(
        Float, comment="Eigenvector for second diffraction limit, coord 3"
    )
    resolutionEllipsoidAxis31 = Column(
        Float, comment="Eigenvector for third diffraction limit, coord 1"
    )
    resolutionEllipsoidAxis32 = Column(
        Float, comment="Eigenvector for third diffraction limit, coord 2"
    )
    resolutionEllipsoidAxis33 = Column(
        Float, comment="Eigenvector for third diffraction limit, coord 3"
    )
    resolutionEllipsoidValue1 = Column(
        Float, comment="First (anisotropic) diffraction limit"
    )
    resolutionEllipsoidValue2 = Column(
        Float, comment="Second (anisotropic) diffraction limit"
    )
    resolutionEllipsoidValue3 = Column(
        Float, comment="Third (anisotropic) diffraction limit"
    )

    AutoProc = relationship("AutoProc")


class BFComponent(Base):
    __tablename__ = "BF_component"

    componentId = Column(INTEGER(10), primary_key=True)
    systemId = Column(ForeignKey("BF_system.systemId", ondelete="CASCADE"), index=True)
    name = Column(String(100))
    description = Column(String(200))

    BF_system = relationship("BFSystem")


class BFSystemBeamline(Base):
    __tablename__ = "BF_system_beamline"

    system_beamlineId = Column(INTEGER(10), primary_key=True)
    systemId = Column(ForeignKey("BF_system.systemId", ondelete="CASCADE"), index=True)
    beamlineName = Column(String(20))

    BF_system = relationship("BFSystem")


class BeamApertures(Base):
    __tablename__ = "BeamApertures"

    beamAperturesid = Column(INTEGER(10), primary_key=True)
    beamlineStatsId = Column(
        ForeignKey("BeamlineStats.beamlineStatsId", ondelete="CASCADE"), index=True
    )
    flux = Column(Float(asdecimal=True))
    x = Column(Float)
    y = Column(Float)
    apertureSize = Column(SMALLINT(5))

    BeamlineStats = relationship("BeamlineStats")


class BeamCentres(Base):
    __tablename__ = "BeamCentres"

    beamCentresid = Column(INTEGER(10), primary_key=True)
    beamlineStatsId = Column(
        ForeignKey("BeamlineStats.beamlineStatsId", ondelete="CASCADE"), index=True
    )
    x = Column(Float)
    y = Column(Float)
    zoom = Column(TINYINT(3))

    BeamlineStats = relationship("BeamlineStats")


class Buffer(Base):
    __tablename__ = "Buffer"

    bufferId = Column(INTEGER(11), primary_key=True)
    proposalId = Column(INTEGER(11), nullable=False, server_default=text("-1"))
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE"), index=True
    )
    name = Column(String(45))
    acronym = Column(String(45))
    pH = Column(String(45))
    composition = Column(String(45))
    comments = Column(String(512))
    BLSessionId = Column(INTEGER(10))
    electronDensity = Column(Float(7))

    SafetyLevel = relationship("SafetyLevel")


class DiffractionPlanHasDetector(Base):
    __tablename__ = "DiffractionPlan_has_Detector"

    diffractionPlanId = Column(
        ForeignKey("DiffractionPlan.diffractionPlanId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    detectorId = Column(
        ForeignKey("Detector.detectorId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    exposureTime = Column(Float(asdecimal=True))
    distance = Column(Float(asdecimal=True))
    orientation = Column(Float(asdecimal=True))

    Detector = relationship("Detector")
    DiffractionPlan = relationship("DiffractionPlan")


class ExperimentKindDetails(Base):
    __tablename__ = "ExperimentKindDetails"

    experimentKindId = Column(INTEGER(10), primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    exposureIndex = Column(INTEGER(10))
    dataCollectionType = Column(String(45))
    dataCollectionKind = Column(String(45))
    wedgeValue = Column(Float)

    DiffractionPlan = relationship("DiffractionPlan")


class FrameSet(Base):
    __tablename__ = "FrameSet"

    frameSetId = Column(INTEGER(11), primary_key=True)
    runId = Column(
        ForeignKey("Run.runId", ondelete="CASCADE"), nullable=False, index=True
    )
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    detectorId = Column(INTEGER(11))
    detectorDistance = Column(String(45))
    filePath = Column(String(255))
    internalPath = Column(String(255))

    FrameList = relationship("FrameList")
    Run = relationship("Run")


class FrameToList(Base):
    __tablename__ = "FrameToList"

    frameToListId = Column(INTEGER(11), primary_key=True)
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    frameId = Column(
        ForeignKey("Frame.frameId", ondelete="CASCADE"), nullable=False, index=True
    )

    Frame = relationship("Frame")
    FrameList = relationship("FrameList")


class Instruction(Base):
    __tablename__ = "Instruction"

    instructionId = Column(INTEGER(11), primary_key=True)
    instructionSetId = Column(
        ForeignKey("InstructionSet.instructionSetId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    order = Column(INTEGER(11), nullable=False)
    comments = Column(String(255))

    InstructionSet = relationship("InstructionSet")


class Macromolecule(Base):
    __tablename__ = "Macromolecule"

    macromoleculeId = Column(INTEGER(11), primary_key=True)
    proposalId = Column(INTEGER(10))
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE"), index=True
    )
    name = Column(VARCHAR(45))
    acronym = Column(VARCHAR(45))
    extintionCoefficient = Column(String(45))
    molecularMass = Column(String(45))
    sequence = Column(String(1000))
    contactsDescriptionFilePath = Column(String(255))
    symmetry = Column(String(45))
    comments = Column(VARCHAR(1024))
    refractiveIndex = Column(String(45))
    solventViscosity = Column(String(45))
    creationDate = Column(DateTime)
    electronDensity = Column(Float(7))

    SafetyLevel = relationship("SafetyLevel")


class ModelToList(Base):
    __tablename__ = "ModelToList"

    modelToListId = Column(INTEGER(11), primary_key=True)
    modelId = Column(
        ForeignKey("Model.modelId", ondelete="CASCADE"), nullable=False, index=True
    )
    modelListId = Column(
        ForeignKey("ModelList.modelListId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    Model = relationship("Model")
    ModelList = relationship("ModelList")


class Person(Base):
    __tablename__ = "Person"

    personId = Column(INTEGER(10), primary_key=True)
    laboratoryId = Column(
        ForeignKey("Laboratory.laboratoryId", ondelete="CASCADE"), index=True
    )
    siteId = Column(INTEGER(11), index=True)
    personUUID = Column(String(45))
    familyName = Column(String(100), index=True)
    givenName = Column(String(45))
    title = Column(String(45))
    emailAddress = Column(String(60))
    phoneNumber = Column(VARCHAR(45))
    login = Column(String(45), index=True)
    passwd = Column(String(45))
    faxNumber = Column(String(45))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    externalId = Column(BINARY(16))
    cache = Column(Text)

    Laboratory = relationship("Laboratory")
    Project = relationship("Project", secondary="Project_has_Person")
    UserGroup = relationship("UserGroup", secondary="UserGroup_has_Person")


class PhasingProgramAttachment(Base):
    __tablename__ = "PhasingProgramAttachment"

    phasingProgramAttachmentId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    fileType = Column(
        Enum(
            "DSIGMA_RESOLUTION",
            "OCCUPANCY_SITENUMBER",
            "CONTRAST_CYCLE",
            "CCALL_CCWEAK",
            "IMAGE",
            "Map",
            "Logfile",
            "PDB",
            "CSV",
            "INS",
            "RES",
            "TXT",
        ),
        comment="file type",
    )
    fileName = Column(String(45), comment="file name")
    filePath = Column(String(255), comment="file path")
    input = Column(TINYINT(1))
    recordTimeStamp = Column(
        TIMESTAMP,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    PhasingProgramRun = relationship("PhasingProgramRun")


class ScanParametersModel(Base):
    __tablename__ = "ScanParametersModel"

    scanParametersModelId = Column(INTEGER(10), primary_key=True)
    scanParametersServiceId = Column(
        ForeignKey(
            "ScanParametersService.scanParametersServiceId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    dataCollectionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    modelNumber = Column(TINYINT(3))
    start = Column(Float(asdecimal=True))
    stop = Column(Float(asdecimal=True))
    step = Column(Float(asdecimal=True))
    array = Column(Text)

    DiffractionPlan = relationship("DiffractionPlan")
    ScanParametersService = relationship("ScanParametersService")


class ScheduleComponent(Base):
    __tablename__ = "ScheduleComponent"

    scheduleComponentId = Column(INTEGER(10), primary_key=True)
    scheduleId = Column(
        ForeignKey("Schedule.scheduleId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    inspectionTypeId = Column(
        ForeignKey("InspectionType.inspectionTypeId", ondelete="CASCADE"), index=True
    )
    offset_hours = Column(INTEGER(11))

    InspectionType = relationship("InspectionType")
    Schedule = relationship("Schedule")


class SpaceGroup(Base):
    __tablename__ = "SpaceGroup"

    spaceGroupId = Column(INTEGER(10), primary_key=True, comment="Primary key")
    geometryClassnameId = Column(
        ForeignKey(
            "GeometryClassname.geometryClassnameId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    spaceGroupNumber = Column(INTEGER(10), comment="ccp4 number pr IUCR")
    spaceGroupShortName = Column(
        String(45), index=True, comment="short name without blank"
    )
    spaceGroupName = Column(String(45), comment="verbose name")
    bravaisLattice = Column(String(45), comment="short name")
    bravaisLatticeName = Column(String(45), comment="verbose name")
    pointGroup = Column(String(45), comment="point group")
    MX_used = Column(
        TINYINT(1),
        nullable=False,
        server_default=text("0"),
        comment="1 if used in the crystal form",
    )

    GeometryClassname = relationship("GeometryClassname")


class UntrustedRegion(Base):
    __tablename__ = "UntrustedRegion"
    __table_args__ = {"comment": "Untrsuted region linked to a detector"}

    untrustedRegionId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    detectorId = Column(
        ForeignKey("Detector.detectorId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    x1 = Column(INTEGER(11), nullable=False)
    x2 = Column(INTEGER(11), nullable=False)
    y1 = Column(INTEGER(11), nullable=False)
    y2 = Column(INTEGER(11), nullable=False)

    Detector = relationship("Detector")


t_UserGroup_has_Permission = Table(
    "UserGroup_has_Permission",
    metadata,
    Column(
        "userGroupId",
        ForeignKey("UserGroup.userGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "permissionId",
        ForeignKey("Permission.permissionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class WorkflowDehydration(Base):
    __tablename__ = "WorkflowDehydration"

    workflowDehydrationId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="Related workflow",
    )
    dataFilePath = Column(String(255))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    Workflow = relationship("Workflow")


class WorkflowStep(Base):
    __tablename__ = "WorkflowStep"

    workflowStepId = Column(INTEGER(11), primary_key=True)
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    workflowStepType = Column(String(45))
    status = Column(String(45))
    folderPath = Column(String(1024))
    imageResultFilePath = Column(String(1024))
    htmlResultFilePath = Column(String(1024))
    resultFilePath = Column(String(1024))
    comments = Column(String(2048))
    crystalSizeX = Column(String(45))
    crystalSizeY = Column(String(45))
    crystalSizeZ = Column(String(45))
    maxDozorScore = Column(String(45))
    recordTimeStamp = Column(TIMESTAMP)

    Workflow = relationship("Workflow")


class Assembly(Base):
    __tablename__ = "Assembly"

    assemblyId = Column(INTEGER(11), primary_key=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    creationDate = Column(DateTime)
    comments = Column(String(255))

    Macromolecule = relationship("Macromolecule")


class AutoProcScalingStatistics(Base):
    __tablename__ = "AutoProcScalingStatistics"

    autoProcScalingStatisticsId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="Related autoProcScaling item (used by foreign key)",
    )
    scalingStatisticsType = Column(
        Enum("overall", "innerShell", "outerShell"),
        nullable=False,
        index=True,
        server_default=text("'overall'"),
        comment="Scaling statistics type",
    )
    comments = Column(String(255), comment="Comments...")
    resolutionLimitLow = Column(Float, comment="Low resolution limit")
    resolutionLimitHigh = Column(Float, comment="High resolution limit")
    rMerge = Column(Float, comment="Rmerge")
    rMeasWithinIPlusIMinus = Column(Float, comment="Rmeas (within I+/I-)")
    rMeasAllIPlusIMinus = Column(Float, comment="Rmeas (all I+ & I-)")
    rPimWithinIPlusIMinus = Column(Float, comment="Rpim (within I+/I-) ")
    rPimAllIPlusIMinus = Column(Float, comment="Rpim (all I+ & I-)")
    fractionalPartialBias = Column(Float, comment="Fractional partial bias")
    nTotalObservations = Column(INTEGER(11), comment="Total number of observations")
    nTotalUniqueObservations = Column(INTEGER(11), comment="Total number unique")
    meanIOverSigI = Column(Float, comment="Mean((I)/sd(I))")
    completeness = Column(Float, comment="Completeness")
    multiplicity = Column(Float, comment="Multiplicity")
    anomalousCompleteness = Column(Float, comment="Anomalous completeness")
    anomalousMultiplicity = Column(Float, comment="Anomalous multiplicity")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    anomalous = Column(
        TINYINT(1), server_default=text("0"), comment="boolean type:0 noanoum - 1 anoum"
    )
    ccHalf = Column(Float, comment="information from XDS")
    ccAno = Column(Float)
    sigAno = Column(String(45))
    isa = Column(String(45))
    completenessSpherical = Column(
        Float, comment="Completeness calculated assuming isotropic diffraction"
    )
    completenessEllipsoidal = Column(
        Float, comment="Completeness calculated allowing for anisotropic diffraction"
    )
    anomalousCompletenessSpherical = Column(
        Float,
        comment="Anomalous completeness calculated assuming isotropic diffraction",
    )
    anomalousCompletenessEllipsoidal = Column(
        Float,
        comment="Anisotropic completeness calculated allowing for anisotropic diffraction",
    )

    AutoProcScaling = relationship("AutoProcScaling")


class BFComponentBeamline(Base):
    __tablename__ = "BF_component_beamline"

    component_beamlineId = Column(INTEGER(10), primary_key=True)
    componentId = Column(
        ForeignKey("BF_component.componentId", ondelete="CASCADE"), index=True
    )
    beamlinename = Column(String(20))

    BF_component = relationship("BFComponent")


class BFSubcomponent(Base):
    __tablename__ = "BF_subcomponent"

    subcomponentId = Column(INTEGER(10), primary_key=True)
    componentId = Column(
        ForeignKey("BF_component.componentId", ondelete="CASCADE"), index=True
    )
    name = Column(String(100))
    description = Column(String(200))

    BF_component = relationship("BFComponent")


class BufferHasAdditive(Base):
    __tablename__ = "BufferHasAdditive"

    bufferHasAdditiveId = Column(INTEGER(11), primary_key=True)
    bufferId = Column(
        ForeignKey("Buffer.bufferId", ondelete="CASCADE"), nullable=False, index=True
    )
    additiveId = Column(
        ForeignKey("Additive.additiveId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    measurementUnitId = Column(
        ForeignKey("MeasurementUnit.measurementUnitId", ondelete="CASCADE"), index=True
    )
    quantity = Column(String(45))

    Additive = relationship("Additive")
    Buffer = relationship("Buffer")
    MeasurementUnit = relationship("MeasurementUnit")


class MXMRRun(Base):
    __tablename__ = "MXMRRun"

    mxMRRunId = Column(INTEGER(10), primary_key=True)
    autoProcScalingId = Column(
        ForeignKey("AutoProcScaling.autoProcScalingId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    success = Column(
        TINYINT(1),
        server_default=text("0"),
        comment="Indicates whether the program completed. 1 for success, 0 for failure.",
    )
    message = Column(
        String(255), comment="A short summary of the findings, success or failure."
    )
    pipeline = Column(String(50))
    inputCoordFile = Column(String(255))
    outputCoordFile = Column(String(255))
    inputMTZFile = Column(String(255))
    outputMTZFile = Column(String(255))
    runDirectory = Column(String(255))
    logFile = Column(String(255))
    commandLine = Column(String(255))
    rValueStart = Column(Float)
    rValueEnd = Column(Float)
    rFreeValueStart = Column(Float)
    rFreeValueEnd = Column(Float)
    starttime = Column(DateTime)
    endtime = Column(DateTime)

    AutoProcScaling = relationship("AutoProcScaling")


class MacromoleculeRegion(Base):
    __tablename__ = "MacromoleculeRegion"

    macromoleculeRegionId = Column(INTEGER(11), primary_key=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    regionType = Column(String(45))
    id = Column(String(45))
    count = Column(String(45))
    sequence = Column(String(45))

    Macromolecule = relationship("Macromolecule")


class ModelBuilding(Base):
    __tablename__ = "ModelBuilding"

    modelBuildingId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class Phasing(Base):
    __tablename__ = "Phasing"

    phasingId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    method = Column(
        Enum("solvent flattening", "solvent flipping"), comment="phasing method"
    )
    solventContent = Column(Float(asdecimal=True))
    enantiomorph = Column(TINYINT(1), comment="0 or 1")
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class PhasingStep(Base):
    __tablename__ = "PhasingStep"

    phasingStepId = Column(INTEGER(10), primary_key=True)
    previousPhasingStepId = Column(INTEGER(10))
    programRunId = Column(
        ForeignKey("PhasingProgramRun.phasingProgramRunId", ondelete="CASCADE"),
        index=True,
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE"), index=True
    )
    autoProcScalingId = Column(
        ForeignKey("AutoProcScaling.autoProcScalingId", ondelete="CASCADE"), index=True
    )
    phasingAnalysisId = Column(INTEGER(10), index=True)
    phasingStepType = Column(
        Enum(
            "PREPARE",
            "SUBSTRUCTUREDETERMINATION",
            "PHASING",
            "MODELBUILDING",
            "REFINEMENT",
            "LIGAND_FIT",
        )
    )
    method = Column(String(45))
    solventContent = Column(String(45))
    enantiomorph = Column(String(45))
    lowRes = Column(String(45))
    highRes = Column(String(45))
    groupName = Column(String(45))
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    AutoProcScaling = relationship("AutoProcScaling")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class PhasingHasScaling(Base):
    __tablename__ = "Phasing_has_Scaling"

    phasingHasScalingId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related autoProcScaling item",
    )
    datasetNumber = Column(
        INTEGER(11),
        comment="serial number of the dataset and always reserve 0 for the reference",
    )
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    AutoProcScaling = relationship("AutoProcScaling")
    PhasingAnalysis = relationship("PhasingAnalysis")


class PreparePhasingData(Base):
    __tablename__ = "PreparePhasingData"

    preparePhasingDataId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


class Project(Base):
    __tablename__ = "Project"

    projectId = Column(INTEGER(10), primary_key=True)
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    title = Column(String(200))
    acronym = Column(String(100))
    owner = Column(String(50))

    Person = relationship("Person")
    Protein = relationship("Protein", secondary="Project_has_Protein")
    BLSession = relationship("BLSession", secondary="Project_has_Session")
    Shipping = relationship("Shipping", secondary="Project_has_Shipping")
    XFEFluorescenceSpectrum = relationship(
        "XFEFluorescenceSpectrum", secondary="Project_has_XFEFSpectrum"
    )


class Proposal(Base):
    __tablename__ = "Proposal"
    __table_args__ = (
        Index("Proposal_FKIndexCodeNumber", "proposalCode", "proposalNumber"),
    )

    proposalId = Column(INTEGER(10), primary_key=True)
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    title = Column(VARCHAR(200))
    proposalCode = Column(String(45))
    proposalNumber = Column(String(45))
    proposalType = Column(String(2), comment="Proposal type: MX, BX")
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    externalId = Column(BINARY(16))
    state = Column(Enum("Open", "Closed", "Cancelled"), server_default=text("'Open'"))

    Person = relationship("Person")


class StockSolution(Base):
    __tablename__ = "StockSolution"

    stockSolutionId = Column(INTEGER(11), primary_key=True)
    proposalId = Column(INTEGER(11), nullable=False, server_default=text("-1"))
    bufferId = Column(
        ForeignKey("Buffer.bufferId", ondelete="CASCADE"), nullable=False, index=True
    )
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"), index=True
    )
    instructionSetId = Column(
        ForeignKey("InstructionSet.instructionSetId", ondelete="CASCADE"), index=True
    )
    boxId = Column(INTEGER(10))
    name = Column(String(45))
    storageTemperature = Column(String(55))
    volume = Column(String(55))
    concentration = Column(String(55))
    comments = Column(String(255))

    Buffer = relationship("Buffer")
    InstructionSet = relationship("InstructionSet")
    Macromolecule = relationship("Macromolecule")


class Stoichiometry(Base):
    __tablename__ = "Stoichiometry"

    stoichiometryId = Column(INTEGER(11), primary_key=True)
    hostMacromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    ratio = Column(String(45))

    Macromolecule = relationship(
        "Macromolecule",
        primaryjoin="Stoichiometry.hostMacromoleculeId == Macromolecule.macromoleculeId",
    )
    Macromolecule1 = relationship(
        "Macromolecule",
        primaryjoin="Stoichiometry.macromoleculeId == Macromolecule.macromoleculeId",
    )


class SubstructureDetermination(Base):
    __tablename__ = "SubstructureDetermination"

    substructureDeterminationId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingAnalysisId = Column(
        ForeignKey(
            "PhasingAnalysis.phasingAnalysisId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related phasing analysis item",
    )
    phasingProgramRunId = Column(
        ForeignKey(
            "PhasingProgramRun.phasingProgramRunId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="Related program item",
    )
    spaceGroupId = Column(
        ForeignKey("SpaceGroup.spaceGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Related spaceGroup",
    )
    method = Column(
        Enum("SAD", "MAD", "SIR", "SIRAS", "MR", "MIR", "MIRAS", "RIP", "RIPAS"),
        comment="phasing method",
    )
    lowRes = Column(Float(asdecimal=True))
    highRes = Column(Float(asdecimal=True))
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    PhasingAnalysis = relationship("PhasingAnalysis")
    PhasingProgramRun = relationship("PhasingProgramRun")
    SpaceGroup = relationship("SpaceGroup")


t_UserGroup_has_Person = Table(
    "UserGroup_has_Person",
    metadata,
    Column(
        "userGroupId",
        ForeignKey("UserGroup.userGroupId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "personId",
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class AssemblyHasMacromolecule(Base):
    __tablename__ = "AssemblyHasMacromolecule"

    AssemblyHasMacromoleculeId = Column(INTEGER(11), primary_key=True)
    assemblyId = Column(
        ForeignKey("Assembly.assemblyId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    Assembly = relationship("Assembly")
    Macromolecule = relationship("Macromolecule")


class BFSubcomponentBeamline(Base):
    __tablename__ = "BF_subcomponent_beamline"

    subcomponent_beamlineId = Column(INTEGER(10), primary_key=True)
    subcomponentId = Column(
        ForeignKey("BF_subcomponent.subcomponentId", ondelete="CASCADE"), index=True
    )
    beamlinename = Column(String(20))

    BF_subcomponent = relationship("BFSubcomponent")


class BLSession(Base):
    __tablename__ = "BLSession"

    sessionId = Column(INTEGER(10), primary_key=True)
    expSessionPk = Column(INTEGER(10), comment="smis session Pk ")
    beamLineSetupId = Column(
        ForeignKey(
            "BeamLineSetup.beamLineSetupId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    projectCode = Column(String(45))
    startDate = Column(DateTime, index=True)
    endDate = Column(DateTime, index=True)
    beamLineName = Column(String(45), index=True)
    scheduled = Column(TINYINT(1))
    nbShifts = Column(INTEGER(10), index=True)
    comments = Column(String(2000))
    beamLineOperator = Column(String(255))
    visit_number = Column(INTEGER(10), server_default=text("0"))
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    usedFlag = Column(
        TINYINT(1),
        comment="indicates if session has Datacollections or XFE or EnergyScans attached",
    )
    sessionTitle = Column(String(255), comment="fx accounts only")
    structureDeterminations = Column(Float)
    dewarTransport = Column(Float)
    databackupFrance = Column(Float, comment="data backup and express delivery France")
    databackupEurope = Column(Float, comment="data backup and express delivery Europe")
    operatorSiteNumber = Column(String(10), index=True, comment="matricule site")
    lastUpdate = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("'0000-00-00 00:00:00'"),
        comment="last update timestamp: by default the end of the session, the last collect...",
    )
    protectedData = Column(
        String(1024), comment="indicates if the data are protected or not"
    )
    externalId = Column(BINARY(16))
    nbReimbDewars = Column(INTEGER(11))

    BeamLineSetup = relationship("BeamLineSetup")
    Proposal = relationship("Proposal")
    Shipping = relationship("Shipping", secondary="ShippingHasSession")


class LabContact(Base):
    __tablename__ = "LabContact"
    __table_args__ = (
        Index("personAndProposal", "personId", "proposalId", unique=True),
        Index("cardNameAndProposal", "cardName", "proposalId", unique=True),
    )

    labContactId = Column(INTEGER(10), primary_key=True)
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), nullable=False)
    cardName = Column(String(40), nullable=False)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    defaultCourrierCompany = Column(String(45))
    courierAccount = Column(String(45))
    billingReference = Column(String(45))
    dewarAvgCustomsValue = Column(INTEGER(10), nullable=False, server_default=text("0"))
    dewarAvgTransportValue = Column(
        INTEGER(10), nullable=False, server_default=text("0")
    )
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")


class MXMRRunBlob(Base):
    __tablename__ = "MXMRRunBlob"

    mxMRRunBlobId = Column(INTEGER(10), primary_key=True)
    mxMRRunId = Column(
        ForeignKey("MXMRRun.mxMRRunId", ondelete="CASCADE"), nullable=False, index=True
    )
    view1 = Column(String(255))
    view2 = Column(String(255))
    view3 = Column(String(255))

    MXMRRun = relationship("MXMRRun")


class PhasingStatistics(Base):
    __tablename__ = "PhasingStatistics"

    phasingStatisticsId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    phasingHasScalingId1 = Column(
        ForeignKey(
            "Phasing_has_Scaling.phasingHasScalingId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="the dataset in question",
    )
    phasingHasScalingId2 = Column(
        ForeignKey(
            "Phasing_has_Scaling.phasingHasScalingId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="if this is MIT or MAD, which scaling are being compared, null otherwise",
    )
    phasingStepId = Column(
        ForeignKey("PhasingStep.phasingStepId", ondelete="CASCADE"), index=True
    )
    numberOfBins = Column(INTEGER(11), comment="the total number of bins")
    binNumber = Column(INTEGER(11), comment="binNumber, 999 for overall")
    lowRes = Column(
        Float(asdecimal=True), comment="low resolution cutoff of this binfloat"
    )
    highRes = Column(
        Float(asdecimal=True), comment="high resolution cutoff of this binfloat"
    )
    metric = Column(
        Enum(
            "Rcullis",
            "Average Fragment Length",
            "Chain Count",
            "Residues Count",
            "CC",
            "PhasingPower",
            "FOM",
            '<d"/sig>',
            "Best CC",
            "CC(1/2)",
            "Weak CC",
            "CFOM",
            "Pseudo_free_CC",
            "CC of partial model",
            "Start R-work",
            "Start R-free",
            "Final R-work",
            "Final R-free",
        ),
        comment="metric",
    )
    statisticsValue = Column(Float(asdecimal=True), comment="the statistics value")
    nReflections = Column(INTEGER(11))
    recordTimeStamp = Column(
        TIMESTAMP,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    Phasing_has_Scaling = relationship(
        "PhasingHasScaling",
        primaryjoin="PhasingStatistics.phasingHasScalingId1 == PhasingHasScaling.phasingHasScalingId",
    )
    Phasing_has_Scaling1 = relationship(
        "PhasingHasScaling",
        primaryjoin="PhasingStatistics.phasingHasScalingId2 == PhasingHasScaling.phasingHasScalingId",
    )
    PhasingStep = relationship("PhasingStep")


t_Project_has_Person = Table(
    "Project_has_Person",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "personId",
        ForeignKey("Person.personId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ProjectHasUser(Base):
    __tablename__ = "Project_has_User"

    projecthasuserid = Column(INTEGER(10), primary_key=True)
    projectid = Column(
        ForeignKey("Project.projectId", ondelete="CASCADE"), nullable=False, index=True
    )
    username = Column(String(15))

    Project = relationship("Project")


class ProposalHasPerson(Base):
    __tablename__ = "ProposalHasPerson"

    proposalHasPersonId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE"), nullable=False, index=True
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")


class Protein(Base):
    __tablename__ = "Protein"
    __table_args__ = (Index("ProteinAcronym_Index", "proposalId", "acronym"),)

    proteinId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    name = Column(VARCHAR(255))
    acronym = Column(String(45), index=True)
    description = Column(
        Text, comment="A description/summary using words and sentences"
    )
    hazardGroup = Column(
        TINYINT(3),
        nullable=False,
        server_default=text("1"),
        comment="A.k.a. risk group",
    )
    containmentLevel = Column(
        TINYINT(3),
        nullable=False,
        server_default=text("1"),
        comment="A.k.a. biosafety level, which indicates the level of containment required",
    )
    safetyLevel = Column(Enum("GREEN", "YELLOW", "RED"))
    molecularMass = Column(Float(asdecimal=True))
    proteinType = Column(String(45))
    sequence = Column(Text)
    personId = Column(INTEGER(10), index=True)
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    isCreatedBySampleSheet = Column(TINYINT(1), server_default=text("0"))
    externalId = Column(BINARY(16))
    componentTypeId = Column(
        ForeignKey(
            "ComponentType.componentTypeId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    modId = Column(String(20))
    concentrationTypeId = Column(INTEGER(10))
    _global = Column("global", TINYINT(1), server_default=text("0"))

    ComponentType = relationship("ComponentType")
    Proposal = relationship("Proposal")
    ComponentSubType = relationship(
        "ComponentSubType", secondary="Component_has_SubType"
    )


class ProteinHasLattice(Protein):
    __tablename__ = "Protein_has_Lattice"

    proteinId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE"), primary_key=True
    )
    cell_a = Column(Float(asdecimal=True))
    cell_b = Column(Float(asdecimal=True))
    cell_c = Column(Float(asdecimal=True))
    cell_alpha = Column(Float(asdecimal=True))
    cell_beta = Column(Float(asdecimal=True))
    cell_gamma = Column(Float(asdecimal=True))


class SWOnceToken(Base):
    __tablename__ = "SW_onceToken"
    __table_args__ = {
        "comment": "One-time use tokens needed for token auth in order to grant access to file downloads and webcams (and some images)"
    }

    onceTokenId = Column(INTEGER(10), primary_key=True)
    token = Column(String(128))
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    validity = Column(String(200))
    recordTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    Person = relationship("Person")
    Proposal = relationship("Proposal")


class Screen(Base):
    __tablename__ = "Screen"

    screenId = Column(INTEGER(10), primary_key=True)
    name = Column(String(45))
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    _global = Column("global", TINYINT(1))

    Proposal = relationship("Proposal")


class AssemblyRegion(Base):
    __tablename__ = "AssemblyRegion"

    assemblyRegionId = Column(INTEGER(11), primary_key=True)
    assemblyHasMacromoleculeId = Column(
        ForeignKey(
            "AssemblyHasMacromolecule.AssemblyHasMacromoleculeId", ondelete="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    assemblyRegionType = Column(String(45))
    name = Column(String(45))
    fromResiduesBases = Column(String(45))
    toResiduesBases = Column(String(45))

    AssemblyHasMacromolecule = relationship("AssemblyHasMacromolecule")


class BFFault(Base):
    __tablename__ = "BF_fault"

    faultId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    owner = Column(String(50))
    subcomponentId = Column(
        ForeignKey("BF_subcomponent.subcomponentId", ondelete="CASCADE"), index=True
    )
    starttime = Column(DateTime)
    endtime = Column(DateTime)
    beamtimelost = Column(TINYINT(1))
    beamtimelost_starttime = Column(DateTime)
    beamtimelost_endtime = Column(DateTime)
    title = Column(String(200))
    description = Column(Text)
    resolved = Column(TINYINT(1))
    resolution = Column(Text)
    assignee = Column(String(50))
    attachment = Column(String(200))
    eLogId = Column(INTEGER(11))
    personId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    assigneeId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)

    Person = relationship("Person", primaryjoin="BFFault.assigneeId == Person.personId")
    Person1 = relationship("Person", primaryjoin="BFFault.personId == Person.personId")
    BLSession = relationship("BLSession")
    BF_subcomponent = relationship("BFSubcomponent")


class BLSessionHasSCPosition(Base):
    __tablename__ = "BLSession_has_SCPosition"

    blsessionhasscpositionid = Column(INTEGER(10), primary_key=True)
    blsessionid = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    scContainer = Column(
        SMALLINT(5), comment="Position of container within sample changer"
    )
    containerPosition = Column(
        SMALLINT(5), comment="Position of sample within container"
    )

    BLSession = relationship("BLSession")


class BeamlineAction(Base):
    __tablename__ = "BeamlineAction"

    beamlineActionId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"), index=True
    )
    startTimestamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )
    endTimestamp = Column(
        TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'")
    )
    message = Column(String(255))
    parameter = Column(String(50))
    value = Column(String(30))
    loglevel = Column(Enum("DEBUG", "CRITICAL", "INFO"))
    status = Column(
        Enum("PAUSED", "RUNNING", "TERMINATED", "COMPLETE", "ERROR", "EPICSFAIL")
    )

    BLSession = relationship("BLSession")


t_Component_has_SubType = Table(
    "Component_has_SubType",
    metadata,
    Column(
        "componentId",
        ForeignKey("Protein.proteinId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "componentSubTypeId",
        ForeignKey(
            "ComponentSubType.componentSubTypeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class Crystal(Base):
    __tablename__ = "Crystal"

    crystalId = Column(INTEGER(10), primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    proteinId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    crystalUUID = Column(String(45))
    name = Column(String(255))
    spaceGroup = Column(String(20))
    morphology = Column(String(255))
    color = Column(String(45))
    size_X = Column(Float(asdecimal=True))
    size_Y = Column(Float(asdecimal=True))
    size_Z = Column(Float(asdecimal=True))
    cell_a = Column(Float(asdecimal=True))
    cell_b = Column(Float(asdecimal=True))
    cell_c = Column(Float(asdecimal=True))
    cell_alpha = Column(Float(asdecimal=True))
    cell_beta = Column(Float(asdecimal=True))
    cell_gamma = Column(Float(asdecimal=True))
    comments = Column(String(255))
    pdbFileName = Column(String(255), comment="pdb file name")
    pdbFilePath = Column(String(1024), comment="pdb file path")
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    abundance = Column(Float)
    packingFraction = Column(Float)

    DiffractionPlan = relationship("DiffractionPlan")
    Protein = relationship("Protein")


class DewarRegistry(Base):
    __tablename__ = "DewarRegistry"

    dewarRegistryId = Column(INTEGER(11), primary_key=True)
    facilityCode = Column(String(20), nullable=False, unique=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", onupdate="CASCADE"), index=True
    )
    labContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="SET NULL", onupdate="CASCADE"),
        index=True,
    )
    purchaseDate = Column(DateTime)
    bltimestamp = Column(
        DateTime, nullable=False, server_default=text("current_timestamp()")
    )

    LabContact = relationship("LabContact")
    Proposal = relationship("Proposal")


class Experiment(Base):
    __tablename__ = "Experiment"

    experimentId = Column(INTEGER(11), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"), index=True
    )
    proposalId = Column(INTEGER(11), nullable=False)
    name = Column(String(255))
    creationDate = Column(DateTime)
    experimentType = Column(String(128))
    sourceFilePath = Column(String(256))
    dataAcquisitionFilePath = Column(
        String(256),
        comment="The file path pointing to the data acquisition. Eventually it may be a compressed file with all the files or just the folder",
    )
    status = Column(String(45))
    comments = Column(String(512))

    BLSession = relationship("BLSession")


t_Project_has_Protein = Table(
    "Project_has_Protein",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "proteinId",
        ForeignKey("Protein.proteinId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_Session = Table(
    "Project_has_Session",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "sessionId",
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ProteinHasPDB(Base):
    __tablename__ = "Protein_has_PDB"

    proteinhaspdbid = Column(INTEGER(10), primary_key=True)
    proteinid = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE"), nullable=False, index=True
    )
    pdbid = Column(
        ForeignKey("PDB.pdbId", ondelete="CASCADE"), nullable=False, index=True
    )

    PDB = relationship("PDB")
    Protein = relationship("Protein")


class ScreenComponentGroup(Base):
    __tablename__ = "ScreenComponentGroup"

    screenComponentGroupId = Column(INTEGER(10), primary_key=True)
    screenId = Column(
        ForeignKey("Screen.screenId", ondelete="CASCADE"), nullable=False, index=True
    )
    position = Column(SMALLINT(6))

    Screen = relationship("Screen")


class SessionType(Base):
    __tablename__ = "SessionType"

    sessionTypeId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    typeName = Column(String(31), nullable=False)

    BLSession = relationship("BLSession")


class SessionHasPerson(Base):
    __tablename__ = "Session_has_Person"

    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    role = Column(
        Enum(
            "Local Contact",
            "Local Contact 2",
            "Staff",
            "Team Leader",
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
        )
    )
    remote = Column(TINYINT(1), server_default=text("0"))

    Person = relationship("Person")
    BLSession = relationship("BLSession")


class Shipping(Base):
    __tablename__ = "Shipping"

    shippingId = Column(INTEGER(10), primary_key=True)
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    shippingName = Column(String(45), index=True)
    deliveryAgent_agentName = Column(String(45))
    deliveryAgent_shippingDate = Column(Date)
    deliveryAgent_deliveryDate = Column(Date)
    deliveryAgent_agentCode = Column(String(45))
    deliveryAgent_flightCode = Column(String(45))
    shippingStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime)
    laboratoryId = Column(INTEGER(10), index=True)
    isStorageShipping = Column(TINYINT(1), server_default=text("0"))
    creationDate = Column(DateTime, index=True)
    comments = Column(String(255))
    sendingLabContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE"), index=True
    )
    returnLabContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE"), index=True
    )
    returnCourier = Column(String(45))
    dateOfShippingToUser = Column(DateTime)
    shippingType = Column(String(45))
    safetyLevel = Column(String(8))

    Proposal = relationship("Proposal")
    LabContact = relationship(
        "LabContact",
        primaryjoin="Shipping.returnLabContactId == LabContact.labContactId",
    )
    LabContact1 = relationship(
        "LabContact",
        primaryjoin="Shipping.sendingLabContactId == LabContact.labContactId",
    )


class BLSampleTypeHasComponent(Base):
    __tablename__ = "BLSampleType_has_Component"

    blSampleTypeId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    componentId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    abundance = Column(Float)

    Crystal = relationship("Crystal")
    Protein = relationship("Protein")


class CrystalHasUUID(Base):
    __tablename__ = "Crystal_has_UUID"

    crystal_has_UUID_Id = Column(INTEGER(10), primary_key=True)
    crystalId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    UUID = Column(String(45), index=True)
    imageURL = Column(String(255))

    Crystal = relationship("Crystal")


class Dewar(Base):
    __tablename__ = "Dewar"

    dewarId = Column(INTEGER(10), primary_key=True)
    shippingId = Column(
        ForeignKey("Shipping.shippingId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    code = Column(String(45), index=True)
    comments = Column(TINYTEXT)
    storageLocation = Column(String(45))
    dewarStatus = Column(String(45), index=True)
    bltimeStamp = Column(TIMESTAMP, server_default=text("current_timestamp()"))
    isStorageDewar = Column(TINYINT(1), server_default=text("0"))
    barCode = Column(String(45), unique=True)
    firstExperimentId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    customsValue = Column(INTEGER(10))
    transportValue = Column(INTEGER(10))
    trackingNumberToSynchrotron = Column(String(30))
    trackingNumberFromSynchrotron = Column(String(30))
    facilityCode = Column(String(20), comment="Unique barcode assigned to each dewar")
    type = Column(
        Enum("Dewar", "Toolbox"), nullable=False, server_default=text("'Dewar'")
    )
    isReimbursed = Column(
        TINYINT(1),
        server_default=text("0"),
        comment="set this dewar as reimbursed by the user office",
    )

    BLSession = relationship("BLSession")
    Shipping = relationship("Shipping")


class DewarRegistryHasProposal(Base):
    __tablename__ = "DewarRegistry_has_Proposal"
    __table_args__ = (
        Index("dewarRegistryId", "dewarRegistryId", "proposalId", unique=True),
    )

    dewarRegistryHasProposalId = Column(INTEGER(10), primary_key=True)
    dewarRegistryId = Column(
        ForeignKey("DewarRegistry.dewarRegistryId", ondelete="CASCADE")
    )
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE"),
        index=True,
        comment="Person registering the dewar",
    )
    recordTimestamp = Column(DateTime, server_default=text("current_timestamp()"))
    labContactId = Column(
        ForeignKey("LabContact.labContactId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="Owner of the dewar",
    )

    DewarRegistry = relationship("DewarRegistry")
    LabContact = relationship("LabContact")
    Person = relationship("Person")
    Proposal = relationship("Proposal")


t_Project_has_Shipping = Table(
    "Project_has_Shipping",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "shippingId",
        ForeignKey("Shipping.shippingId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class SamplePlate(Base):
    __tablename__ = "SamplePlate"

    samplePlateId = Column(INTEGER(11), primary_key=True)
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    plateGroupId = Column(
        ForeignKey("PlateGroup.plateGroupId", ondelete="CASCADE"), index=True
    )
    plateTypeId = Column(
        ForeignKey("PlateType.PlateTypeId", ondelete="CASCADE"), index=True
    )
    instructionSetId = Column(
        ForeignKey("InstructionSet.instructionSetId", ondelete="CASCADE"), index=True
    )
    boxId = Column(INTEGER(10))
    name = Column(String(45))
    slotPositionRow = Column(String(45))
    slotPositionColumn = Column(String(45))
    storageTemperature = Column(String(45))

    Experiment = relationship("Experiment")
    InstructionSet = relationship("InstructionSet")
    PlateGroup = relationship("PlateGroup")
    PlateType = relationship("PlateType")


class SaxsDataCollection(Base):
    __tablename__ = "SaxsDataCollection"

    dataCollectionId = Column(INTEGER(11), primary_key=True)
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    comments = Column(String(5120))

    Experiment = relationship("Experiment")


class ScreenComponent(Base):
    __tablename__ = "ScreenComponent"

    screenComponentId = Column(INTEGER(10), primary_key=True)
    screenComponentGroupId = Column(
        ForeignKey("ScreenComponentGroup.screenComponentGroupId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    componentId = Column(
        ForeignKey("Protein.proteinId", ondelete="CASCADE"), index=True
    )
    concentration = Column(Float)
    pH = Column(Float)

    Protein = relationship("Protein")
    ScreenComponentGroup = relationship("ScreenComponentGroup")


t_ShippingHasSession = Table(
    "ShippingHasSession",
    metadata,
    Column(
        "shippingId",
        ForeignKey("Shipping.shippingId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
    Column(
        "sessionId",
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class Container(Base):
    __tablename__ = "Container"

    containerId = Column(INTEGER(10), primary_key=True)
    dewarId = Column(
        ForeignKey("Dewar.dewarId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    code = Column(String(45))
    containerType = Column(String(20))
    capacity = Column(INTEGER(10))
    beamlineLocation = Column(String(20), index=True)
    sampleChangerLocation = Column(String(20))
    containerStatus = Column(String(45), index=True)
    bltimeStamp = Column(DateTime)
    barcode = Column(String(45), unique=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"), index=True
    )
    ownerId = Column(ForeignKey("Person.personId", ondelete="CASCADE"), index=True)
    screenId = Column(INTEGER(10))
    scheduleId = Column(INTEGER(10))
    imagerId = Column(INTEGER(10))
    scLocationUpdated = Column(DateTime)
    requestedImagerId = Column(INTEGER(10))
    requestedReturn = Column(
        TINYINT(1),
        server_default=text("0"),
        comment="True for requesting return, False means container will be disposed",
    )
    comments = Column(String(255))
    experimentType = Column(String(20))
    storageTemperature = Column(Float)

    Dewar = relationship("Dewar")
    Person = relationship("Person")
    BLSession = relationship("BLSession")


class DewarTransportHistory(Base):
    __tablename__ = "DewarTransportHistory"

    DewarTransportHistoryId = Column(INTEGER(10), primary_key=True)
    dewarId = Column(
        ForeignKey("Dewar.dewarId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    dewarStatus = Column(String(45), nullable=False)
    storageLocation = Column(String(45))
    arrivalDate = Column(DateTime)

    Dewar = relationship("Dewar")


class SamplePlatePosition(Base):
    __tablename__ = "SamplePlatePosition"

    samplePlatePositionId = Column(INTEGER(11), primary_key=True)
    samplePlateId = Column(
        ForeignKey("SamplePlate.samplePlateId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    rowNumber = Column(INTEGER(11))
    columnNumber = Column(INTEGER(11))
    volume = Column(String(45))

    SamplePlate = relationship("SamplePlate")


class Subtraction(Base):
    __tablename__ = "Subtraction"

    subtractionId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(
        ForeignKey("SaxsDataCollection.dataCollectionId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    rg = Column(String(45))
    rgStdev = Column(String(45))
    I0 = Column(String(45))
    I0Stdev = Column(String(45))
    firstPointUsed = Column(String(45))
    lastPointUsed = Column(String(45))
    quality = Column(String(45))
    isagregated = Column(String(45))
    concentration = Column(String(45))
    gnomFilePath = Column(String(255))
    rgGuinier = Column(String(45))
    rgGnom = Column(String(45))
    dmax = Column(String(45))
    total = Column(String(45))
    volume = Column(String(45))
    creationTime = Column(DateTime)
    kratkyFilePath = Column(String(255))
    scatteringFilePath = Column(String(255))
    guinierFilePath = Column(String(255))
    substractedFilePath = Column(String(255))
    gnomFilePathOutput = Column(String(255))
    sampleOneDimensionalFiles = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    bufferOnedimensionalFiles = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    sampleAverageFilePath = Column(String(255))
    bufferAverageFilePath = Column(String(255))

    FrameList = relationship(
        "FrameList",
        primaryjoin="Subtraction.bufferOnedimensionalFiles == FrameList.frameListId",
    )
    SaxsDataCollection = relationship("SaxsDataCollection")
    FrameList1 = relationship(
        "FrameList",
        primaryjoin="Subtraction.sampleOneDimensionalFiles == FrameList.frameListId",
    )


class BFAutomationFault(Base):
    __tablename__ = "BF_automationFault"

    automationFaultId = Column(INTEGER(10), primary_key=True)
    automationErrorId = Column(
        ForeignKey("BF_automationError.automationErrorId", ondelete="CASCADE"),
        index=True,
    )
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE"), index=True
    )
    severity = Column(Enum("1", "2", "3"))
    stacktrace = Column(Text)
    resolved = Column(TINYINT(1))
    faultTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    BF_automationError = relationship("BFAutomationError")
    Container = relationship("Container")


class BLSample(Base):
    __tablename__ = "BLSample"
    __table_args__ = (Index("crystalId", "crystalId", "containerId"),)

    blSampleId = Column(INTEGER(10), primary_key=True)
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    crystalId = Column(
        ForeignKey("Crystal.crystalId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    name = Column(String(100), index=True)
    code = Column(String(45))
    location = Column(String(45))
    holderLength = Column(Float(asdecimal=True))
    loopLength = Column(Float(asdecimal=True))
    loopType = Column(String(45))
    wireWidth = Column(Float(asdecimal=True))
    comments = Column(String(1024))
    completionStage = Column(String(45))
    structureStage = Column(String(45))
    publicationStage = Column(String(45))
    publicationComments = Column(String(255))
    blSampleStatus = Column(String(20), index=True)
    isInSampleChanger = Column(TINYINT(1))
    lastKnownCenteringPosition = Column(String(255))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    SMILES = Column(
        String(400),
        comment="the symbolic description of the structure of a chemical compound",
    )
    lastImageURL = Column(String(255))
    positionId = Column(INTEGER(10))
    blSubSampleId = Column(INTEGER(10))
    screenComponentGroupId = Column(INTEGER(10), index=True)
    volume = Column(Float)
    dimension1 = Column(Float(asdecimal=True))
    dimension2 = Column(Float(asdecimal=True))
    dimension3 = Column(Float(asdecimal=True))
    shape = Column(String(15))
    subLocation = Column(
        SMALLINT(5),
        comment="Indicates the sample's location on a multi-sample pin, where 1 is closest to the pin base",
    )

    Container = relationship("Container")
    Crystal = relationship("Crystal")
    DiffractionPlan = relationship("DiffractionPlan")
    DiffractionPlan1 = relationship(
        "DiffractionPlan", secondary="BLSample_has_DiffractionPlan"
    )
    Project = relationship("Project", secondary="Project_has_BLSample")


class ContainerHistory(Base):
    __tablename__ = "ContainerHistory"

    containerHistoryId = Column(INTEGER(10), primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    location = Column(String(45))
    blTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    status = Column(String(45))

    Container = relationship("Container")


class ContainerInspection(Base):
    __tablename__ = "ContainerInspection"

    containerInspectionId = Column(INTEGER(10), primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    inspectionTypeId = Column(
        ForeignKey("InspectionType.inspectionTypeId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    imagerId = Column(ForeignKey("Imager.imagerId", ondelete="CASCADE"), index=True)
    temperature = Column(Float)
    blTimeStamp = Column(DateTime)
    scheduleComponentid = Column(
        ForeignKey("ScheduleComponent.scheduleComponentId", ondelete="CASCADE"),
        index=True,
    )
    state = Column(String(20))
    priority = Column(SMALLINT(6))
    manual = Column(TINYINT(1))
    scheduledTimeStamp = Column(DateTime)
    completedTimeStamp = Column(DateTime)

    Container = relationship("Container")
    Imager = relationship("Imager")
    InspectionType = relationship("InspectionType")
    ScheduleComponent = relationship("ScheduleComponent")


class ContainerQueue(Base):
    __tablename__ = "ContainerQueue"

    containerQueueId = Column(INTEGER(10), primary_key=True)
    containerId = Column(
        ForeignKey("Container.containerId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    personId = Column(
        ForeignKey("Person.personId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    createdTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    completedTimeStamp = Column(TIMESTAMP)

    Container = relationship("Container")
    Person = relationship("Person")


class Specimen(Base):
    __tablename__ = "Specimen"

    specimenId = Column(INTEGER(11), primary_key=True)
    experimentId = Column(
        ForeignKey("Experiment.experimentId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    bufferId = Column(ForeignKey("Buffer.bufferId", ondelete="CASCADE"), index=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"), index=True
    )
    samplePlatePositionId = Column(
        ForeignKey("SamplePlatePosition.samplePlatePositionId", ondelete="CASCADE"),
        index=True,
    )
    safetyLevelId = Column(
        ForeignKey("SafetyLevel.safetyLevelId", ondelete="CASCADE"), index=True
    )
    stockSolutionId = Column(
        ForeignKey("StockSolution.stockSolutionId", ondelete="CASCADE"), index=True
    )
    code = Column(String(255))
    concentration = Column(String(45))
    volume = Column(String(45))
    comments = Column(String(5120))

    Buffer = relationship("Buffer")
    Experiment = relationship("Experiment")
    Macromolecule = relationship("Macromolecule")
    SafetyLevel = relationship("SafetyLevel")
    SamplePlatePosition = relationship("SamplePlatePosition")
    StockSolution = relationship("StockSolution")


class SubtractionToAbInitioModel(Base):
    __tablename__ = "SubtractionToAbInitioModel"

    subtractionToAbInitioModelId = Column(INTEGER(11), primary_key=True)
    abInitioId = Column(
        ForeignKey("AbInitioModel.abInitioModelId", ondelete="CASCADE"), index=True
    )
    subtractionId = Column(
        ForeignKey("Subtraction.subtractionId", ondelete="CASCADE"), index=True
    )

    AbInitioModel = relationship("AbInitioModel")
    Subtraction = relationship("Subtraction")


class BLSampleGroupHasBLSample(Base):
    __tablename__ = "BLSampleGroup_has_BLSample"

    blSampleGroupId = Column(
        ForeignKey("BLSampleGroup.blSampleGroupId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    )
    order = Column(MEDIUMINT(9))
    type = Column(Enum("background", "container", "sample", "calibrant"))

    BLSampleGroup = relationship("BLSampleGroup")
    BLSample = relationship("BLSample")


class BLSampleImage(Base):
    __tablename__ = "BLSampleImage"

    blSampleImageId = Column(INTEGER(10), primary_key=True)
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    micronsPerPixelX = Column(Float)
    micronsPerPixelY = Column(Float)
    imageFullPath = Column(String(255))
    blSampleImageScoreId = Column(INTEGER(11))
    comments = Column(String(255))
    blTimeStamp = Column(DateTime)
    containerInspectionId = Column(
        ForeignKey("ContainerInspection.containerInspectionId", ondelete="CASCADE"),
        index=True,
    )
    modifiedTimeStamp = Column(DateTime)

    BLSample = relationship("BLSample")
    ContainerInspection = relationship("ContainerInspection")


t_BLSample_has_DiffractionPlan = Table(
    "BLSample_has_DiffractionPlan",
    metadata,
    Column(
        "blSampleId",
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "diffractionPlanId",
        ForeignKey("DiffractionPlan.diffractionPlanId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class BLSubSample(Base):
    __tablename__ = "BLSubSample"

    blSubSampleId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="sample",
    )
    diffractionPlanId = Column(
        ForeignKey(
            "DiffractionPlan.diffractionPlanId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="eventually diffractionPlan",
    )
    positionId = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="position of the subsample",
    )
    position2Id = Column(
        ForeignKey("Position.positionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    blSubSampleUUID = Column(String(45), comment="uuid of the blsubsample")
    imgFileName = Column(String(255), comment="image filename")
    imgFilePath = Column(String(1024), comment="url image")
    comments = Column(String(1024), comment="comments")
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    motorPositionId = Column(
        ForeignKey(
            "MotorPosition.motorPositionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="motor position",
    )

    BLSample = relationship("BLSample")
    DiffractionPlan = relationship("DiffractionPlan")
    MotorPosition = relationship("MotorPosition")
    Position = relationship(
        "Position", primaryjoin="BLSubSample.position2Id == Position.positionId"
    )
    Position1 = relationship(
        "Position", primaryjoin="BLSubSample.positionId == Position.positionId"
    )


class DataCollectionGroup(Base):
    __tablename__ = "DataCollectionGroup"
    __table_args__ = {
        "comment": "a dataCollectionGroup is a group of dataCollection for a spe"
    }

    dataCollectionGroupId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="references BLSample table",
    )
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="references Session table",
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    experimentType = Column(
        Enum(
            "EM",
            "SAD",
            "SAD - Inverse Beam",
            "OSC",
            "Collect - Multiwedge",
            "MAD",
            "Helical",
            "Multi-positional",
            "Mesh",
            "Burn",
            "MAD - Inverse Beam",
            "Characterization",
            "Dehydration",
            "Still",
        ),
        comment="Experiment type flag",
    )
    startTime = Column(DateTime, comment="Start time of the dataCollectionGroup")
    endTime = Column(DateTime, comment="end time of the dataCollectionGroup")
    crystalClass = Column(String(20), comment="Crystal Class for industrials users")
    comments = Column(String(1024), comment="comments")
    detectorMode = Column(String(255), comment="Detector mode")
    actualSampleBarcode = Column(String(45), comment="Actual sample barcode")
    actualSampleSlotInContainer = Column(
        INTEGER(10), comment="Actual sample slot number in container"
    )
    actualContainerBarcode = Column(String(45), comment="Actual container barcode")
    actualContainerSlotInSC = Column(
        INTEGER(10), comment="Actual container slot number in sample changer"
    )
    xtalSnapshotFullPath = Column(String(255))

    BLSample = relationship("BLSample")
    BLSession = relationship("BLSession")
    Workflow = relationship("Workflow")
    Project = relationship("Project", secondary="Project_has_DCGroup")


class DataCollectionPlanGroup(Base):
    __tablename__ = "DataCollectionPlanGroup"

    dataCollectionPlanGroupId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    BLSample = relationship("BLSample")
    BLSession = relationship("BLSession")


class Measurement(Base):
    __tablename__ = "Measurement"

    measurementId = Column(INTEGER(11), primary_key=True)
    specimenId = Column(
        ForeignKey("Specimen.specimenId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    runId = Column(ForeignKey("Run.runId", ondelete="CASCADE"), index=True)
    code = Column(String(100))
    imageDirectory = Column(String(512))
    priorityLevelId = Column(INTEGER(11))
    exposureTemperature = Column(String(45))
    viscosity = Column(String(45))
    flow = Column(TINYINT(1))
    extraFlowTime = Column(String(45))
    volumeToLoad = Column(String(45))
    waitTime = Column(String(45))
    transmission = Column(String(45))
    comments = Column(String(512))
    pathToH5 = Column(String(512))

    Run = relationship("Run")
    Specimen = relationship("Specimen")


t_Project_has_BLSample = Table(
    "Project_has_BLSample",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "blSampleId",
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class RobotAction(Base):
    __tablename__ = "RobotAction"
    __table_args__ = {"comment": "Robot actions as reported by MXCube"}

    robotActionId = Column(INTEGER(10), primary_key=True)
    blsessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    blsampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"), index=True
    )
    actionType = Column(Enum("LOAD", "UNLOAD", "DISPOSE", "STORE", "WASH", "ANNEAL"))
    startTimestamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp() ON UPDATE current_timestamp()"),
    )
    endTimestamp = Column(
        TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'")
    )
    status = Column(Enum("SUCCESS", "ERROR", "CRITICAL", "WARNING", "COMMANDNOTSENT"))
    message = Column(String(255))
    containerLocation = Column(SMALLINT(6))
    dewarLocation = Column(SMALLINT(6))
    sampleBarcode = Column(String(45))
    xtalSnapshotBefore = Column(String(255))
    xtalSnapshotAfter = Column(String(255))

    BLSample = relationship("BLSample")
    BLSession = relationship("BLSession")


class Structure(Base):
    __tablename__ = "Structure"

    structureId = Column(INTEGER(11), primary_key=True)
    macromoleculeId = Column(
        ForeignKey("Macromolecule.macromoleculeId", ondelete="CASCADE"), index=True
    )
    crystalId = Column(ForeignKey("Crystal.crystalId", ondelete="CASCADE"), index=True)
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"), index=True
    )
    filePath = Column(String(2048))
    structureType = Column(String(45))
    fromResiduesBases = Column(String(45))
    toResiduesBases = Column(String(45))
    sequence = Column(String(45))
    creationDate = Column(DateTime)
    name = Column(String(255))
    symmetry = Column(String(45))
    multiplicity = Column(String(45))
    groupName = Column(String(45))
    proposalId = Column(
        ForeignKey("Proposal.proposalId", ondelete="CASCADE"), index=True
    )
    uniprotId = Column(String(45))

    BLSample = relationship("BLSample")
    Crystal = relationship("Crystal")
    Macromolecule = relationship("Macromolecule")
    Proposal = relationship("Proposal")


class BLSampleImageAnalysis(Base):
    __tablename__ = "BLSampleImageAnalysis"

    blSampleImageAnalysisId = Column(INTEGER(10), primary_key=True)
    blSampleImageId = Column(
        ForeignKey("BLSampleImage.blSampleImageId", ondelete="CASCADE"), index=True
    )
    oavSnapshotBefore = Column(String(255))
    oavSnapshotAfter = Column(String(255))
    deltaX = Column(INTEGER(11))
    deltaY = Column(INTEGER(11))
    goodnessOfFit = Column(Float)
    scaleFactor = Column(Float)
    resultCode = Column(String(15))
    matchStartTimeStamp = Column(TIMESTAMP, server_default=text("current_timestamp()"))
    matchEndTimeStamp = Column(TIMESTAMP)

    BLSampleImage = relationship("BLSampleImage")


class ContainerQueueSample(Base):
    __tablename__ = "ContainerQueueSample"

    containerQueueSampleId = Column(INTEGER(10), primary_key=True)
    containerQueueId = Column(
        ForeignKey(
            "ContainerQueue.containerQueueId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )

    BLSubSample = relationship("BLSubSample")
    ContainerQueue = relationship("ContainerQueue")


class EnergyScan(Base):
    __tablename__ = "EnergyScan"

    energyScanId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE"), index=True
    )
    fluorescenceDetector = Column(String(255))
    scanFileFullPath = Column(String(255))
    choochFileFullPath = Column(String(255))
    jpegChoochFileFullPath = Column(String(255))
    element = Column(String(45))
    startEnergy = Column(Float)
    endEnergy = Column(Float)
    transmissionFactor = Column(Float)
    exposureTime = Column(Float)
    axisPosition = Column(Float)
    synchrotronCurrent = Column(Float)
    temperature = Column(Float)
    peakEnergy = Column(Float)
    peakFPrime = Column(Float)
    peakFDoublePrime = Column(Float)
    inflectionEnergy = Column(Float)
    inflectionFPrime = Column(Float)
    inflectionFDoublePrime = Column(Float)
    xrayDose = Column(Float)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    edgeEnergy = Column(String(255))
    filename = Column(String(255))
    beamSizeVertical = Column(Float)
    beamSizeHorizontal = Column(Float)
    crystalClass = Column(String(20))
    comments = Column(String(1024))
    flux = Column(Float(asdecimal=True), comment="flux measured before the energyScan")
    flux_end = Column(
        Float(asdecimal=True), comment="flux measured after the energyScan"
    )
    workingDirectory = Column(String(45))
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE"), index=True
    )
    remoteEnergy = Column(Float)
    remoteFPrime = Column(Float)
    remoteFDoublePrime = Column(Float)

    BLSample = relationship("BLSample")
    BLSubSample = relationship("BLSubSample")
    BLSession = relationship("BLSession")
    Project = relationship("Project", secondary="Project_has_EnergyScan")


class FitStructureToExperimentalData(Base):
    __tablename__ = "FitStructureToExperimentalData"

    fitStructureToExperimentalDataId = Column(INTEGER(11), primary_key=True)
    structureId = Column(
        ForeignKey("Structure.structureId", ondelete="CASCADE"), index=True
    )
    subtractionId = Column(
        ForeignKey("Subtraction.subtractionId", ondelete="CASCADE"), index=True
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE"), index=True
    )
    fitFilePath = Column(String(255))
    logFilePath = Column(String(255))
    outputFilePath = Column(String(255))
    creationDate = Column(DateTime)
    comments = Column(String(2048))

    Structure = relationship("Structure")
    Subtraction = relationship("Subtraction")
    Workflow = relationship("Workflow")


class MeasurementToDataCollection(Base):
    __tablename__ = "MeasurementToDataCollection"

    measurementToDataCollectionId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(
        ForeignKey("SaxsDataCollection.dataCollectionId", ondelete="CASCADE"),
        index=True,
    )
    measurementId = Column(
        ForeignKey("Measurement.measurementId", ondelete="CASCADE"), index=True
    )
    dataCollectionOrder = Column(INTEGER(11))

    SaxsDataCollection = relationship("SaxsDataCollection")
    Measurement = relationship("Measurement")


class Merge(Base):
    __tablename__ = "Merge"

    mergeId = Column(INTEGER(11), primary_key=True)
    measurementId = Column(
        ForeignKey("Measurement.measurementId", ondelete="CASCADE"), index=True
    )
    frameListId = Column(
        ForeignKey("FrameList.frameListId", ondelete="CASCADE"), index=True
    )
    discardedFrameNameList = Column(String(1024))
    averageFilePath = Column(String(255))
    framesCount = Column(String(45))
    framesMerge = Column(String(45))
    creationDate = Column(DateTime)

    FrameList = relationship("FrameList")
    Measurement = relationship("Measurement")


t_Project_has_DCGroup = Table(
    "Project_has_DCGroup",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "dataCollectionGroupId",
        ForeignKey(
            "DataCollectionGroup.dataCollectionGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class Screening(Base):
    __tablename__ = "Screening"

    screeningId = Column(INTEGER(10), primary_key=True)
    diffractionPlanId = Column(
        INTEGER(10), index=True, comment="references DiffractionPlan"
    )
    dataCollectionGroupId = Column(
        ForeignKey("DataCollectionGroup.dataCollectionGroupId", ondelete="CASCADE"),
        index=True,
    )
    dataCollectionId = Column(INTEGER(10))
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )
    programVersion = Column(String(45))
    comments = Column(String(255))
    shortComments = Column(String(20))
    xmlSampleInformation = Column(LONGBLOB)

    DataCollectionGroup = relationship("DataCollectionGroup")


class XFEFluorescenceSpectrum(Base):
    __tablename__ = "XFEFluorescenceSpectrum"

    xfeFluorescenceSpectrumId = Column(INTEGER(10), primary_key=True)
    sessionId = Column(
        ForeignKey("BLSession.sessionId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
    )
    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
    )
    fittedDataFileFullPath = Column(String(255))
    scanFileFullPath = Column(String(255))
    jpegScanFileFullPath = Column(String(255))
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    filename = Column(String(255))
    energy = Column(Float)
    exposureTime = Column(Float)
    axisPosition = Column(Float)
    beamTransmission = Column(Float)
    annotatedPymcaXfeSpectrum = Column(String(255))
    beamSizeVertical = Column(Float)
    beamSizeHorizontal = Column(Float)
    crystalClass = Column(String(20))
    comments = Column(String(1024))
    flux = Column(Float(asdecimal=True), comment="flux measured before the xrfSpectra")
    flux_end = Column(
        Float(asdecimal=True), comment="flux measured after the xrfSpectra"
    )
    workingDirectory = Column(String(512))
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE"), index=True
    )

    BLSample = relationship("BLSample")
    BLSubSample = relationship("BLSubSample")
    BLSession = relationship("BLSession")


class BLSampleHasEnergyScan(Base):
    __tablename__ = "BLSample_has_EnergyScan"

    blSampleId = Column(
        ForeignKey("BLSample.blSampleId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    energyScanId = Column(
        ForeignKey("EnergyScan.energyScanId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    blSampleHasEnergyScanId = Column(INTEGER(11), primary_key=True)

    BLSample = relationship("BLSample")
    EnergyScan = relationship("EnergyScan")


class MixtureToStructure(Base):
    __tablename__ = "MixtureToStructure"

    fitToStructureId = Column(INTEGER(11), primary_key=True)
    structureId = Column(
        ForeignKey("Structure.structureId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    mixtureId = Column(
        ForeignKey(
            "FitStructureToExperimentalData.fitStructureToExperimentalDataId",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    volumeFraction = Column(String(45))
    creationDate = Column(DateTime)

    FitStructureToExperimentalData = relationship("FitStructureToExperimentalData")
    Structure = relationship("Structure")


t_Project_has_EnergyScan = Table(
    "Project_has_EnergyScan",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "energyScanId",
        ForeignKey("EnergyScan.energyScanId", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


t_Project_has_XFEFSpectrum = Table(
    "Project_has_XFEFSpectrum",
    metadata,
    Column(
        "projectId",
        ForeignKey("Project.projectId", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "xfeFluorescenceSpectrumId",
        ForeignKey(
            "XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId", ondelete="CASCADE"
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)


class ScreeningInput(Base):
    __tablename__ = "ScreeningInput"

    screeningInputId = Column(INTEGER(10), primary_key=True)
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    diffractionPlanId = Column(INTEGER(11), comment="references DiffractionPlan table")
    beamX = Column(Float)
    beamY = Column(Float)
    rmsErrorLimits = Column(Float)
    minimumFractionIndexed = Column(Float)
    maximumFractionRejected = Column(Float)
    minimumSignalToNoise = Column(Float)
    xmlSampleInformation = Column(LONGBLOB)

    Screening = relationship("Screening")


class ScreeningOutput(Base):
    __tablename__ = "ScreeningOutput"

    screeningOutputId = Column(INTEGER(10), primary_key=True)
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    statusDescription = Column(String(1024))
    rejectedReflections = Column(INTEGER(10))
    resolutionObtained = Column(Float)
    spotDeviationR = Column(Float)
    spotDeviationTheta = Column(Float)
    beamShiftX = Column(Float)
    beamShiftY = Column(Float)
    numSpotsFound = Column(INTEGER(10))
    numSpotsUsed = Column(INTEGER(10))
    numSpotsRejected = Column(INTEGER(10))
    mosaicity = Column(Float)
    iOverSigma = Column(Float)
    diffractionRings = Column(TINYINT(1))
    strategySuccess = Column(TINYINT(1), nullable=False, server_default=text("0"))
    mosaicityEstimated = Column(TINYINT(1), nullable=False, server_default=text("0"))
    rankingResolution = Column(Float(asdecimal=True))
    program = Column(String(45))
    doseTotal = Column(Float(asdecimal=True))
    totalExposureTime = Column(Float(asdecimal=True))
    totalRotationRange = Column(Float(asdecimal=True))
    totalNumberOfImages = Column(INTEGER(11))
    rFriedel = Column(Float(asdecimal=True))
    indexingSuccess = Column(TINYINT(1), nullable=False, server_default=text("0"))
    screeningSuccess = Column(TINYINT(1), server_default=text("0"))

    Screening = relationship("Screening")


class ScreeningRank(Base):
    __tablename__ = "ScreeningRank"

    screeningRankId = Column(INTEGER(10), primary_key=True)
    screeningRankSetId = Column(
        ForeignKey(
            "ScreeningRankSet.screeningRankSetId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    screeningId = Column(
        ForeignKey("Screening.screeningId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    rankValue = Column(Float)
    rankInformation = Column(String(1024))

    Screening = relationship("Screening")
    ScreeningRankSet = relationship("ScreeningRankSet")


class ScreeningOutputLattice(Base):
    __tablename__ = "ScreeningOutputLattice"

    screeningOutputLatticeId = Column(INTEGER(10), primary_key=True)
    screeningOutputId = Column(
        ForeignKey(
            "ScreeningOutput.screeningOutputId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    spaceGroup = Column(String(45))
    pointGroup = Column(String(45))
    bravaisLattice = Column(String(45))
    rawOrientationMatrix_a_x = Column(Float)
    rawOrientationMatrix_a_y = Column(Float)
    rawOrientationMatrix_a_z = Column(Float)
    rawOrientationMatrix_b_x = Column(Float)
    rawOrientationMatrix_b_y = Column(Float)
    rawOrientationMatrix_b_z = Column(Float)
    rawOrientationMatrix_c_x = Column(Float)
    rawOrientationMatrix_c_y = Column(Float)
    rawOrientationMatrix_c_z = Column(Float)
    unitCell_a = Column(Float)
    unitCell_b = Column(Float)
    unitCell_c = Column(Float)
    unitCell_alpha = Column(Float)
    unitCell_beta = Column(Float)
    unitCell_gamma = Column(Float)
    bltimeStamp = Column(TIMESTAMP, server_default=text("current_timestamp()"))
    labelitIndexing = Column(TINYINT(1), server_default=text("0"))

    ScreeningOutput = relationship("ScreeningOutput")


class ScreeningStrategy(Base):
    __tablename__ = "ScreeningStrategy"

    screeningStrategyId = Column(INTEGER(10), primary_key=True)
    screeningOutputId = Column(
        ForeignKey(
            "ScreeningOutput.screeningOutputId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    phiStart = Column(Float)
    phiEnd = Column(Float)
    rotation = Column(Float)
    exposureTime = Column(Float)
    resolution = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    anomalous = Column(TINYINT(1), nullable=False, server_default=text("0"))
    program = Column(String(45))
    rankingResolution = Column(Float)
    transmission = Column(
        Float, comment="Transmission for the strategy as given by the strategy program."
    )

    ScreeningOutput = relationship("ScreeningOutput")


class ScreeningStrategyWedge(Base):
    __tablename__ = "ScreeningStrategyWedge"

    screeningStrategyWedgeId = Column(
        INTEGER(10), primary_key=True, comment="Primary key"
    )
    screeningStrategyId = Column(
        ForeignKey(
            "ScreeningStrategy.screeningStrategyId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="Foreign key to parent table",
    )
    wedgeNumber = Column(
        INTEGER(10), comment="The number of this wedge within the strategy"
    )
    resolution = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    doseTotal = Column(Float, comment="Total dose for this wedge")
    numberOfImages = Column(INTEGER(10), comment="Number of images for this wedge")
    phi = Column(Float)
    kappa = Column(Float)
    chi = Column(Float)
    comments = Column(String(255))
    wavelength = Column(Float(asdecimal=True))

    ScreeningStrategy = relationship("ScreeningStrategy")


class ScreeningStrategySubWedge(Base):
    __tablename__ = "ScreeningStrategySubWedge"

    screeningStrategySubWedgeId = Column(
        INTEGER(10), primary_key=True, comment="Primary key"
    )
    screeningStrategyWedgeId = Column(
        ForeignKey(
            "ScreeningStrategyWedge.screeningStrategyWedgeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="Foreign key to parent table",
    )
    subWedgeNumber = Column(
        INTEGER(10), comment="The number of this subwedge within the wedge"
    )
    rotationAxis = Column(String(45), comment="Angle where subwedge starts")
    axisStart = Column(Float, comment="Angle where subwedge ends")
    axisEnd = Column(Float, comment="Exposure time for subwedge")
    exposureTime = Column(Float, comment="Transmission for subwedge")
    transmission = Column(Float)
    oscillationRange = Column(Float)
    completeness = Column(Float)
    multiplicity = Column(Float)
    doseTotal = Column(Float, comment="Total dose for this subwedge")
    numberOfImages = Column(INTEGER(10), comment="Number of images for this subwedge")
    comments = Column(String(255))
    resolution = Column(Float)

    ScreeningStrategyWedge = relationship("ScreeningStrategyWedge")


class DataCollection(Base):
    __tablename__ = "DataCollection"

    dataCollectionId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    dataCollectionGroupId = Column(
        ForeignKey(
            "DataCollectionGroup.dataCollectionGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="references DataCollectionGroup table",
    )
    strategySubWedgeOrigId = Column(
        ForeignKey(
            "ScreeningStrategySubWedge.screeningStrategySubWedgeId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
        comment="references ScreeningStrategySubWedge table",
    )
    detectorId = Column(
        ForeignKey("Detector.detectorId", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        comment="references Detector table",
    )
    blSubSampleId = Column(
        ForeignKey("BLSubSample.blSubSampleId", ondelete="CASCADE"), index=True
    )
    startPositionId = Column(INTEGER(10), index=True)
    endPositionId = Column(INTEGER(10), index=True)
    dataCollectionNumber = Column(INTEGER(10), index=True)
    startTime = Column(DateTime, index=True, comment="Start time of the dataCollection")
    endTime = Column(DateTime, comment="end time of the dataCollection")
    runStatus = Column(String(45))
    axisStart = Column(Float)
    axisEnd = Column(Float)
    axisRange = Column(Float)
    overlap = Column(Float)
    numberOfImages = Column(INTEGER(10))
    startImageNumber = Column(INTEGER(10))
    numberOfPasses = Column(INTEGER(10))
    exposureTime = Column(Float)
    imageDirectory = Column(String(255), index=True)
    imagePrefix = Column(String(100), index=True)
    imageSuffix = Column(String(45))
    imageContainerSubPath = Column(
        String(255),
        comment="Internal path of a HDF5 file pointing to the data for this data collection",
    )
    fileTemplate = Column(String(255))
    wavelength = Column(Float)
    resolution = Column(Float)
    detectorDistance = Column(Float)
    xBeam = Column(Float)
    yBeam = Column(Float)
    xBeamPix = Column(Float, comment="Beam size in pixels")
    yBeamPix = Column(Float, comment="Beam size in pixels")
    comments = Column(String(1024))
    printableForReport = Column(TINYINT(3), server_default=text("1"))
    slitGapVertical = Column(Float)
    slitGapHorizontal = Column(Float)
    transmission = Column(Float)
    synchrotronMode = Column(String(20))
    xtalSnapshotFullPath1 = Column(String(255))
    xtalSnapshotFullPath2 = Column(String(255))
    xtalSnapshotFullPath3 = Column(String(255))
    xtalSnapshotFullPath4 = Column(String(255))
    rotationAxis = Column(Enum("Omega", "Kappa", "Phi"))
    phiStart = Column(Float)
    kappaStart = Column(Float)
    omegaStart = Column(Float)
    resolutionAtCorner = Column(Float)
    detector2Theta = Column(Float)
    undulatorGap1 = Column(Float)
    undulatorGap2 = Column(Float)
    undulatorGap3 = Column(Float)
    beamSizeAtSampleX = Column(Float)
    beamSizeAtSampleY = Column(Float)
    centeringMethod = Column(String(255))
    averageTemperature = Column(Float)
    actualCenteringPosition = Column(String(255))
    beamShape = Column(String(45))
    flux = Column(Float(asdecimal=True))
    flux_end = Column(Float(asdecimal=True), comment="flux measured after the collect")
    totalAbsorbedDose = Column(
        Float(asdecimal=True), comment="expected dose delivered to the crystal, EDNA"
    )
    bestWilsonPlotPath = Column(String(255))
    imageQualityIndicatorsPlotPath = Column(String(512))
    imageQualityIndicatorsCSVPath = Column(String(512))
    blSampleId = Column(INTEGER(10))
    sessionId = Column(INTEGER(10), server_default=text("0"))
    experimentType = Column(String(24))
    crystalClass = Column(String(20))
    chiStart = Column(Float)
    detectorMode = Column(String(255))
    actualSampleBarcode = Column(String(45))
    actualSampleSlotInContainer = Column(INTEGER(10))
    actualContainerBarcode = Column(String(45))
    actualContainerSlotInSC = Column(INTEGER(10))
    positionId = Column(INTEGER(10))
    focalSpotSizeAtSampleX = Column(Float)
    polarisation = Column(Float)
    focalSpotSizeAtSampleY = Column(Float)
    apertureId = Column(INTEGER(10))
    screeningOrigId = Column(INTEGER(10))
    processedDataFile = Column(String(255))
    datFullPath = Column(String(255))
    magnification = Column(INTEGER(11), comment="Unit: X")
    binning = Column(
        TINYINT(1),
        server_default=text("1"),
        comment="1 or 2. Number of pixels to process as 1. (Use mean value.)",
    )
    particleDiameter = Column(Float, comment="Unit: nm")
    boxSize_CTF = Column(Float, comment="Unit: pixels")
    minResolution = Column(Float, comment="Unit: A")
    minDefocus = Column(Float, comment="Unit: A")
    maxDefocus = Column(Float, comment="Unit: A")
    defocusStepSize = Column(Float, comment="Unit: A")
    amountAstigmatism = Column(Float, comment="Unit: A")
    extractSize = Column(Float, comment="Unit: pixels")
    bgRadius = Column(Float, comment="Unit: nm")
    voltage = Column(Float, comment="Unit: kV")
    objAperture = Column(Float, comment="Unit: um")
    c1aperture = Column(Float, comment="Unit: um")
    c2aperture = Column(Float, comment="Unit: um")
    c3aperture = Column(Float, comment="Unit: um")
    c1lens = Column(Float, comment="Unit: %")
    c2lens = Column(Float, comment="Unit: %")
    c3lens = Column(Float, comment="Unit: %")

    BLSubSample = relationship("BLSubSample")
    DataCollectionGroup = relationship("DataCollectionGroup")
    Detector = relationship("Detector")
    ScreeningStrategySubWedge = relationship("ScreeningStrategySubWedge")


class AutoProcProgram(Base):
    __tablename__ = "AutoProcProgram"

    autoProcProgramId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    dataCollectionId = Column(
        ForeignKey("DataCollection.dataCollectionId", ondelete="CASCADE"), index=True
    )
    processingCommandLine = Column(
        String(255), comment="Command line for running the automatic processing"
    )
    processingPrograms = Column(
        String(255), comment="Processing programs (comma separated)"
    )
    processingStatus = Column(
        Enum("RUNNING", "FAILED", "SUCCESS", "0", "1"), comment="success (1) / fail (0)"
    )
    processingMessage = Column(String(255), comment="warning, error,...")
    processingStartTime = Column(DateTime, comment="Processing start time")
    processingEndTime = Column(DateTime, comment="Processing end time")
    processingEnvironment = Column(String(255), comment="Cpus, Nodes,...")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    DataCollection = relationship("DataCollection")


class DataCollectionFileAttachment(Base):
    __tablename__ = "DataCollectionFileAttachment"

    dataCollectionFileAttachmentId = Column(INTEGER(10), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    fileFullPath = Column(String(255), nullable=False)
    fileType = Column(
        Enum("snapshot", "log", "xy", "recip"),
        comment="snapshot: image file, usually of the sample. \\r\\nlog: a text file with logging info. \\r\\nxy: x and y data in text format. \\r\\nrecip: a compressed csv file with reciprocal space coordinates.",
    )
    createTime = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    DataCollection = relationship("DataCollection")


class Image(Base):
    __tablename__ = "Image"
    __table_args__ = (Index("Image_Index3", "fileLocation", "fileName"),)

    imageId = Column(INTEGER(10), primary_key=True)
    dataCollectionId = Column(
        ForeignKey("DataCollection.dataCollectionId", ondelete="CASCADE"),
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        server_default=text("0"),
    )
    motorPositionId = Column(INTEGER(10), index=True)
    imageNumber = Column(INTEGER(10), index=True)
    fileName = Column(String(255))
    fileLocation = Column(String(255))
    measuredIntensity = Column(Float)
    jpegFileFullPath = Column(String(255))
    jpegThumbnailFileFullPath = Column(String(255))
    temperature = Column(Float)
    cumulativeIntensity = Column(Float)
    synchrotronCurrent = Column(Float)
    comments = Column(String(1024))
    machineMessage = Column(String(1024))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    DataCollection = relationship(
        "DataCollection",
        primaryjoin="Image.dataCollectionId == DataCollection.dataCollectionId",
    )


class Movie(Base):
    __tablename__ = "Movie"

    movieId = Column(INTEGER(11), primary_key=True)
    dataCollectionId = Column(
        ForeignKey("DataCollection.dataCollectionId", ondelete="CASCADE"), index=True
    )
    movieNumber = Column(INTEGER(11))
    movieFullPath = Column(String(255), index=True)
    positionX = Column(String(45))
    positionY = Column(String(45))
    micrographFullPath = Column(String(255))
    micrographSnapshotFullPath = Column(String(255))
    xmlMetaDataFullPath = Column(String(255))
    dosePerImage = Column(String(45))
    createdTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    DataCollection = relationship("DataCollection")


class Particle(Base):
    __tablename__ = "Particle"

    particleId = Column(INTEGER(10), primary_key=True)
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    x = Column(Float)
    y = Column(Float)

    DataCollection = relationship("DataCollection")


class XRFFluorescenceMapping(Base):
    __tablename__ = "XRFFluorescenceMapping"

    xrfFluorescenceMappingId = Column(INTEGER(10), primary_key=True)
    xrfFluorescenceMappingROIId = Column(
        ForeignKey(
            "XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
    )
    imageNumber = Column(INTEGER(10), nullable=False)
    counts = Column(INTEGER(10), nullable=False)

    DataCollection = relationship("DataCollection")
    XRFFluorescenceMappingROI = relationship("XRFFluorescenceMappingROI")


class AutoProcIntegration(Base):
    __tablename__ = "AutoProcIntegration"

    autoProcIntegrationId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    dataCollectionId = Column(
        ForeignKey(
            "DataCollection.dataCollectionId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="DataCollection item",
    )
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="Related program item",
    )
    startImageNumber = Column(INTEGER(10), comment="start image number")
    endImageNumber = Column(INTEGER(10), comment="end image number")
    refinedDetectorDistance = Column(
        Float, comment="Refined DataCollection.detectorDistance"
    )
    refinedXBeam = Column(Float, comment="Refined DataCollection.xBeam")
    refinedYBeam = Column(Float, comment="Refined DataCollection.yBeam")
    rotationAxisX = Column(Float, comment="Rotation axis")
    rotationAxisY = Column(Float, comment="Rotation axis")
    rotationAxisZ = Column(Float, comment="Rotation axis")
    beamVectorX = Column(Float, comment="Beam vector")
    beamVectorY = Column(Float, comment="Beam vector")
    beamVectorZ = Column(Float, comment="Beam vector")
    cell_a = Column(Float, comment="Unit cell")
    cell_b = Column(Float, comment="Unit cell")
    cell_c = Column(Float, comment="Unit cell")
    cell_alpha = Column(Float, comment="Unit cell")
    cell_beta = Column(Float, comment="Unit cell")
    cell_gamma = Column(Float, comment="Unit cell")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    anomalous = Column(
        TINYINT(1), server_default=text("0"), comment="boolean type:0 noanoum - 1 anoum"
    )

    AutoProcProgram = relationship("AutoProcProgram")
    DataCollection = relationship("DataCollection")


class AutoProcProgramAttachment(Base):
    __tablename__ = "AutoProcProgramAttachment"

    autoProcProgramAttachmentId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Related autoProcProgram item",
    )
    fileType = Column(Enum("Log", "Result", "Graph"), comment="Type of file Attachment")
    fileName = Column(String(255), comment="Attachment filename")
    filePath = Column(String(255), comment="Attachment filepath to disk storage")
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    AutoProcProgram = relationship("AutoProcProgram")


class ImageQualityIndicators(Base):
    __tablename__ = "ImageQualityIndicators"

    imageQualityIndicatorsId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    imageId = Column(INTEGER(11), index=True)
    autoProcProgramId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
        index=True,
        comment="Foreign key to the AutoProcProgram table",
    )
    spotTotal = Column(INTEGER(11), comment="Total number of spots")
    inResTotal = Column(
        INTEGER(11), comment="Total number of spots in resolution range"
    )
    goodBraggCandidates = Column(
        INTEGER(11), comment="Total number of Bragg diffraction spots"
    )
    iceRings = Column(INTEGER(11), comment="Number of ice rings identified")
    method1Res = Column(Float, comment="Resolution estimate 1 (see publication)")
    method2Res = Column(Float, comment="Resolution estimate 2 (see publication)")
    maxUnitCell = Column(
        Float, comment="Estimation of the largest possible unit cell edge"
    )
    pctSaturationTop50Peaks = Column(
        Float, comment="The fraction of the dynamic range being used"
    )
    inResolutionOvrlSpots = Column(INTEGER(11), comment="Number of spots overloaded")
    binPopCutOffMethod2Res = Column(
        Float, comment="Cut off used in resolution limit calculation"
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")
    totalIntegratedSignal = Column(Float(asdecimal=True))
    dozor_score = Column(Float(asdecimal=True), comment="dozor_score")
    dataCollectionId = Column(INTEGER(10))
    imageNumber = Column(MEDIUMINT(8))

    AutoProcProgram = relationship("AutoProcProgram")


class MotionCorrection(Base):
    __tablename__ = "MotionCorrection"

    motionCorrectionId = Column(INTEGER(11), primary_key=True)
    movieId = Column(ForeignKey("Movie.movieId", ondelete="CASCADE"), index=True)
    firstFrame = Column(String(45))
    lastFrame = Column(String(45))
    dosePerFrame = Column(String(45))
    doseWeight = Column(String(45))
    totalMotion = Column(String(45))
    averageMotionPerFrame = Column(String(45))
    driftPlotFullPath = Column(String(512))
    micrographFullPath = Column(String(512))
    micrographSnapshotFullPath = Column(String(512))
    correctedDoseMicrographFullPath = Column(String(512))
    patchesUsed = Column(String(45))
    logFileFullPath = Column(String(512))
    createdTimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    Movie = relationship("Movie")


class PDBEntry(Base):
    __tablename__ = "PDBEntry"

    pdbEntryId = Column(INTEGER(10), primary_key=True)
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", ondelete="CASCADE"), index=True
    )
    code = Column(String(4))
    cell_a = Column(Float)
    cell_b = Column(Float)
    cell_c = Column(Float)
    cell_alpha = Column(Float)
    cell_beta = Column(Float)
    cell_gamma = Column(Float)
    resolution = Column(Float)
    pdbTitle = Column(String(255))
    pdbAuthors = Column(String(600))
    pdbDate = Column(DateTime)
    pdbBeamlineName = Column(String(50))
    beamlines = Column(String(100))
    distance = Column(Float)
    autoProcCount = Column(SMALLINT(6))
    dataCollectionCount = Column(SMALLINT(6))
    beamlineMatch = Column(TINYINT(1))
    authorMatch = Column(TINYINT(1))

    AutoProcProgram = relationship("AutoProcProgram")


class WorkflowMesh(Base):
    __tablename__ = "WorkflowMesh"

    workflowMeshId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    workflowId = Column(
        ForeignKey("Workflow.workflowId", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        index=True,
        comment="Related workflow",
    )
    bestPositionId = Column(INTEGER(10), index=True)
    bestImageId = Column(
        ForeignKey("Image.imageId", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )
    value1 = Column(Float(asdecimal=True))
    value2 = Column(Float(asdecimal=True))
    value3 = Column(Float(asdecimal=True), comment="N value")
    value4 = Column(Float(asdecimal=True))
    cartographyPath = Column(String(255))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )

    Image = relationship("Image")
    Workflow = relationship("Workflow")


class AutoProcScalingHasInt(Base):
    __tablename__ = "AutoProcScaling_has_Int"
    __table_args__ = (
        Index(
            "AutoProcScalingHasInt_FKIndex3",
            "autoProcScalingId",
            "autoProcIntegrationId",
        ),
    )

    autoProcScaling_has_IntId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcScalingId = Column(
        ForeignKey(
            "AutoProcScaling.autoProcScalingId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
        comment="AutoProcScaling item",
    )
    autoProcIntegrationId = Column(
        ForeignKey(
            "AutoProcIntegration.autoProcIntegrationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
        comment="AutoProcIntegration item",
    )
    recordTimeStamp = Column(DateTime, comment="Creation or last update date/time")

    AutoProcIntegration = relationship("AutoProcIntegration")
    AutoProcScaling = relationship("AutoProcScaling")


class AutoProcStatus(Base):
    __tablename__ = "AutoProcStatus"
    __table_args__ = {
        "comment": "AutoProcStatus table is linked to AutoProcIntegration"
    }

    autoProcStatusId = Column(
        INTEGER(11), primary_key=True, comment="Primary key (auto-incremented)"
    )
    autoProcIntegrationId = Column(
        ForeignKey(
            "AutoProcIntegration.autoProcIntegrationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=False,
        index=True,
    )
    step = Column(
        Enum("Indexing", "Integration", "Correction", "Scaling", "Importing"),
        nullable=False,
        comment="autoprocessing step",
    )
    status = Column(
        Enum("Launched", "Successful", "Failed"),
        nullable=False,
        comment="autoprocessing status",
    )
    comments = Column(String(1024), comment="comments")
    bltimeStamp = Column(
        TIMESTAMP, nullable=False, server_default=text("current_timestamp()")
    )

    AutoProcIntegration = relationship("AutoProcIntegration")


class GridInfo(Base):
    __tablename__ = "GridInfo"

    gridInfoId = Column(
        INTEGER(10), primary_key=True, comment="Primary key (auto-incremented)"
    )
    workflowMeshId = Column(
        ForeignKey(
            "WorkflowMesh.workflowMeshId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    xOffset = Column(Float(asdecimal=True))
    yOffset = Column(Float(asdecimal=True))
    dx_mm = Column(Float(asdecimal=True))
    dy_mm = Column(Float(asdecimal=True))
    steps_x = Column(Float(asdecimal=True))
    steps_y = Column(Float(asdecimal=True))
    meshAngle = Column(Float(asdecimal=True))
    recordTimeStamp = Column(
        TIMESTAMP,
        nullable=False,
        server_default=text("current_timestamp()"),
        comment="Creation or last update date/time",
    )
    orientation = Column(
        Enum("vertical", "horizontal"), server_default=text("'horizontal'")
    )
    dataCollectionGroupId = Column(
        ForeignKey("DataCollectionGroup.dataCollectionGroupId", ondelete="CASCADE"),
        index=True,
    )
    pixelspermicronX = Column(Float)
    pixelspermicronY = Column(Float)
    snapshot_offsetxpixel = Column(Float)
    snapshot_offsetypixel = Column(Float)

    DataCollectionGroup = relationship("DataCollectionGroup")
    WorkflowMesh = relationship("WorkflowMesh")


class PDBEntryHasAutoProcProgram(Base):
    __tablename__ = "PDBEntry_has_AutoProcProgram"

    pdbEntryHasAutoProcId = Column(INTEGER(10), primary_key=True)
    pdbEntryId = Column(
        ForeignKey("PDBEntry.pdbEntryId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    autoProcProgramId = Column(
        ForeignKey("AutoProcProgram.autoProcProgramId", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    distance = Column(Float)

    AutoProcProgram = relationship("AutoProcProgram")
    PDBEntry = relationship("PDBEntry")


class ParticlePicker(Base):
    __tablename__ = "ParticlePicker"
    __table_args__ = {
        "comment": "An instance of a particle picker program that was run"
    }

    particlePickerId = Column(INTEGER(10), primary_key=True)
    programId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    firstMotionCorrectionId = Column(
        ForeignKey(
            "MotionCorrection.motionCorrectionId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    particlePickingTemplate = Column(String(255), comment="Cryolo model")
    particleDiameter = Column(Float, comment="Unit: nm")
    numberOfParticles = Column(INTEGER(10))
    summaryImageFullPath = Column(
        String(255),
        comment="Generated summary micrograph image with highlighted particles",
    )

    MotionCorrection = relationship("MotionCorrection")
    AutoProcProgram = relationship("AutoProcProgram")


class ParticleClassificationGroup(Base):
    __tablename__ = "ParticleClassificationGroup"

    particleClassificationGroupId = Column(INTEGER(10), primary_key=True)
    particlePickerId = Column(
        ForeignKey(
            "ParticlePicker.particlePickerId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    programId = Column(
        ForeignKey(
            "AutoProcProgram.autoProcProgramId", ondelete="CASCADE", onupdate="CASCADE"
        ),
        index=True,
    )
    type = Column(
        Enum("2D", "3D"), comment="Indicates the type of particle classification"
    )
    batchNumber = Column(INTEGER(10), comment="Corresponding to batch number")
    numberOfParticlesPerBatch = Column(
        INTEGER(10), comment="total number of particles per batch (a large integer)"
    )
    numberOfClassesPerBatch = Column(INTEGER(10))
    symmetry = Column(String(20))

    ParticlePicker = relationship("ParticlePicker")
    AutoProcProgram = relationship("AutoProcProgram")


class ParticleClassification(Base):
    __tablename__ = "ParticleClassification"
    __table_args__ = {"comment": "Results of 2D or 3D classification"}

    particleClassificationId = Column(INTEGER(10), primary_key=True)
    particleClassificationGroupId = Column(
        ForeignKey(
            "ParticleClassificationGroup.particleClassificationGroupId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        index=True,
    )
    classNumber = Column(
        INTEGER(10), comment="Identified of the class. A unique ID given by Relion"
    )
    classImageFullPath = Column(String(255), comment="The PNG of the class")
    particlesPerClass = Column(
        INTEGER(10),
        comment="Number of particles within the selected class, can then be used together with the total number above to calculate the percentage",
    )
    classDistribution = Column(Float)
    rotationAccuracy = Column(Float)
    translationAccuracy = Column(Float, comment="Unit: Angstroms")
    estimatedResolution = Column(Float, comment="Unit: Angstroms")
    overallFourierCompleteness = Column(Float)

    ParticleClassificationGroup = relationship("ParticleClassificationGroup")


t_ParticleClassification_has_CryoemInitialModel = Table(
    "ParticleClassification_has_CryoemInitialModel",
    metadata,
    Column(
        "particleClassificationId",
        ForeignKey(
            "ParticleClassification.particleClassificationId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "cryoemInitialModelId",
        ForeignKey(
            "CryoemInitialModel.cryoemInitialModelId",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
        index=True,
    ),
)
