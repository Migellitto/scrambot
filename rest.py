from datetime import datetime, timedelta

def get_month():
    today = datetime.now()
    first = today.replace(day=1)
    return [int(datetime.now().month), int((first - timedelta(days=1)).strftime("%m"))]

# print(get_month())