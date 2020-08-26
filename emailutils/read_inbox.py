import email
import imaplib


def get_emails(email_address, password, only_select_unread=True, read_receipt=False, *, log=False):
    emails_list = []  # list of email objects to return

    # connect to the server and go to its inbox
    server = imaplib.IMAP4_SSL('imap.gmail.com')  # port 993

    server.login(email_address, password)
    server.select('Inbox', readonly=(not read_receipt))

    # search using ALL criteria, get all unread messages
    # (data is list of uids)
    status, data = server.search(None, '(UNSEEN)' if only_select_unread else 'ALL')

    # extract mail_ids
    mail_ids = []
    for block in data:
        mail_ids += block.split()  # b'1 2 3'.split() => [b'1', b'2', b'3']

    # extract each email and contents
    for i in mail_ids:
        # the fetch function fetch the email given its id and format
        status, data = server.fetch(i, '(RFC822)')

        # '(RFC822)' => a list with a tuple with header, content, and the closing byte b')'
        for response_part in data:
            # so if its a tuple...
            if isinstance(response_part, tuple):
                # use SECOND element (header is first and closing is last)
                message = email.message_from_bytes(response_part[1])

                mail_from = message['from']
                mail_subject = message['subject']

                # PLEASE SEE MasonWang025/mailing-client-python for extracting content from emails

                emails_list.append({
                    "from": mail_from,
                    "subject": mail_subject,
                })

                if log:
                    log_subject = (mail_subject[:21] + '..') if len(mail_subject) > 21 else mail_subject
                    print(f'Adding [{log_subject}] (from {mail_from}).')

    return emails_list
