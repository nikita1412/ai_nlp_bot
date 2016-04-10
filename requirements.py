import urllib2

access_token = 'UTZY736TQK7HYDKLVOIEHHQZBN65KNU4'
App_Id = '57078ce6-4b6e-4453-bfbd-c36d9b51c373'
Wallet = 100
MESSAGES = {
	'hi_message' : 'Bot:Hi There! Enter number and amount for recharge',
	'low_confidence' : 'Bot:Sorry! Pal can\'t get you.Please give input again',
	'Invalid_Phone_Number' : 'Bot:Ahmm! Guess some digits are misplaced',
	'Invalid_Amount':'Bot:Amount given is not valid,Enter valid Amount Friend',
	'Payment_Details': 'Bot:Getting your Wallet Balance',
	'Re-enter Details':'Bot:Please Enter Phone Number and Amount',
	'Payment Rejection':'Bot:Never mind Meet you soon',
	'Successful Payment':'Bot:Payment Done Successfully',
	'UnSuccessful Payment' : 'Bot:Payment Failed!Low Wallet Balance'}

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: 
    	print('Bot: Ckeck Network and then input Number and Amount')
    return False