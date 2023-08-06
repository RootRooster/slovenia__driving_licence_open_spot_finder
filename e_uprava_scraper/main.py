from e_uprava_scraper.spiders.a_category_scraper import ACategoryScraperSpider
from scrapy.crawler import CrawlerProcess
from email.message import EmailMessage
import smtplib
import ssl
import os

def send_email(location, time):
    sender_email = 'kokiparot@gmail.com'
    email_password = os.getenv('APP_PASSWORD')
    reciever_email = input('Enter your email: ')
    subject = 'NEW OPEN SPOT ON E-UPRAVA'

    body = f'''
                There is a new open spot in {location} at {time}.
            '''
    
    email_msg = EmailMessage()
    email_msg['From'] = sender_email
    email_msg['To'] = reciever_email
    email_msg['Subject'] = subject
    email_msg.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, email_password)
        smtp.sendmail(sender_email, reciever_email, email_msg.as_string())
    
    print('An email has been sent!')



def main():
    process = CrawlerProcess()
    process.crawl(ACategoryScraperSpider)
    process.start()


    

if __name__ == '__main__':
    main()
