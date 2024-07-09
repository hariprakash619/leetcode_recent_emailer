import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
    "username": "xxxxxxxxxx",
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
            unique.add('https://leetcode.com/problems/'+u+'/description/'+'\n')
else:
    # Output the error
    print(f"Query failed with status code {response.status_code}: {response.text}")


# Clean up the URLs by stripping any leading/trailing whitespace
urls = [url.strip() for url in unique]

# Email details
from_email = "xxxxx@gmail.com"
to_email = "xxxxx@gmail.com"
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
        server.login(from_email, "xxxxxxxxxxxx")  # Replace with your email/app password
        server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")
