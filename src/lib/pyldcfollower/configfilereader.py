import os
import json


class ConfigFileReader(object):

    ConfigFileEnvVariableName = 'LDC_FOLLOWER_CONFIG_FILE_PATH'

    DefaultConfigFile = '~/.ldcfollower.json'

    def __init__(self):
        self.config = None
        self.dbname = None

    def read(self):

        if self.ConfigFileEnvVariableName in os.environ:
            config_file_path = self.ConfigFileEnvVariableName
        else:
            config_file_path = self.DefaultConfigFile

        assert os.path.exists(config_file_path), \
            "Don't see ldc follower config file at %s. Default location is %s, or use %s to set." % \
            (config_file_path, self.DefaultConfigFile, self.ConfigFileEnvVariableName)

        with open(config_file_path, 'rt') as fid:
            self.config = json.load(fid)

        assert 'dbname' in self.config, "Missing 'dbname' in config json."

        assert 'host' in self.config, "Missing 'host' in config json."

        assert 'port' in self.config, "Missing 'port' in config json."

        assert 'user' in self.config, "Missing 'user' in config json."

        assert 'password' in self.config, "Missing 'password' in config json."

        return self

    def get_connection_string(self):
        conn = ''

        for key in self.config:
            conn += '%s=%s' % (key, self.config[key])

        return conn






