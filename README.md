# calendly-notify-for-realtors

Scripts to handle Calendly confirmation emails for realtor showing schedules.

Example (`CalendlyNotify.get_calendly_events`):
```python
import datetime
output = [
    {'event-type': 'new event', 'event': '4082 W Rincon Avenue, Campbell 95008', 'datetime': datetime.datetime(2020, 8, 20, 11, 0)},
    {'event-type': 'delete', 'event': '4082 W Rincon Avenue, Campbell 95008', 'datetime': datetime.datetime(2020, 8, 20, 11, 30)},
    # ...        
    {'event-type': 'new event', 'event': '4082 W Rincon Avenue, Campbell 95008', 'datetime': datetime.datetime(2020, 8, 20, 3, 0)},
]
```

# Use
Simply edit the credentials in `configurations/credentials.txt` and run `main.py`. Logging is on by default.