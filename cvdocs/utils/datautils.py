'''
Created on 20 nov. 2016

@author: roberto
'''

import logging
import sys
from collections import OrderedDict
from cvdocs.exception.exception import CVDOCSError

def sort_dictionary(dictionary,order_by='key',order='desc'):
    #TODO: check keywords parameters
    
    method_name = "sort_dictionary()"
    
    logging.info("Sorting dict ...")
    
    # Check the data type as dict
    if not isinstance(dictionary, dict):
        raise CVDOCSError(None,"Invalid dict as param", method_name)
    
    try:
                    
        # Which order?
        if order == 'desc':     
            reverse_order = True 
        else:
            reverse_order = False
            
        if order_by == 'key':
            d = OrderedDict(sorted(dictionary.items(),key=lambda t: t[0],reverse=reverse_order))
        else:
            d = OrderedDict(sorted(dictionary.items(),key=lambda t: t[1],reverse=reverse_order))
        
    except Exception:
        raise CVDOCSError(None,sys.exc_info()[0],method_name)
    
    logging.info("Ending sorting dict ...")
        
    return d

