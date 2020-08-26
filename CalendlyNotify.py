from emailutils import read_inbox
from emailutils import send_email
from datetime import datetime


class CalendlyNotify:
    def __init__(self, email, password, log=False):
        self.log = log
        self.email = email.strip()
        self.password = password.strip()
        self.calendly_events = []

    def get_calendly_events(self):
        subjects = self.get_calendly_emails()
        for subject in subjects:
            calendly_event = {}
            parts = subject.split("-")
            calendly_event["event"] = parts[0].split(":")[0].strip().lower()
            calendly_event["datetime"] = datetime_from_calendly_str(parts[1].strip())
            calendly_event["event"] = parts[2].strip().replace("\n", "").replace("\r", "")
            self.calendly_events.append(calendly_event)
        print(self.calendly_events)

    def update_event(self, event_name, new_datetime_object, old_datetime_object):
        self.delete_event(old_datetime_object)

    def delete_event(self, datetime_object):
        self.calendly_events = list(filter(lambda e: e.datetime.date() != datetime_object.date(), self.calendly_events))

    def get_calendly_emails(self):
        emails_list = read_inbox.get_emails(self.email, self.password, log=self.log)
        subjects = []
        for mail in emails_list:
            if "notifications@calendly.com" in mail["from"]:
                subjects.append(mail["subject"])

        return subjects


def datetime_from_calendly_str(calendly_str):
    return datetime.strptime(calendly_str.strip(), '%H:%M%p %a, %b %d, %Y')
