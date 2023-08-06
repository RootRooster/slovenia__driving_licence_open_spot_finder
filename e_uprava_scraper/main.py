from e_uprava_scraper.spiders.a_category_scraper import ACategoryScraperSpider
from scrapy.crawler import CrawlerProcess
from email.message import EmailMessage
import pandas as pd
from time import sleep
import smtplib
import csv
import ssl
import os

def send_email(reciever_email, location, date, time):
    sender_email = 'kokiparot@gmail.com'
    email_password = os.getenv('APP_PASSWORD')
    subject = 'NEW OPEN SPOT ON E-UPRAVA'

    body = f'''There is a new open spot in {location} on {date} at {time}.'''
    
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



def clear_data():
    # clear the data.csv file
    with open('data.csv', 'w') as f:
        f.write('')

def process_data():
    # process the data
    df = pd.read_csv('data.csv', header=0)
    df['date'] = pd.to_datetime(df['date'], format='%d. %m. %Y')
    df = df.sort_values('date', ascending=True)
    first_row = df.iloc[0]
    first_location, first_date, first_time = first_row['location'], first_row['date'], first_row['time']
    return first_location, first_date, first_time

def main():
    best_date = None
    reciever_email = input('Enter your email: ')
    while(True):
        clear_data()
        process = CrawlerProcess()
        process.start()
        process.crawl(ACategoryScraperSpider)
        sleep(10)
        location, date, time = process_data()
        if best_date is None:
            best_date = date
            send_email(reciever_email, location, date, time)
        elif best_date > date:
            best_date = date
            send_email(reciever_email, location, date, time)
                


    

if __name__ == '__main__':
    main()
