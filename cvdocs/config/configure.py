'''
Created on 2 sept. 2016

@author: roberto
'''

import yaml
from cvdocs.exception.exception import ConfigError
import sys
import traceback

class Configure(object):
    """ 
        Class which constains the configuration file parameters. There will exists just one instance of this class.
    
    """
    
    __CONFIG_FILE_PATH = 'config/config.yaml'
    
    __instance = None
    config_params = {}
    def __new__(cls):
        if Configure.__instance is None:
            Configure.__instance = object.__new__(cls)
        return Configure.__instance
    
    def load_config(self):
        
        method_name = "load_config()"
        
        try:        
            with open(self.__CONFIG_FILE_PATH, 'r') as stream:
                conf = yaml.load(stream)
            
            Configure.__instance.config_params = conf
        except IOError:
            raise ConfigError(self,"No such config file '%s'" %(self.get_config_path()),method_name)
        except yaml.scanner.ScannerError:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback ,limit=5, file=sys.stdout)
            raise ConfigError(self,"Incorrect config file '%s'" %(self.get_config_path()),method_name)
        except Exception:
            raise ConfigError(self,sys.exc_info()[0],method_name)
        
    def get_config(self):
        return Configure.__instance.config_params
    
    def get_config_path(self):
        return self.__CONFIG_FILE_PATH
    