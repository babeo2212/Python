def sending_email(receiver, subject, content, attachment_link=0):    
    '''
    - receiver: test@gmail.com
    - subject: string
    '''
    import os
    import smtplib, ssl
    import imghdr
    from email.message import EmailMessage # set email message
    from tkinter import filedialog

    EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
    EMAIL_PASS = os.environ.get('EMAIL_PASS')

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    
    msg['To'] = receiver
    

    msg.set_content(content)

    try:
        with open(attachment_link, 'rb') as f:
            file = f.read()
            file_type = imghdr.what(f.name) # get image type 
            file_name = f.name #get image name

        msg.add_attachment(file, maintype = 'image', subtype = file_type, filename=file_name)
    except Exception:
        pass 


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
    ## OR: 
    # with smtplib.SMTP('smtp.gmail.com', 587) as smtp: 
        # smtp.ehlo() # identify ourselve with the mail server we are using (automatically)
        # smtp.starttls() # encrsmtplib.SMTPypt the traffic
        # smtp.ehlo() # reidentify

        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        try:
            smtp.send_message(msg) # sendmail(SENDER, RECIEVER, msg)
        except Exception as err:
            print(err, 'Please enter properly. Please enter again.')
    
    
    print('All Done.')

if __name__=='__main__':
    receiver = input('Please enter email address: ')
    subject = input('Please enter Mail Subject: ')
    content = input('Please enter Mail Content: ')
    attachment_link = input('(If available) Please enter links located in your PC.')
    sending_email(receiver, subject, content, attachment_link)