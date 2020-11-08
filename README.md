# python-lambda-contact-form

This is a contact form for a static site using AWS API Gateway, Lambda
and Simple Email Service (SES). It is written in Python and uses the
[Chalice][1] microframework to manage deployment.

It is written for Python 3.8.

I use it on my site at https://al.sdair.co.uk/contact/

## Instructions (WIP)

### Verify your from-email address

AWS requires that you verify the from email address. See [the docs][2]
for more info.

### Clone the repository

    git clone https://github.com/alasdairnicol/python-lambda-contact-form
    cd python-lambda-contact-form

[1]: https://github.com/awslabs/chalice 
[2]: http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html
