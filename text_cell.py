# Using Twilio (it's free)
# simple code to text my cell when my programs fail
from twilio.rest import Client
account_sid = 'account_sid'
auth_token = 'auth_token'

client = Client(account_sid, auth_token)

  
def text_my_cell(text='program failed',trent=False):
  # text: String. This is the message to be texted
  # trent = True
    # Also send the message to my research advisor Trent
    call = client.messages.create(
                            body=text,
                            to='input_your_number',
                            from_='input_twilio_number'
                        )
    if trent:
        call = client.messages.create(
                                body=text,
                                to='input_another_number',
                                from_='input_twilio_number'
                            )
                  
# I use this code to send my self daily updates on the overall data collection every day
# Useful to catch random bugs in Twitter's API that result in a request timeout and need to be corrected manually 

# simple function to put commas in an integer to make it easily readable
def int_comma(integer):
    return ','.join([str(integer)[::-1][i:i+3] for i in range(0,len(str(integer)),3)])[::-1]
