from twilio.rest import Client as SMSClient

from settings import TWILIO_ACCOUNT_ID, TWILIO_TOKEN, TEST_NUMBER, ACCOUNT_NUMBER


TWILIO_CLIENT = SMSClient(TWILIO_ACCOUNT_ID, TWILIO_TOKEN)


def send_message(text):
    return TWILIO_CLIENT.messages.create(to=TEST_NUMBER, from_=ACCOUNT_NUMBER, body=text)


def list_messages():
    return TWILIO_CLIENT.messages.list()


if __name__ == '__main__':
    content = 'This is a test message sent from the twilio python client'

    send_message(content)