This provides a set of [SQLAlchemy](https://www.sqlalchemy.org/) ORM models for the [ISPyB database](https://github.com/ispyb/ispyb-database/).

## Installation

Install from pypi [ispyb-models](https://pypi.org/project/ispyb-models):

```bash
pip install ispyb-models
```

## Basic Usage

```python
from ispyb import models

dataCollection = models.DataCollection(
    ...
)

ses.add(dataCollection)
ses.commit()

...

datacollections = (
    ses.query(
        models.DataCollection
    ).filter(models.DataCollection.dataCollectionId == 1)
    ).first()
)
```

## Generate a new version

To update the models you need to run the workflow `Update Models` through GitHub Actions panel.
This will create a new branch with models matching the latest DB release and create a pull request for merge this branch into main. Before merging there are some things you need to do:

-   Make sure py-ispyb tests still pass with these new models
-   Update `HISTORY.md` to reflect the changes
-   Bump version number with `bump2version`

### ⚠️ Do not edit the output file yourself

**The resulting `_auto_db_schema.py` should not be edited** (other than automatic
formatting with `black` or sorting of imports with `isort`). All models are imported
into and accessed via the `__init__.py`. Any modifications, e.g. injecting additional
relationships between models should be done here.

### ⚠️ _[for local test]_ Manually update the DB schema

Checkout the specific tag for a given `ispyb-database` version:

```bash
$ git clone -b v1.18.1 https://github.com/ispyb/ispyb-database.git
$ # or, if you have an existing copy of the repository:
$ git checkout v1.18.1
```

Apply the schema patch in `patches/circular_references.patch` to avoid circular foreign key references:

```bash
$ patch -p1 < ispyb-models/patches/circular_references.patch
```

Then run the `ispyb-database` `build.sh` script to generate the database:

```bash
$ sh build.sh
```

Generate the models with [sqlacodegen](https://pypi.org/project/sqlacodegen/)
in `src/ispyb/models/`:

```bash
. generate_models.sh
```
