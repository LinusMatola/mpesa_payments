from datetime import datetime

def get_timestamp():
    unformated_time = datetime.now()
    formated_time = unformated_time.strftime("%Y%m%d%H%M%S")

    return formated_time