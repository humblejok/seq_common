from seq_common.utils import emailing
import datetime
import sys
import socket
import traceback


def log_start_end_email(addressees):

    def caller(f):
        def wrapper(*args, **kwargs):
            failed = None
            result = None
            try:
                emailing.send_text_email(addressees, '[' + socket.gethostname() + '] ' + f.__name__ + ' started at ' + str(datetime.datetime.today()), '')
            except:
                None
            try:
                result = f(*args, **kwargs)
            except Exception as e:
                failed = e
            try:
                if failed==None:
                    emailing.send_text_email(addressees, '[' + socket.gethostname() + '] ' + f.__name__ + ' ended at ' + str(datetime.datetime.today()), '')
                else:
                    emailing.send_text_email(addressees, '[' + socket.gethostname() + '] ' + f.__name__ + ' FAILED at ' + str(datetime.datetime.today()), str(failed))
                    traceback.print_exc()
            except:
                None
            return result
        return wrapper
    return caller