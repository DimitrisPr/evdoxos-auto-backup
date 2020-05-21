
<img src="https://www.unipi.gr/unipi/images/images/LOGOPAPEI4.png" width="150" align="right">

# HTB Cancel Machine Resets Bot

[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python](https://img.shields.io/badge/built%20with-Python-red.svg)](https://www.python.org/)

Script that monitors for changes in your word file and automatically backs up your work on Evdoxos.

Let the script running in the background and focus on your exams, distraction free.


Table of Contents
=================

* [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Installation](#installation)
* [How to use](#how-to-use)  
* [How to contribute](#how-to-contribute)  

## Getting started

### Requirements:

  
### Installation:

  1. Update chrome (IMPORTANT): https://www.google.com/chrome/ 
  2. Check your chrome version 
    - Ubuntu: `google-chrome --version`
    - Windows: chrome://settings/help
  3. Download Chromedriver for your chrome version & OS: http://chromedriver.chromium.org/downloads
  4. Add Chromedriver to the same directory with the script
  5. Clone this repo: `git clone https://github.com/DimitrisPr/evdoxos-auto-backup.git; cd evdoxos-auto-backup`
  6. Install requirments `pip install -r requirements.txt`
  7. Open autosave.py and change the following variables
    
      ```
      USERNAME = 'your_username_here'
      PASSWORD = 'your_password_here'
      PROJECT_UPLOAD_DIRECTORY_URL = 'the_project_upload_directory_url_here'
      ```
  where PROJECT_UPLOAD_DIRECTORY_URL is the upload directory if your exam test file. 
  
  8. Save and exit
  9. Create a new doc, .docx or .odt file at the the project's directory. (The name doesn't matter, the extension does)
  
## How to execute

Let the script running:
```bash
$ python autosave.py
```

**Disclaimer**: This project has been tested on:
                  - Windows (Latest chrome version as of 21-5-2020: 83.0.4103.61)
                  - Linux (Latest chrome version as of 21-5-2020: 83.0.4103.61)

**Contact me**: I would love to socialize with you. Find me: https://prasakis.com
