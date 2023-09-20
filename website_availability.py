import requests
import smtplib

website = ""
email = ""

try:
    response = requests.head(website)
    if response.status_code == 200:
        print("Website is up")
    else:
        message = "Website is down"
        subject = "Website Down Alert"
        server = smtplib.SMTP("smtp.yourprovider.com", 587)
        server.starttls()
        server.login("your@email.com", "your_password")
        server.sendmail(email, email, f"Subject: {subject}\n\n{message}")
        server.quit()
except requests.ConnectionError:
    print("Website is down")
