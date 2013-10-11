'''
Created on Oct 3, 2013

@author: sdejonckheere
'''
def modified_dietz(values, cashflows):
    cashflow_sum=0.0
    cashflow_weighted=0.0
    period_start = values['start_date'].timetuple().tm_yday
    period_end = values['end_date'].timetuple().tm_yday
    period_length = period_end - period_start
    for cashflow in cashflows:
        cashflow_sum += cashflow['value']
        cashflow_weighted += cashflow['value'] * float(period_end-cashflow['date'].timetuple().tm_yday)/float(period_length)
    if values['start_value']+cashflow_weighted==0.0: 
        return 0.0
    else:
        return (values['end_value'] - values['start_value'] - cashflow_sum)/(values['start_value'] + cashflow_weighted)