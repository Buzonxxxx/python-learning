from twilio.rest import Client

account_sid = 'account_sid'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='your twillo number',
  body='Hello Louis, Be patient. Sometimes you have to go through the worst to ge the best.',
  to='your phone number'
)

print(message.sid)