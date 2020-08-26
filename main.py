from emailutils import read_inbox
from emailutils import send_email


def main():
    credentials = open("configurations/credentials.txt", 'r').readlines()
    email_address, password = credentials[0], credentials[1]

    read_inbox.get_emails(email_address, password)


if __name__ == "__main__":
    main()
