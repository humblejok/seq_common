from seq_common.utils import emailing
import datetime
import sys
import socket


def log_start_end_email(addressees):

    def caller(f):
        def wrapper(*args, **kwargs):
            try:
                emailing.send_text_email(addressees, f.__name__ + ' started at ' + str(datetime.datetime.today()) + ' on ' + socket.gethostname(), '')
            except:
                None
            f(*args, **kwargs)
            try:
                emailing.send_text_email(addressees, f.__name__ + ' ended at ' + str(datetime.datetime.today()) + ' on ' + socket.gethostname(), '')
            except:
                None
        return wrapper
    return caller