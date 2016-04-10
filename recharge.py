import wit_handler
import requirements
import validations_check
final_order = {}
#def Payment_Gateway(order):
requirements.Wallet = 100

def Payment_Gateway():
    print('Bot:Your wallet has Amount %d' %(requirements.Wallet))
    print(requirements.Wallet)
    if final_order.get('Amount',0) <= requirements.Wallet:
        print(requirements.MESSAGES['Successful Payment'])
        requirements.Wallet = requirements.Wallet - final_order.get("Amount",0)
        print('Bot:Current Wallet Balance %d' %(requirements.Wallet))
        print("Bot:Recharge Again! Enter number and Amount")
    else:
        print(requirements.MESSAGES['UnSuccessful Payment'])
        print("Bot:Never Mind Pal! Recharge Again!Enter number and amount")
    return


def only_number_state(number):
    got_money = False
    while not got_money:
        print('Bot:Please Enter Amount')
        message = raw_input('You:')
        intent ,outcomes = wit_handler.get_intent(message)
  #      print(intent)
 #       print(outcomes)
        entities = wit_handler.get_entities(outcomes)
        #print(entities)
        if intent == u'phone_recharge' and entities.has_key('money'):
            both_num_money_state(number,entities.get('money',0))
            got_money = True
    return

def only_money_state(money):
    got_number = False
    while not got_number:
        print('Bot:Enter Number Again')
        message = raw_input('You:')
        intent ,outcomes = wit_handler.get_intent(message)
        entities = wit_handler.get_entities(outcomes)
        if intent == u'phone_recharge' and entities.has_key('number'):
   #         print(entities)
            both_num_money_state(entities.get('number',0),money)
            got_number = True
    return

def both_num_money_state(number,money):
    
    no_valid ,ph_number = validations_check.validate_number(number)
    if no_valid:
        final_order['ph_number'] = ph_number
    else:
        only_money_state(money)
        return
    
    amt_valid ,Amount = validations_check.validate_money(money)
    
    if amt_valid:
        final_order['Amount'] = Amount
    else:
        only_number_state(number)
        return

    if no_valid and amt_valid:
        verify_order_details()
    return


def verify_order_details():
    print('Bot:Instantiating Recharge on Number: %d for Amount: %d ok?' %(final_order['ph_number'],final_order['Amount']) )
    return



if __name__ == '__main__':
    
    message = raw_input(requirements.MESSAGES['hi_message'] + '\n' + 'You:')
    no_valid = False
    amt_valid = False
    if message:
        while message:
            if validations_check.is_connected():
                intent,outcomes = wit_handler.get_intent(message)
                if intent == u'phone_recharge':
                    entities = wit_handler.get_entities(outcomes)
                    if(len(entities)==2):
                        both_num_money_state(entities.get('number',0),entities.get('money',0))
                    elif(len(entities)>0):
                        if(entities.has_key('number')):
                            only_number_state(entities.get('number',0))
                        elif(entities.has_key('money')):
                            only_money_state(entities.get('money',0))
                    else:
                        print(requirements.MESSAGES['Re-enter Details'])
                if intent == u'accept' :
                    if len(final_order) ==2:
                        print(requirements.MESSAGES['Payment_Details'])
                        Payment_Gateway()
                    
                    else:
                        print("Bot:Bye")
                        print(requirements.MESSAGES['hi_message'])
                if intent == u'reject':
                    print(requirements.MESSAGES['Payment Rejection'])
                    final_order.clear()

                message = raw_input('You:')

