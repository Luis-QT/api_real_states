""" File to connect PostgreSQL Database """
import os
import sqlalchemy
from app.db import BasePsql, Session

def build_uri():
    """ Build Database URI Postgres """
    uri_psql = str("")
    
    if os.environ['APP_MODE'] in ['development', 'staging']:
        uri_psql = str("postgresql://{user}:{password}@{host}:{port}/{database}").format(
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            host="db_template",
            port=os.environ['POSTGRES_PORT'],
            database=os.environ['POSTGRES_DB']
        )
    elif os.environ['APP_MODE'] == 'production':
        uri_psql = str("postgresql://{user}:{password}@{host}:{port}/{database}").format(
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            host="psql-integrador",
            port=os.environ['POSTGRES_PORT'],
            database=os.environ['POSTGRES_DB']
        )
    return uri_psql

def refresh_db():
    """ Function that reset the database. Resets models and seeders """
    from app.db.seeders import run_seeds # pylint: disable=import-outside-toplevel
    BasePsql.metadata.drop_all(bind=engine)
    BasePsql.metadata.create_all(bind=engine)
    db = Session(bind=engine)
    try:
        run_seeds(db=db)
    finally:
        db.close()

def get_db():
    """ Dependency that generates a session instance """
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

engine = sqlalchemy.create_engine(build_uri())
BasePsql.metadata.create_all(bind=engine)
