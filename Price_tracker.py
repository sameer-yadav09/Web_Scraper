import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/MSI-Optix-MAG241C-Logitech-Keyboard/dp/B089BMPGNN/ref=sr_1_2?dchild=1&keywords=MSI+MAG241C&qid=1599711971&sr=8-2'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.154'}
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    print(title.strip()) #strip() used to eliminate white spaces.
    price = soup.find(id="priceblock_ourprice").get_text()
    print(price)
    cost = price.replace(',','')
    print(cost)
    converted_price= float(cost[2:8])
    print(converted_price)
    if(converted_price < 19000.0 ):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sender's email address', 'password')

    subject = 'You can afford it now!'
    body = 'link: https://www.amazon.in/CORSAIR-Vengeance-1x16GB-3200MHZ-Desktop/dp/B07W8ZDDKT/ref=bmx_1/260-6664605-9586114?_encoding=UTF8&pd_rd_i=B07W8ZDDKT&pd_rd_r=d012315a-acb2-41f5-8758-b5263d536376&pd_rd_w=inTlg&pd_rd_wg=INxqa&pf_rd_p=36ca7b19-4351-4ad5-b4ac-81d572158780&pf_rd_r=KWBJKD9NB6CE4X2SHQBE&psc=1&refRID=KWBJKD9NB6CE4X2SHQBE'
    msg= f"Subject: {subject}\n\n{body}"

    server.sendmail(
         'reciever's email address',
         'sender's email address',
         msg
    )
    print('Email sent!')
    server.quit()

if __name__ == '__main__':
    check_price()
