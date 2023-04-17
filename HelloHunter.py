import requests
import json

# Enter the username, email address, phone number, and known social media accounts
username = "example_username"
email = "example_email@example.com"
phone_number = "123-456-7890"
social_media_accounts = ["facebook", "twitter", "linkedin"]

# Perform OSINT on the username
username_url = f"https://api.github.com/users/{username}"
username_response = requests.get(username_url)
if username_response.status_code == 200:
    username_data = json.loads(username_response.text)
    print(f"Name: {username_data['name']}")
    print(f"Location: {username_data['location']}")
    print(f"Bio: {username_data['bio']}")
    print(f"Public Repositories: {username_data['public_repos']}")
    print(f"Followers: {username_data['followers']}")
else:
    print(f"Username {username} not found.")

# Perform OSINT on the email address
email_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
email_headers = {"hibp-api-key": "YOUR_API_KEY_HERE"}
email_response = requests.get(email_url, headers=email_headers)
if email_response.status_code == 200:
    email_data = json.loads(email_response.text)
    for breach in email_data:
        print(f"Email breached in {breach['Name']} on {breach['BreachDate']}")
else:
    print(f"Email {email} not found in any breaches.")

# Perform OSINT on the phone number
phone_url = f"https://api.numverify.com/api/phone_number_info?access_key=YOUR_ACCESS_KEY_HERE&number={phone_number}"
phone_response = requests.get(phone_url)
if phone_response.status_code == 200:
    phone_data = json.loads(phone_response.text)
    print(f"Phone number: {phone_data['number']}")
    print(f"Country: {phone_data['country_name']}")
    print(f"Carrier: {phone_data['carrier']}")
else:
    print(f"Phone number {phone_number} not found.")

# Perform OSINT on the social media accounts
for account in social_media_accounts:
    account_url = f"https://api.urlmeta.org/?url=https://{account}.com"
    account_response = requests.get(account_url)
    if account_response.status_code == 200:
        account_data = json.loads(account_response.text)
        print(f"Account: {account}")
        print(f"Title: {account_data['title']}")
        print(f"Description: {account_data['description']}")
        print(f"Image: {account_data['image']}")
    else:
        print(f"Account {account} not found.")
