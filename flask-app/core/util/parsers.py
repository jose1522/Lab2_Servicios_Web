from datetime import datetime

def timestampToDate(input):
    try:
        ts = datetime.strptime(input, "%Y-%m-%dT%H:%M:%SZ")
        return datetime.date(ts)
    except:
        return None
