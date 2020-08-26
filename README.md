# calendly-notify-for-realtors

Scripts to handle Calendly confirmation emails for realtor showing schedules. 

**Calendly does not support *bcc*, thus exposing buyer and seller contact information. The code here solves this by allowing extraction of information and automated notifications.**

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
Simply edit the credentials in `configurations/credentials.txt` and run `main.py`. See [MasonWang025/mailing-client-python](https://github.com/MasonWang025/mailing-client-python) for more information regarding setting up email access through IMAP. 

Logging is on by default, so code structure and flow should be apparent after a first run.
