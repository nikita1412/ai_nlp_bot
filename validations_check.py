import recharge
import requirements
import socket

REMOTE_SERVER = "www.google.com"
def validate_number(str_number):
    #print("inside Validate number function")
    #print(str_number)
    str_number = str_number.encode('utf8')
    str_number = str_number.strip()
    length = len(str_number)
    flag = True
    if length < 10 or length > 13:
        print(requirements.MESSAGES['Invalid_Phone_Number'])
        flag = False
    elif length == 11 and str_number[0] == '0' :
        recharge.final_order['ph_number'] = int(str_number[1:])
    elif length == 12 and str_number[0:2] == '91' :
        recharge.final_order['ph_number'] = int(str_number[2:])
    elif length == 13 and str_number[0:3] == '+91' :
        recharge.final_order['ph_number'] = int(str_number[3:])
    return (flag,int(str_number))

def validate_money(money):
    flag = False
    if money < 0:
        print(requirements.MESSAGES['Invalid_Amount'])
    else:
 #       print('Amount Valid')
        flag = True
        recharge.final_order['Amount'] = money
    #print('returning flag')
    #print(flag)
    return (flag,money)

def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
    print('Bot:Check internet Connection')
  return False
