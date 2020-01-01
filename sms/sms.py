from twilio.rest import Client 
 
account_sid = 'AC0ef5536469e7f296a9a5b1eee2957d9a' 
auth_token = '30cb86553c6f650d6b79472efebf94c7' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+18317776915',  
                              body='Twilio message from python script :p',      
                              to='+48724666357' 
                          ) 
 
print(message.sid)