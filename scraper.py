import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_timetable(url, class_name='yraLaisvo'):
    # Initialize Chrome WebDriver with headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)

    # Open the webpage
    driver.get(url)

    # Wait until at least 100 elements with the specified class appear
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))

    # Ensure at least 100 elements are found
    while len(elements) < 400:
        elements = driver.find_elements(By.CLASS_NAME, class_name)

    # Once at least 100 elements are found, retrieve the page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract values from elements with class 'l'
    values = []
    for element in soup.find_all(class_='l'):
        value = element.get_text(strip=True)
        if not value or value == 'undefined':
            values.append(0)
        else:
            try:
                values.append(int(value))
            except ValueError:
                pass  # Ignore non-numeric values

    # Close the WebDriver
    driver.quit()

    # Define the time range
    start_time = datetime.strptime('06:00', '%H:%M')
    end_time = datetime.strptime('23:00', '%H:%M')
    step = timedelta(minutes=30)
    time_values = []
    current_time = start_time
    while current_time <= end_time:
        time_values.append(current_time.strftime('%H:%M'))
        current_time += step

    # Get today's date and generate a list of dates for the next 28 days
    today = datetime.today().date()
    date_range = [today + timedelta(days=i) for i in range(28)]

    # Create an empty DataFrame with time values as rows and date values as columns
    df = pd.DataFrame(columns=date_range, index=time_values)

    # Fill the DataFrame with zeros
    df = df.fillna(0)

    # Fill the DataFrame with values
    value_index = 0
    for column in df.columns:
        for i, row in enumerate(df.index):
            if value_index < len(values):
                df.at[row, column] = values[value_index]
                value_index += 1
            else:
                break

    return df