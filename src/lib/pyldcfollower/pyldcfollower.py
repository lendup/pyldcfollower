import psycopg2

from .configfilereader import ConfigFileReader


__all__ = ['LdcFollowerConnection']


class LdcFollowerConnection(object):

    class __FollowerConnection(object):
        connect_str = ConfigFileReader().read().get_connection_string()
        _connection = None

        try:
            _connection = psycopg2.connect(connect_str)

        except Exception as err:
            print("Error encountered. I cannot connect to database:")
            print(err.message)

    instance = None

    def __init__(self):
        if LdcFollowerConnection.instance is None:
            LdcFollowerConnection.instance = LdcFollowerConnection.__FollowerConnection()
            assert LdcFollowerConnection.instance is not None, "No connection created."

    def connection(self):
        assert self.instance._connection is not None, "No database connection."
        return self.instance._connection

    def cursor(self):
        assert self.instance._connection is not None, "No database connection."
        return self.instance._connection.cursor()
