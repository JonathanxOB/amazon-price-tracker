import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/R%C3%98DE-Microphones-WAVE-Wireless-400836009/dp/B08XFQ6KP9/ref=sr_1_5?crid=3C5C9TF6O90UO&keywords=rode%2Bmicrophone%2Bwireless&qid=1700087368&sprefix=rode%2Bmicrophone%2B%2Caps%2C112&sr=8-5&ufe=app_do%3Aamzn1.fos.23648568-4ba5-49f2-9aa6-31ae75f1e9cd&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find('span', class_={"a-price-whole"}).get_text()
    converted_price = float(price[0:5])

    if(converted_price <  235):
        send_mail()

    print(converted_price)
    print(title.strip())

# Clause to trigger the email
    if(converted_price < 235):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # ehlo - this is a command send by an command sent by an email server to identify itself when connecting to another email
    server.ehlo()
    # starttls encrypts our connection
    server.starttls()
    server.ehlo()

    server.login('jonathanowusu1297@gmail.com','akzi yern fjpl fids')

    subject = 'Hey, the price just fell! Don\'t miss this!'
    body = 'Check out the amazon link - https://www.amazon.co.uk/R%C3%98DE-Microphones-WAVE-Wireless-400836009/dp/B08XFQ6KP9/ref=sr_1_5?crid=3C5C9TF6O90UO&keywords=rode%2Bmicrophone%2Bwireless&qid=1700087368&sprefix=rode%2Bmicrophone%2B%2Caps%2C112&sr=8-5&ufe=app_do%3Aamzn1.fos.23648568-4ba5-49f2-9aa6-31ae75f1e9cd&th=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'jonathanowusu1297@gmail.com',
        'jonoudriver@gmail.com',
        msg
    )
    print('Hey, this email has been sent!')

    server.quit()

# check email once every hour (seconds)
while(True):
    check_price()
    time.sleep(3600)
