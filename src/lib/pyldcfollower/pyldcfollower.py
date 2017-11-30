import psycopg2

from .configfilereader import ConfigFileReader


__all__ = ['LdcFollowerConnection']


class LdcFollowerConnection(object):

    class __FollowerConnection(object):
        connect_str = ConfigFileReader().read().get_connection_string()
        _connection = None

        try:
            _connection = psycopg2.connect(connect_str)
        except:
            print "I cannot connect to database."

    instance = None

    def __init__(self):
        if LdcFollowerConnection.instance is None:
            LdcFollowerConnection.instance = LdcFollowerConnection.__FollowerConnection()

    def get_connection(self):
        return self.instance._connection

    def get_cursor(self):
        return self.instance._connection.cursor()
