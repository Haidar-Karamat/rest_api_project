import os
import requests
import jinja2
from dotenv import load_dotenv

load_dotenv()

template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject, body, html):
    domain = os.getenv("MAILGUN_DOMAIN")
    api_key = os.getenv("MAILGUN_API_KEY")
    sender = os.getenv("MAILGUN_SENDER", f"Stores API <postmaster@{domain}>")

    response = requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": sender,
            "to": [to],
            "subject": subject,
            "text": body,
            "html":html,
        },
    )

    if response.status_code != 200:
        print(f"Mailgun error: {response.status_code} - {response.text}")
    return response



def send_welcome_email(user_email, username):
    html_content = render_template("email/action.html", username=username, current_year=2026)
    return send_simple_message(
        to=user_email,
        subject="Successfully signed up",
        body=f"Hi {username}! You have successfully signed up to the Stores REST API.",
        html=html_content
        
    )


def send_admin_notification(username, user_email):
    admin_email = os.getenv("ADMIN_EMAIL", "haiderkaramat2022@gmail.com")
    html_content = render_template("email/admin_notification.html", username=username, user_email=user_email)

    return send_simple_message(
        to=admin_email,
        subject="New User Registered",
        body=f"A new user has registered:\n\nUsername: {username}\nEmail: {user_email}",
        html=html_content
    )