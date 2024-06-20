from scraper import scrape_timetable
from send_email import send_email
from helpers import *

# email parameters
sender_email = 'x@gmail.com'
receiver_email = 'x@gmail.com'
password = 'kodas'
subject = 'Teniso Rezervacijos. Automatines'
log_file = 'seen_values.log'

# scraping parameters
url = 'https://book.sebarena.lt/?_ga=2.117973065.1966334876.1713010607-2100705733.1713010607#/rezervuoti/tenisas'

df = scrape_timetable(url)

# apply filter
df = apply_filters(df=df
                   , min_hour='17:00'
                   , top_hour='21:00'
                   , days_to_keep=['Tuesday', 'Saturday']
                   , number_of_spots=10)

send_email(sender_email, receiver_email, password, subject, log_file)