from seq_common.utils import emailing
import datetime
import sys
import socket


def log_start_end_email(addressees):

    def caller(f):
        def wrapper(*args, **kwargs):
            emailing.send_text_email(addressees, f.__name__ + ' started at ' + str(datetime.datetime.today()) + ' on ' + socket.gethostname(), '')
            f(*args, **kwargs)
            emailing.send_text_email(addressees, f.__name__ + ' ended at ' + str(datetime.datetime.today()) + ' on ' + socket.gethostname(), '')
        return wrapper
    return caller