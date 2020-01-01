from twilio.rest import Client 
 
account_sid = 'twilio`s account id' 
auth_token = 'authentication token from twilio' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='twilio`s number',  
                              body='Twilio message from python script :p',      
                              to='phone number' 
                          ) 
 
print(message.sid)
