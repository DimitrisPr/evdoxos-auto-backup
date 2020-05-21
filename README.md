<img src="https://prasakis.com/github/LOGOPAPEI4.png" width="180" align="right">

# Exam Test Auto-backup for Evdoxos Platform

[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python](https://img.shields.io/badge/built%20with-Python-red.svg)](https://www.python.org/)


Table of Contents
=================

* [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Installation](#installation)
* [How to execute](#how-to-execute)  
* [How to contribute](#how-to-contribute)  

## Getting started

Script that monitors word or open office files for changes and automatically backs them up on Evdoxos Platform.
Let the script running in the background and focus on your exams, distraction free.

### Requirements:
    - Google Chrome
    - Python 
  
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

Let the script running on the background. Everytime it detects a change it automatically uploads a new file on Evdoxos.
```bash
$ python autosave.py
```

## How to contribute

Let's make a GUI ith tkinter? Contributions accepted. 

<hr/> 

**Disclaimer**: This project has been tested on:
                  - Windows (Latest chrome version as of 21-5-2020: 83.0.4103.61)
                  - Linux (Latest chrome version as of 21-5-2020: 83.0.4103.61)

**Contact me**: I would love to socialize with you. Find me: https://prasakis.com
