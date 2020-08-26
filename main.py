from CalendlyNotify import CalendlyNotify


def main():
    credentials = open("configurations/credentials.txt", 'r').readlines()
    calendly = CalendlyNotify(credentials[0], credentials[1], log=True)
    calendly.get_calendly_events()


if __name__ == "__main__":
    main()
