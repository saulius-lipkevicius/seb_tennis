from flask import Flask
import threading
import time
from helpers import *
import warnings

# Ignore all future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

url = 'https://book.sebarena.lt/?_ga=2.117973065.1966334876.1713010607-2100705733.1713010607#/rezervuoti/tenisas'
min_hour = '17:00'
max_hour = '18:00'
days_to_keep = ['Tuesday']

app = Flask(__name__)

running = True

def repeated_function():
    while running:
        print("Function is running...")
        call_scraper(url, min_hour, max_hour, days_to_keep)
        time.sleep(60)  # Repeat every 60 seconds

@app.route('/')
def home():
    return "Server is running. Check the console for repeated function output."

def start_server():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Start the repeated function in a separate thread
    function_thread = threading.Thread(target=repeated_function)
    function_thread.start()

    try:
        # Start the Flask server
        start_server()
    finally:
        # Signal the repeated function to stop and wait for the thread to finish
        running = False
        function_thread.join()
        print("Server has been shut down and the repeated function has stopped.")

