LeetCode Recent Submissions Emailer
This Python script fetches recent LeetCode submissions and emails a list of unique problem URLs to a specified email address.

Features
Fetches recent LeetCode submissions using the GraphQL API.
Generates a unique list of problem URLs.
Sends the list via email using the Gmail SMTP server.
Prerequisites
Python 3.x
Gmail account for sending emails
Installation
### Clone the repository:
git clone https://github.com/yourusername/leetcode-recent-emailer.git
cd leetcode-recent-emailer
### Install the required packages:
pip install requests

### Variables
Update your LeetCode username and email credentials in the script:
variables = {
    "username": "your_leetcode_username",
    "limit": 20
}

from_email = "your_email@gmail.com"
to_email = "recipient_email@gmail.com"
Set up a 16-digit app password for your Gmail account. Follow these steps:

Go to Google App Passwords.
Select "Mail" as the app and "Other" for the device name.
Generate the app password and copy the 16-digit password.
Replace "your_email_password" in the script with this 16-digit app password.

### Run the script:
python3 main.py

### The script will:

Fetch recent submissions from LeetCode.
Generate a list of unique problem URLs.
Email the list to the specified email address.
Script Breakdown
Fetch LeetCode Submissions:

# python
Copy code
import requests
from datetime import datetime

# Define the GraphQL query
query = """
query getRecentSubmissions($username: String!, $limit: Int) {
    recentSubmissionList(username: $username, limit: $limit) {
        title
        titleSlug
        timestamp
        statusDisplay
        lang
    }
}
"""

# Define the variables
variables = {
    "username": "hariprakash_619",
    "limit": 20
}

# Define the endpoint URL
url = "https://leetcode.com/graphql?"

payload = {
    "query": query,
    "variables": variables
}

# Send the request
response = requests.post(url, json=payload)

# Check for successful request
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()
    # Output the response
    n = len(data["data"]["recentSubmissionList"])
    unique = set()
    for i in range(n):
        u = data["data"]["recentSubmissionList"][i]["titleSlug"]
        unique.add('https://leetcode.com/problems/' + u + '/description/' + '\n')
else:
    # Output the error
    print(f"Query failed with status code {response.status_code}: {response.text}")

# Clean up the URLs by stripping any leading/trailing whitespace
urls = [url.strip() for url in unique]
Send Email with URLs:

python
Copy code
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
from_email = "xx@gmail.com"
to_email = "xxxx@gmail.com"
subject = "Today's List of URLs"
body = "Here is the list of URLs:\n\n" + "\n".join(urls)

# Create the email message
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Attach the body with the URLs to the email
msg.attach(MIMEText(body, 'plain'))

# Gmail SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For starttls

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(from_email, "your_16_digit_app_password")
        server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")

Notes
Ensure you have enabled "Less secure app access" in your Gmail account settings to allow the script to send emails.
Update your email password in the script securely. Consider using environment variables or a configuration file to store sensitive information.
License
This project is licensed under the MIT License.

