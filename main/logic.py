import threading, smtplib, random
import time, re
from .models import Emails, Contacts, Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta



def sender():
    while True:

            
        now = datetime.now()
        weekday = now.weekday()
        hour = now.hour

        if 0 <= weekday <= 4:  
            if 8 <= hour < 16:

                wait_seconds = random.randint(300, 600)
                print(f"Waiting {wait_seconds//60} minit and {wait_seconds%60} second 4 next email.")
                time.sleep(wait_seconds)
            else:
                # aft 16
                if hour >= 16:
                    next_day = now + timedelta(days=1)
                else:
                    # bfr 8:00
                    next_day = now

                # OTHER DAY WEEKEND
                if next_day.weekday() >= 5:
                    days_until_monday = (7 - now.weekday()) % 7
                    if days_until_monday == 0:
                        days_until_monday = 1  
                    next_start = (now + timedelta(days=days_until_monday)).replace(hour=8, minute=0, second=0, microsecond=0)
                else:
                    next_start = next_day.replace(hour=8, minute=0, second=0, microsecond=0)

                sleep_seconds = (next_start - now).total_seconds()
                print(f"Waiting for the work day {next_start} ({int(sleep_seconds/60/60)} hours).")
                time.sleep(sleep_seconds)
        else:
            # weekend = til Mon - 8:00
            days_until_monday = (7 - weekday) % 7
            if days_until_monday == 0:
                days_until_monday = 1
            next_start = (now + timedelta(days=days_until_monday)).replace(hour=8, minute=0, second=0, microsecond=0)
            sleep_seconds = (next_start - now).total_seconds()
            print(f"Waiting till Monday 8:00 ({int(sleep_seconds/60/60)} hours).")
            time.sleep(sleep_seconds)

            
        for x in Emails.objects.all():
            y = Contacts.objects.filter(contacted = False, user=x.user ).first()
            try:
                g = Message.objects.filter(user=x.user,name=y.message).first()
                print(f"adressa:{y.name}")
                print(f"subject:{g.subject}")
                try:
                    msg = re.sub(r'\bSUBJECT\b', y.name, g.message)
                    msg = re.sub(r'\bCOMPANY\b', y.company, msg)
                except:
                    msg = g.message
                print(f"msg:{msg}")
                # print(x.user,g.name,g.message,y.company)
                # print(Message.objects.first().user)
                HOST = x.host
                port = x.port
                fromE = x.email

                # fromE = toE
                passwo = x.token
                eml = MIMEMultipart("alternative")
                eml["Subject"] = g.subject
                eml["From"] = fromE

                eml["To"]= y.email
                eml["Cc"] = fromE
                eml["Bcc"] = fromE


                eml.attach(MIMEText(f'<p>{msg}</p>', 'html'))
                #file sending

                #error kodiky
                smtp = smtplib.SMTP(HOST, port)
                status_code, response = smtp.ehlo()
                print(f"echoing: {status_code}, {response}")

                status_code, response = smtp.starttls()
                print(f"tls:{status_code} {response}")


                status_code, response = smtp.login(fromE, passwo)
                print(f"loging:{status_code} {response}")

                smtp.sendmail(fromE, y.email, eml.as_string())
                smtp.quit()
                y.contacted = True
                y.save()
            except smtplib.SMTPAuthenticationError as e:
                print("AUT error:", e)
            except smtplib.SMTPException as e:
                print("SMTP error:", e)
            except Exception as e:
                print("Other error:", e)

        print("Sending e-mails...")



def start_sender_thread():
    thread = threading.Thread(target=sender, daemon=True)
    thread.start()