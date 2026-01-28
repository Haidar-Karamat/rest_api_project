import os
import requests
def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox68e196c2091f450c9b04c4ded22477c7.mailgun.org/messages",
  		auth=("api", os.getenv('API_KEY', 'key-77c6c375-8bd9980e')),
  		data={"from": "Mailgun Sandbox <postmaster@sandbox68e196c2091f450c9b04c4ded22477c7.mailgun.org>",
			"to": "Haidar Karamt <haiderkaramat2022@gmail.com>",
  			"subject": "Hello Haidar Karamt",
  			"text": "Congratulations Haidar Karamt, you just sent an email with Mailgun! You are truly awesome!"})


if __name__ == '__main__':
	response = send_simple_message()
	print(response.status_code)
	print(response.text)