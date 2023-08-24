import requests
from bs4 import BeautifulSoup
import smtplib

YOUR_EMAIL = 'EMAIL'
YOUR_PASSWORD = 'ПАРОЛЬ'
YOUR_SMTP_ADDRESS = 'SMTP'
BUY_PRICE = 130

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?dchild=1&keywords=instant+pot&qid=1597660904&sr=8-4"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < BUY_PRICE:
    message = f"{title} сейчас {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Низкая цена на!\n\n{message}\n{url}")



