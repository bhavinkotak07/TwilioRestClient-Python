from twilio.rest import TwilioRestClient
account = 'Your twilio account sid'
token = 'your account token'
client = TwilioRestClient(account, token)
message = client.messages.create(body="Message from Twilio rest client !", from_="+xxx",
                                 to="+xxxx")
