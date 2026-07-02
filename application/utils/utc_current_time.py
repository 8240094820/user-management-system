import pytz
from datetime import datetime


def UTC_current_time():
    utc_timezone = pytz.timezone("UTC")
    current_time  = datetime.now(utc_timezone)
    current_time = current_time.replace(tzinfo=None)
    return current_time

def convert_datetime(login_date):
    if login_date:
        return login_date.strftime("%m-%d-%Y %H:%M:%S")
    return ''