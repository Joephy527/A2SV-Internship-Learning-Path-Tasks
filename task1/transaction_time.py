from datetime import datetime as dt


def get_time_of_transaction():
    datetime = str(dt.now())
    date, time = datetime[:10], datetime[11:]
    
    return (date, time)

if __name__ == "__main__":
    get_time_of_transaction()