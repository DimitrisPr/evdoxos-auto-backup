## Dependecies
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import logging
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

###################################################################### PREFERENCES ##################################################################################################
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver', options=options) 

USERNAME = 'your_evdoxos_username'
PASSWORD = 'your_evdoxos_password'
PROJECTS_DIRECTORY = "" ## Enter path where you have all academic projects. Use \\ and not \
BASE_UPLOAD_URL = 'https://evdoxos.ds.unipi.gr/modules/work/index.php?course=' ## Base URL for Upload after Log-In Don't change that!!!
###################################################################### PREFERENCES ##################################################################################################
######################################################################## LOGGING ####################################################################################################
## Logger basic information
logging.basicConfig(level=logging.INFO,format='%(asctime)s : %(name)s : %(levelname)-8s : %(message)s',filename='Watchdog.log',filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
loggerwatchdog = logging.getLogger('Watchdog')
######################################################################## LOGGING ####################################################################################################
######################################################################## STARTED ####################################################################################################
## Start messages
loggerwatchdog.info("******************* Pre-initialization ***********************************")
loggerwatchdog.info("Watchdog will be active to this directory: "+PROJECTS_DIRECTORY)
loggerwatchdog.info("You have set the Evdoxos username to: " +USERNAME)
loggerwatchdog.info("You have set the Evdoxos password to: " +PASSWORD)
loggerwatchdog.info("******************* Pre-initialization ***********************************")
######################################################################## STARTED ####################################################################################################

def login():
        loggerwatchdog.info("********************** Login Section *************************************")
        loggerwatchdog.info("Logging in...")
        driver.get("https://evdoxos.ds.unipi.gr/main/login_form.php")

        time.sleep(2)
        login_form = driver.find_element_by_name('uname')
        login_form.send_keys(USERNAME)
        login_form = driver.find_element_by_name('pass')
        login_form.send_keys(PASSWORD)
        login_form = driver.find_element_by_name('submit')
        login_form.click()
        loggerwatchdog.info("Logged in...")
        loggerwatchdog.info("********************** Login Section *************************************")
    
def listen_for_changes():
    loggerwatchdog.info("********************* Watchdog initiated *********************************")
    loggerwatchdog.info("Check for modified .doc, .docx or .odt files in the directory: " +PROJECTS_DIRECTORY)
    loggerwatchdog.info("********************* Watchdog initiated *********************************")

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, PROJECTS_DIRECTORY, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        loggerwatchdog.info ("Watchdog disabled")

def upload_file(modified_file_path):

    upload_button = driver.find_element_by_name('userfile')
    upload_button.send_keys(os.getcwd()+modified_file_path)
    
    submit_button = driver.find_element_by_name('work_submit')
    submit_button.click()

    loggerwatchdog.info("******************** Upload Section **********************************")
    loggerwatchdog.info("File was uploaded succesfully on Evdoxos...")
    loggerwatchdog.info("******************** Upload Section **********************************")

class MyHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            loggerwatchdog.info ("Received created event : %s" % event.src_path)

        elif event.event_type == 'modified':
            loggerwatchdog.info ("Received modified event: %s" % event.src_path)
            if os.path.exists(event.src_path):

                modified_file_path = str(event.src_path)
                extensions = ('.doc', '.docx', '.odt')

                FullDirectory = os.path.dirname(event.src_path)
                CourseURL = (os.path.dirname(event.src_path)).split(PROJECTS_DIRECTORY)[1].split("##")[0].replace("\\","").replace(" ","")
                SubProjectURL = (os.path.basename(FullDirectory)).split("##")[0].replace(" ","").replace("&","")
                ModifiedFileDetected = os.path.basename(event.src_path)
                ModifiedFileTitle = os.path.splitext(ModifiedFileDetected)[0]
                ModifiedFileType = os.path.splitext(ModifiedFileDetected)[1]

                loggerwatchdog.info("**************** Detection Information ****************************")
                loggerwatchdog.info("Full directory where file change was detected: " +FullDirectory)
                loggerwatchdog.info("Course Folder: " +CourseURL)
                loggerwatchdog.info("Sub Project Folder: " +SubProjectURL)
                loggerwatchdog.info("Modified File: " +ModifiedFileDetected)
                loggerwatchdog.info("**************** Detection Information ****************************")

                ProjectURL = (BASE_UPLOAD_URL+CourseURL+'&'+SubProjectURL)

                loggerwatchdog.info("******************** URL Section **********************************")
                loggerwatchdog.info("Upload URL for the Project: " +ProjectURL)
                loggerwatchdog.info("******************** URL Section **********************************")

                if ((ModifiedFileType in extensions) and not (modified_file_path.startswith(".\~$"))):
                    loggerwatchdog.info("Change detected at file:{}".format(modified_file_path))
                    loggerwatchdog.info("Uploading file...")
                    driver.get(ProjectURL)
                    upload_file(modified_file_path)
        
        elif event.event_type == 'deleted':
            loggerwatchdog.info ("Received deleted event: %s" % event.src_path)   

if __name__ == "__main__":
    login()
    listen_for_changes()
