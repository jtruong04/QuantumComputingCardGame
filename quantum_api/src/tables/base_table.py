# base table
import src
from sqlalchemy import func
from sqlalchemy import update


db = src.db


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


class base_table():

    @classmethod
    def get(cls, target):
        """ Method which returns the instance where primary key == target

        Args:
            target (flexible): primary key of target information.
        Return:
            Database column associated with primary key, if exists, else None.
        """
        session = db.session
        query = session.query(cls)
        result = query.get(target)
        return result

    @classmethod
    def getAll(cls):
        """ Method which returns all elements of database table
        Returns:
            All entries in table
        """
        session = db.session
        query = session.query(cls).all()
        return query

    @classmethod
    def post(cls, to_post):
        session = db.session
        session.add(to_post)
        session.commit()
        return to_post

    @classmethod
    def patch(cls, primary, new_values):
        session = db.session
        query = session.query(cls)
        result = query.get(primary)
        for key in new_values:
            setattr(result, key, new_values[key])
        session.commit()
        return result

    @classmethod
    def delete(cls, target):
        session = db.session
        query = session.query(cls)
        result = query.get(target)
        session.delete(result)
        return session.commit()

    @classmethod
    def count(cls):
        session = db.session
        query = session.query(func.count('*'))
        return query