from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time
import zipfile

# Configure the Selenium WebDriver
service = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")  # Correct path to chromedriver
options = Options()

# Set up the download directory
download_dir = r"C:\Users\Sukkiiii\Desktop\ME_DATA\CSQ"
prefs = {
    "download.default_directory": download_dir,  # Specify the directory
    "download.prompt_for_download": False,       # Disable download prompt
    "safebrowsing.enabled": True                 # Bypass safety checks
}
options.add_experimental_option("prefs", prefs)

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open Cricsheet home page
    driver.get("https://cricsheet.org/")
    
    # Wait for the dropdown to be available
    wait = WebDriverWait(driver, 20)
    select_element = wait.until(EC.presence_of_element_located((By.ID, "selectnav1")))

    # Interact with the dropdown and select the "Downloads" option
    select = Select(select_element)
    select.select_by_value("https://cricsheet.org/downloads/")  # Selecting the "Downloads" option by its value

    # Wait for the page to load after the selection
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '.zip')]")))

    # Find all download links for ZIP files
    download_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.zip')]")

    # Check if any download links are found
    if not download_links:
        print("No .zip files found in the dropdown.")
    else:
        # Download all the ZIP files
        for link in download_links:
            file_url = link.get_attribute("href")
            file_name = file_url.split("/")[-1]
            driver.get(file_url)  # Click the download link to start the download
            print(f"Downloading: {file_name}")

            # Wait for the download to complete (adjust based on file size and connection speed)
            time.sleep(5)

        print("All files downloaded successfully.")

        # Extract the ZIP files
        for zip_file in os.listdir(download_dir):
            if zip_file.endswith(".zip"):
                zip_file_path = os.path.join(download_dir, zip_file)
                extract_folder = os.path.join(download_dir, zip_file.split('.')[0])

                # Create extraction folder if it doesn't exist
                if not os.path.exists(extract_folder):
                    os.makedirs(extract_folder)

                # Extract the ZIP file
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_folder)
                print(f"Extracted {zip_file} to {extract_folder}")

        print("All ZIP files extracted successfully.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()
