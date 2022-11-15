from twilio.rest import Client

account = "ACae7830b909ae8d24c01b194454743b04"
token = "1ff3f0e6555ae8e10da793264f1c06e1"
client = Client(account, token)

call = client.calls.create(to="+919814662390",
                           from_="+15735383621",
                           twiml="<Response><Say>HELLO bro</Say></Response>")
