'''
Created on 12 juin 2013

@author: sdejonckheere
'''
import decimal
def to_decimal(float_price):
    return decimal.Decimal('%.6f' % float_price)