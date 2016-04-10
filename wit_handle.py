import wit
import requirements

def get_entities(message):
	response1 = wit.message(access_token, message)
    print(response1)
    outcomes = response1.get('outcomes',0)
    #response3 = response2[0]
    #response4 = response3['entities']
   # print(response4)
   number = None
   money = None
   values = {}
   if outcomes.get('confidence',0) > 0.0:
   	entities = outcomes.get('entities',0)
    phone_number = entities.get('phone_number',0)
    amount_of_money = response4.get('amount_of_money',0)
    if phone_number:
    	number = phone_number[0].get('value',0)
        print(number)
        values['number'] = number
    if amount_of_money:
    	money = amount_of_money[0].get('value',0)
        print(money)
        values[money] = money
    else:
    	print(requirements.MESSSAGES['low_confidence'])
  return values

  def get_intent(message):
  	response1 = wit.message(access_token,message)
  	print(response1)

  	outcomes = response1.get('outcomes',0)
  	intent = outcomes.get('intent',0)