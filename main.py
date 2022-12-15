from bs4 import BeautifulSoup
import requests
import smtplib
import datetime
from datetime import date

dt = datetime.datetime


def email_send(price_updated):
    my_email = "shlomo.python@yahoo.com"
    password = "m??????????n"
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="pythons.hlomo39@gmail.com"
                            , msg=f"Subject:price change alert\n\n,updated price today {price_updated}$")


url = "https://www.amazon.com/Multi-Functional-Safety-Features-Multicooker-Sterilizer-Measuring/dp/B09YL5YK35/ref" \
      "=sr_1_2_sspa?adgrpid=80697925159&gclid=CjwKCAiAv9ucBhBXEiwA6N8nYKPsfhtlEqtiNTQv27HPM6kS" \
      "-obLmJpr1SudCeo_GpZ0CXit3nx7qhoCXNgQAvD_BwE&hvadid=585479455916&hvdev=c&hvlocint=9073366&hvlocphy=1007973&hvnetw" \
      "=g&hvqmt=b&hvrand=38209899233239390&hvtargid=kwd-822047725126&hydadcr=22367_13333092&keywords=instant+pot+duo" \
      "+evo+plus&qid=1670837144&sr=8-2-spons&psc=1&spLa" \
      "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQUlWTjNDQldISEgxJmVuY3J5cHRlZElkPUEwOTg2ODQ5MTlENVgxS0hYWUVGNiZlbmNyeXB0ZWRBZElkPUEwNDMyMjUyTTVRUE5BWTlBQUZSJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ== "
url_past = "https://www.amazon.com/Instanut-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463&th=1"
url_new_egg = "https://www.newegg.com/p/N82E16824012046"
headers = {'Accept-Language': 'he,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'}
response = requests.get(url=url, headers=headers)
data = response.text
soup = BeautifulSoup(data, 'lxml')

price_search = int(soup.find(class_='a-price-fraction').text)
print(price_search)
x = dt.now()
print(x.strftime("%H %M"))
while x.strftime("%H %M") != 17.33:  # once a day searching process...
    if price_search < 99:
        email_send(price_search)
        print(f"PRICE UPDATING !! {price_search}")
        break


 
