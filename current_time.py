import datetime

def get_time():
# def get_time(milli=True, sep='-', utc=True):
  # now = datetime.utcnow() if utc else datetime.now()
  now = datetime.datetime.now()
  # return now.strftime('%Y%m%d{deli}%H%M%S{milli}'.format(deli=sep, milli='_%f' if milli else ''))
  
  return now
  # return now.strftime("%d-%m-%Y %H:%M")
  # note_entry.append(now.strftime("%d-%m-%Y %H:%M"))
