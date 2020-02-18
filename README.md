Selenium Technical Interview Exercise (Python)
========

## Introduction

This is a simple repository to write functional/acceptance tests using Selenium WebDriver running on MacOS with Python programming language.

## Requirements

* Selenium
* [Python](https://seleniumhq.github.io/selenium/docs/api/py/)
* Browsers (Firefox, Safari, Chrome, IE, etc.)
* Respective browser drivers
  `Note:` I will use Firefox as the default browser runnning for this test


## Steps

1. Install python with [Homebrew](https://brew.sh/)

	`brew install python`


2. Install selenium with [pip](https://pip.pypa.io/en/stable/installing/)

	`pip install -U selenium`

	Note: If error occurs to perform the pip install, try the following,
		`curl -O https://bootstrap.pypa.io/get-pip.py`
		`sudo python3 get-pip.py`


3. Download latest Firefox Webdriver from `https://github.com/mozilla/geckodriver/releases` for macOS and locate it to `/usr/local/bin` directory

4. Start writing your test cases on new text file and save as `my_tests.py`

5. Running the test, simply typing `python my_tests.py`



	



