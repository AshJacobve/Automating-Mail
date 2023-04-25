# Automating Mail

This repository contains a Python script, `run.py`, that automates the process of sending emails using the Gmail API. The script utilizes the Google API Client Library for Python to interact with the Gmail API, allowing users to send emails without manually logging in to their Gmail account.

## Prerequisites

Before running the `run.py` script, you need to install the required libraries. You can do this using the following commands:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

The libraries imported in the `run.py` script are:

- `os`: This module provides a way to interact with the operating system, allowing the script to access and modify files and directories.

- `base64`: This module provides functions for encoding and decoding binary data into ASCII string format, which is used to encode the email message in the Gmail API.

- `email`: This module provides classes and methods for constructing and manipulating email messages, which is used to create the email message that will be sent.

- `google.oauth2.credentials`: This module provides classes for handling OAuth 2.0 credentials, which are used to authenticate the script with the Gmail API.

- `googleapiclient.discovery`: This module provides a way to create a client for interacting with the Gmail API, allowing the script to send emails.

## Downloading the Gmail API

In order to use the Gmail API, you need to create a project in the Google Cloud Console and enable the Gmail API for that project. Once you have done that, you need to create a credentials file that will allow the `run.py` script to authenticate with the Gmail API.

Follow the steps below to download the Gmail API:

1. Go to the Google Cloud Console (https://console.cloud.google.com/).

2. Create a new project or select an existing project.

3. In the left sidebar, click on "API & Services" > "Library".

4. In the "Search for APIs & Services" search bar, type "Gmail API" and click on it in the results.

5. Click the "Enable" button to enable the Gmail API for your project.

6. In the left sidebar, click on "API & Services" > "Credentials".

7. Click the "Create credentials" button and select "Service account" from the dropdown menu.

8. Fill in the required information for the service account, such as the service account name and role. You can leave the "Key type" as JSON.

9. Click the "Create" button to create the service account and download the JSON credentials file.

10. Save the JSON credentials file in the same directory as the `run.py` script.

## Usage

Once you have downloaded the Gmail API credentials file, you can run the `run.py` script to send emails using the Gmail API. You can configure the email settings, such as the sender's email address, recipient's email address, subject, and body, in the `run.py` script before running it.

The mail to be sent is under **"Mail.txt"**. This can be modified for personal use.  

To run the `run.py` script, you can use the following command:

```bash
python run.py
```

Note: You may need to authorize the script to access your Gmail account the first time you run it. Follow the instructions in the terminal to authorize the script.

That's it! The `run.py` script will send the email using the Gmail API with the configured email settings.

## Conclusion

Automating Mail is a Python script that allows you to send emails using the Gmail API. With the help of the Google API Client Library for Python and the Gmail API credentials, you can easily configure and send emails without manually logging in to your Gmail account. Happy emailing!
