from flask import Flask
import threading
import time

app = Flask(__name__)

running = True

def repeated_function():
    while running:
        print("Function is running...")
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
        global running
        running = False
        function_thread.join()
        print("Server has been shut down and the repeated function has stopped.")
