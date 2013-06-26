import datetime, time, logging

LOGGER = logging.getLogger( __name__ )

class StopWatch:
    """ StopWatch class used to monitor the time used to execute a part of code."""
    __watchName = None
    __startTime = None
    __stopTime = None
    __showStartAndStop = False

    def __init__( self, name, showStartStop = False ):
        self.__watchName = name
        self.__showStartAndStop = showStartStop

    def start( self ):
        """ Start the StopWatch to monitor the execution time."""
        self.__startTime = time.time()
        if self.__showStartAndStop:
            LOGGER.debug( "StopWatch [%s] has started at %s" % ( self.__watchName, datetime.datetime.fromtimestamp( self.__startTime ).strftime( "%d.%m.%y at %H:%M:%S" ) ) )

    def stop( self ):
        """ Stop the StopWatch."""
        self.__stopTime = time.time()
        if self.__showStartAndStop:
            LOGGER.debug( "StopWatch [%s] has stopped at %s" % ( self.__watchName, datetime.datetime.fromtimestamp( self.__stopTime ).strftime( "%d.%m.%y at %H:%M:%S" ) ) )

    def printStatus( self ):
        """ Print the status of the StopWatch after execution."""
        if self.__startTime == None:
            LOGGER.error( "StopWatch %s not started" % self.__watchName )
            return

        if self.__stopTime == None:
            self.stop()

        delta = self.__stopTime - self.__startTime
        LOGGER.debug( "StopWatch [%s] has ran during %s s" % ( self.__watchName, str( delta ) ) )
