from datetime import datetime

def current_date():
    return datetime.now().strftime("%d-%m-%Y")

def current_time():
    return datetime.now().strftime("%I:%M:%S %p")