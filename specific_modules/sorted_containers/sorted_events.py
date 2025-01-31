from sortedcontainers import SortedDict
from datetime import datetime

# Create a SortedDict containing event names and their dates
event_dates = SortedDict(
    {
        "Concert": "2023-06-21",
        "Conference": "2023-07-12",
        "Seminar": "2023-06-11",
        "Workshop": "2023-08-05",
    }
)

# TODO: Write logic to find and display the name of the event that is scheduled immediately after 'Seminar'
dates_events = {
    datetime.strptime(date, "%Y-%m-%d"): event for event, date in event_dates.items()
}
sd_dates_events = SortedDict(dates_events)
for i in range(len(sd_dates_events)):
    if sd_dates_events.peekitem(i)[1] == "Seminar":
        next_event = sd_dates_events.peekitem(i + 1)
        next_event = (next_event[0].strftime("%Y-%m-%d"), next_event[1])
        print(next_event)
