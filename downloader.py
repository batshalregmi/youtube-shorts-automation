import selenium
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def download_video(url):
    directory = os.path.dirname(os.path.realpath(__file__))
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={directory}\selenium")
    prefs = {"download.default_directory" : "YOURDIRHERE"}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options)

    driver.get(url)


    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "post-download-all-button")))

    element.click()

    sleep(5)


    folder_path = 'instagram-vids'

    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Find the first file in the folder (assuming there is only one file)
    if files:
        old_file_path = os.path.join(folder_path, files[0])
        new_file_path = os.path.join(folder_path, 'video.mp4')

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"File renamed to {new_file_path}")
    else:
        print("No files found in the folder.")


