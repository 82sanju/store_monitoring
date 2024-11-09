import pandas as pd
from datetime import datetime
import pytz

def calculate_uptime_downtime(store_data, business_hours, timezone_str):
    # Logic to calculate uptime/downtime using interpolation
    pass

def convert_to_local_time(utc_time, timezone_str):
    local_tz = pytz.timezone(timezone_str)
    utc_time = utc_time.replace(tzinfo=pytz.utc)
    local_time = utc_time.astimezone(local_tz)
    return local_time
