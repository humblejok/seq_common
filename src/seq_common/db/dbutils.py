'''
Created on June 12, 2013

@author: sdejonckheere
'''

from django.db import connections
from django.db.utils import DEFAULT_DB_ALIAS
from itertools import izip
import logging
import sys


# Get an instance of a logger
LOGGER = logging.getLogger( __name__ )

def NullValue(dbValue, defaultValue):
    """ 
    Return the dbValue if not null, or the default value instead
    """
    if dbValue is None:
        return defaultValue
    
    return dbValue

def DbDate(dbValue):
    """ 
    Format a python's date or datetime to Oracle DBDate value used in an sql query. Exemple of result: to_date('21/02/2011', 'DD/MM/YYYY')
    """
    try:
        fDate = dbValue.strftime('%d/%m/%Y')
        fValue = 'to_date(\'{0}\', \'DD/MM/YYYY\') '.format(fDate)
    except:
        print "Unexpected error:", sys.exc_info()[1]
        raise
    
    return fValue

def query_to_dicts(query_string, query_connection_id=DEFAULT_DB_ALIAS,*query_args ):    
    """
    Run a simple query and produce a generator    
    that returns the results as a bunch of dictionaries    
    with keys for the column values selected.    
    """
    
    LOGGER.debug(query_string)
    try:
        connection = connections[query_connection_id]
        cursor = connection.cursor()
        cursor.execute(query_string, *query_args)    
        col_names = [desc[0] for desc in cursor.description]
        
        while True:
            row = cursor.fetchone()
            
            if row is None:
                break
    
            row_dict = dict(izip(col_names, row))
            yield row_dict
    except GeneratorExit:
        #GeneratorExit should not logged has an error.
        pass
    except:
        import traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        exceptionStr = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        LOGGER.error("Error when executing query: %s. \nReason:%s" % (query_string, exceptionStr))
        
    return

