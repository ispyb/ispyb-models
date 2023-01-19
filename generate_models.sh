#! /bin/bash

sqlacodegen mysql+mysqlconnector://test:test@127.0.0.1/ispyb_build --nojoined --noinflect --outfile src/ispyb/models/_auto_db_schema.py
black src/ispyb/models/_auto_db_schema.py
patch -p1 src/ispyb/models/_auto_db_schema.py < patches/models.patch
rm src/ispyb/models/_auto_db_schema.py.orig