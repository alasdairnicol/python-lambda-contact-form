from urllib.parse import parse_qs

import boto3

from chalice import Chalice, BadRequestError
from chalicelib import TO_EMAIL, FROM_EMAIL, SITE, IGNORE

app = Chalice(app_name='contactform')


@app.route('/contact', methods=['POST'], content_types=['application/x-www-form-urlencoded'], cors=True)
def contact():
    # Set these in chalice/__init__.py
    to_email = TO_EMAIL
    from_email = FROM_EMAIL
    site = SITE

    parsed = parse_qs(app.current_request.raw_body.decode('utf-8'))

    # Default to [None] to avoid IndexError
    name = parsed.get('name', [None])[0]
    email = parsed.get('email', [None])[0]
    message = parsed.get('message', [None])[0]

    if not name:
        raise BadRequestError("Please enter your name")
    if not email:
        raise BadRequestError("Please enter your email")
    if not message:
        raise BadRequestError("Please enter your message")

    # Don't send message if it contains words from IGNORE list
    for ignore in IGNORE:
        if ignore in message:
            return {
                "status": "OK",
            }

    client = boto3.client('ses')

    client.send_email(
        Source=from_email,
        Destination={
            'ToAddresses': [to_email],
        },
        Message={
            'Subject': {
                'Data': "Message from " + name + " via " + site,
            },
            'Body': {'Text': {
                'Data': message,
            }},
        },
        # setting the reply-to header makes means that when you hit
        # reply, the email goes to your visitor, not your from_email
        ReplyToAddresses=[email],
    )

    response = {
        "status": "OK",
    }

    return response
