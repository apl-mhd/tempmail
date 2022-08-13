import imaplib
import email
# imap_server = imaplib.IMAP4(host='mail.mykitchengossip.com')
# imap_server.login('test@mykitchengossip.com', 'NS18n-VNkvv.')

host = 'mail.mykitchengossip.com'
username = 'test@mykitchengossip.com'
password = 'NS18n-VNkvv.'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)

mail.select("inbox")

_, search_data = mail.search(None, 'ALL')


for num in search_data[0].split():
    _, data = mail.fetch(num, 'RFC822')
    
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    
    for header in ['subject', 'to', 'from', 'date']:
        print("{}: {} ". format(header, email_message[header]))
    
    for part in email_message.walk():
        if part.get_content_type() == "text/html":
            body = part.get_payload(decode=True).decode()
            final_content = body.replace('dir="ltr"', "")
            print(f'Email Body: {final_content}')








