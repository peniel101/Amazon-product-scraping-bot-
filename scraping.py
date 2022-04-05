import time
from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
import os

# getting the password , email and receiver from the environment variables
#get_password = os.environ.get("Password")
#get_email = os.environ.get("Email")
#receiver_email = os.enivron.get("receiver_email")

url = 'https://www.amazon.com/PlayStation-DualSense-Wireless-Controller-Starlight-Blue/dp/B09NLJGTHL/ref=sr_1_3?keywords=ps5+controller&qid=1641382163&sr=8-3'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


# A function to check the price of the product you want to buy
def check_price():
    
    time.sleep(2)
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, "lxml")

    product = soup.find(id="titleSection")
    product_name = product.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    desired_price = 60
    converted_price = float(price[1:])
    print(converted_price)
    # checking the price of the product
    if converted_price < desired_price:
        send_email()
    elif converted_price > desired_price:
        pass

    print(product_name)
    print(price)
    driver.quit()


# A function to send email to me if the price falls
def send_email():
    # the gmail port we are connecting to
    port = 587

    # creating a server with smptlib module
    server = smtplib.SMTP('smtp.gmail.com', port)
    # its kinda establish a connection to the email
    server.ehlo()

    server.starttls()
    server.ehlo()
    # user details and password
    user = get_email
    password = get_password
    # login into google using the  user and password
    server.login(user, password)
    subject = "The price of the PS5 controller has fell down"
    body = f"Check the ps5 controller here: \n {url}"

    message = f"Subject: {subject},\n\n{body} "
    # sending the email
    sender = user
    receiver = receiver_email
    server.sendmail(sender, receiver, message)
    server.quit()
    print("Hey, email sent!!!!")


check_price()