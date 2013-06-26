import datetime

from dateutil.relativedelta import relativedelta
import pytz

# Define the weekday mnemonics to match the date.weekday function
( MON, TUE, WED, THU, FRI, SAT, SUN ) = range( 7 )

def AddWeek( dtDate , intWeek ):
    """
    Add intWeek weeks to dtDate
    """
    return dtDate + relativedelta( weeks = intWeek )

def AddQuarter( dtDate, intQuarter ):
    """
    Add intQuarter quarters to dtDate
    """
    return AddMonth( dtDate, 3 * intQuarter )

def AddDay( dtDate, intDay ):
    """
    Add intDay days to dtDate
    """
    return dtDate + relativedelta( days = intDay )

def AddMonth( dtDate, intMonth ):
    """
    Add intMonth months to dtDate
    """
    return dtDate + relativedelta( months = intMonth )

def AddYear( dtDate, intYear ):
    """
    Add intYear years to dtDate
    """
    return dtDate + relativedelta( years = intYear )

def BusinessDateAdd( start_date, work_days, whichdays = ( MON, TUE, WED, THU, FRI ) ):
    """
    Adds to a given date a number of working days 
    2009/12/04 for example is a friday - adding one weekday
    will return 2009/12/07
    >>> workdayadd(date(year=2009,month=12,day=4),1) 
    datetime.date(2009, 12, 7)
    """
    weeks, days = divmod( work_days, len( whichdays ) )
    new_date = start_date + datetime.timedelta( weeks = weeks )
    for i in range( days ):
        while new_date.weekday() not in whichdays:
            new_date += datetime.timedelta( days = 1 )
    return new_date

def HalfYearEnd( date ):
    """
    Returns the next half-year end after the specified date
    """
    if date.month() <= 6 :
        monthEnd = 6
        day = 30
    else:
        monthEnd = 12
        day = 31

    return datetime.date( date.year, monthEnd, day )

def GetStartOfMonth( date ):
    """
    Returns the 1st day of the month indicated by the specified date
    """
    return datetime.date( date.year, date.month, 1 )


def GetMidMonth( date ):
    """
    Returns the 15th day of the month indicated by the specified date
    """
    return datetime.date( date.year, date.month, 15 )

def GetEndOfMonth( date ):
    """
    Get the last day of the same month than the specified date
    """
    nextMonth = AddMonth( GetStartOfMonth(date), 1 )

    return datetime.date( nextMonth.year, nextMonth.month, 1 ) - datetime.timedelta( days = 1 )

def GetEndOfWeek( date ):
    """
    Get the last day of the same week than the specified date
    """
    newDate = date
    while newDate.weekday() != 5:
        newDate = AddDay( newDate, 1 )

    return newDate

def QuarterEnd( date ):
    """
    Get the last date of the quarter of the specified date
    """
    if date.month() <= 3 :
        monthEnd = 3
        day = 31
    elif date.month() <= 6 :
        monthEnd = 6
        day = 30
    elif date.month() <= 9 :
        monthEnd = 9
        day = 30
    else:
        monthEnd = 12
        day = 31

    return datetime.date( date.year, monthEnd, day )

def IsBusinessDay( date ):
    """
    Indicated if the date is in Monday to Friday
    """
    workingdays = ( MON, TUE, WED, THU, FRI )
    return not( IsHolidayDate( date ) ) and date.weekday() in workingdays

def IsHolidayDate( date ):
    """
    Returns true if the date is holiday.
    Not Yet Implemented, always returns False
    """
    return False

def GetNextBusinessDay( dtDate ):
    """
    Returns the business day next to the specified date
    """
    result = dtDate
    while not IsBusinessDay( result ):
        result = AddDay( result, 1 )

    return result

def GetNextOccurrenceFromList( dtDate, oCol ):
    """
    Returns the date next the the specified one in a given list
    """
    iMonth = dtDate.month

    result = dtDate
    for I in range( len( oCol ) ):
        if oCol[I] >= iMonth :
            result = GetEndOfMonth( datetime.date( dtDate.year, oCol[I], 1 ) )
            break

    return result

def Localize(dtDate):
    utc = pytz.UTC
    return utc.localize(dtDate)