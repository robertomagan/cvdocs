# -*- coding: utf-8 -*-
"""
    :mod:`Error definitions module`
    ===========================================================================
    :synopsis: Contains the description and definitios of every kind of error (exception) that could be raised
    :author: NESG (Network Engineering & Security Group)
    :contact: rmagan@ugr.es
    :organization: University of Granada
    :project: cvdocs
    :since: 0.0.1  
"""
class CVDOCSError(Exception):
    """
        
    *General error definition*
        
    Attributes
    ----------
    _obj: object
        instance of the class which raises the exception
    _msg: str
        error message
    _method: str
        method name where the error is raised    
         
    See Also
    --------
    Exception
    """      
    
    def __init__(self, obj, message='',method=''):
        self._obj = obj
        self._msg = message
        self._method = method
        
    def print_error(self):
        """
            Print the error in a specific format
        """
        
        if not self._obj:
            object_class = ''
        else:
            object_class = self._obj.__class__
        
        print("ERROR: %s, Type: %s, Method: %s" %(self._msg,object_class,self._method))
        
    def get_msg(self):
        return self._msg
    
    def get_method(self):
        return self._method
    
    def get_obj(self):
        return self._obj
        

class ConfigError(CVDOCSError):
    """        
    *Error definition related to the configuration issues*
         
    See Also
    --------
    cvdocs.exception.CVDOCSError
    """
    pass