import re
import time
import os.path, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver', options=options) 

USERNAME = 'your_evdoxos_username'
PASSWORD = 'your_evdoxos_password'
PROJECT_UPLOAD_DIRECTORY_URL = 'evdoxos_url'

def login():

        print("Logging in...")
        driver.get("https://evdoxos.ds.unipi.gr/main/login_form.php")

        time.sleep(2)
        login_form = driver.find_element_by_name('uname')
        login_form.send_keys(USERNAME)
        login_form = driver.find_element_by_name('pass')
        login_form.send_keys(PASSWORD)
        login_form = driver.find_element_by_name('submit')
        login_form.click()
        print("Logged in...")
    
def listen_for_changes():

        print("\n")
        print("**************************************************************************")
        print("Listening for changes on doc,docx or odt files in the current directory...")
        print("**************************************************************************")
        print("\n")

        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()

         try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()

def upload_file(modified_file_path):

        upload_button = driver.find_element_by_name('userfile')
        upload_button.send_keys(os.getcwd()+modified_file_path)

        submit_button = driver.find_element_by_name('work_submit')
        submit_button.click()

        print("File was uploaded succesfully on Evdoxos...\n")

class MyHandler(FileSystemEventHandler):

        def on_modified(self, event):  

        extensions = ('.doc', '.docx', '.odt')
        modified_file_path = str(event.src_path)

        # if file extension is any of $extensions
        if modified_file_path.endswith(extensions) and not modified_file_path.startswith(".\~$"):
            print("Change detected!")
            print("Uploading file...")
            driver.get(PROJECT_UPLOAD_DIRECTORY_URL)
            upload_file(modified_file_path)
        
if __name__ == "__main__":
        login()
        listen_for_changes()
