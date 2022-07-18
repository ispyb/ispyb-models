from ispyb import models


def test_models_retrieve(session):
    datacollection = (
        session.query(models.DataCollection)
        .filter(models.DataCollection.dataCollectionId == 1)
        .first()
    )

    assert datacollection


def test_model_insert(session):
    protein = models.Protein(proposalId=1, name="test", acronym="test")

    session.add(protein)
    session.commit()

    assert protein.proteinId
