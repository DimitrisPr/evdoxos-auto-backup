<img src="https://upload.wikimedia.org/wikipedia/en/7/7e/UNIPI.jpg" width="70" align="right"><img src="https://external.fath3-4.fna.fbcdn.net/safe_image.php?d=AQCdeWE4HvICuAMi&w=540&h=282&url=https%3A%2F%2Frepository-images.githubusercontent.com%2F265819290%2Fbe577080-9c11-11ea-9356-56c0492ec86f&cfs=1&upscale=1&fallback=news_d_placeholder_publisher&_nc_hash=AQChigcTfpNnoyat" width="535">

# Evdoxos file auto-uploader for exams

[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python](https://img.shields.io/badge/built%20with-Python-red.svg)](https://www.python.org/)


Table of Contents
=================

* [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Quick Start](#quick-start)  
* [Contributing](#contributing)  


## Getting started

Script that monitors Word files for changes, and automatically uploads them on Evdoxos (when you save them).
Let the script running in the background and focus on your exams, distraction free.

### Requirements:
    - Google Chrome
    - Chromedriver
    - Python 
  
### Installation:

  1. Update Google Chrome to the latest version (IMPORTANT): https://www.google.com/chrome/  
    - On Ubuntu, update using apt: `sudo apt-get -y update && sudo apt-get -y upgrade`
  2. Check your Chrome version  
    - On Windows, go to this URL: chrome://settings/help  
    - On Ubuntu, use this command: `google-chrome --version`
  3. Download Chromedriver for your current Chrome version & operating system: http://chromedriver.chromium.org/downloads
  4. Add Chromedriver to the script's directory
  5. Clone this repo: `git clone https://github.com/DimitrisPr/evdoxos-auto-backup.git; cd evdoxos-auto-backup`
  6. Install missing Python libraries using requirments.txt   
    - On Windows & Ubuntu 20.04 LTS (or later): `pip install -r requirements.txt`  
    - On Ubuntu 18.04/19.10: `pip3 install -r reuquirements.txt`
  7. Open autosave.py and change the following variables
    
      ```python
      USERNAME = 'your_username_here'
      PASSWORD = 'your_password_here'
      PROJECT_UPLOAD_DIRECTORY_URL = 'the_project_upload_directory_url_here'
      ```
  *PROJECT_UPLOAD_DIRECTORY_URL* is the upload directory for your exam document. 
  
  8. Save and exit
  9. Create a new doc, .docx or .odt file at the project's directory. (While the name doesn't matter, the extension does)
  
You can find a written version of this guide [here](https://drive.google.com/file/d/1dI16ivvDLG3pEbSZy7r4BZR6JwnyVxGf/view?usp=sharing).
  
## Quick start

Now that everything is successfully installed, we can begin with a quick guide on how to use this script.  
Start the script and let it run in the background. Every time a change is detected, your files will be automatically uploaded to Evdoxos.

### Windows
```bash
python autosave.py
```

### Ubuntu
```bash
python3 autosave.py &
disown
```
If you are running Ubuntu 20.04 LTS or later, you can avoid using the `python3` command and use the `python` command directly.

<hr/>
⭐ Star this repo? :)
<hr/>

## Contributing

Contributions are accepted and welcome!  
How about we make a GUI using Python's TKinter?

## Testing

This project has been tested on:
   - Windows (Latest Chrome version as of 21-5-2020: 83.0.4103.61)
   - Linux (Latest Chrome version as of 21-5-2020: 83.0.4103.61)

<hr/>

### Where to find me
* https://prasakis.com
