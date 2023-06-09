import re 
import string
import secrets
from datetime import datetime

def password_validator(password):
    '''
    Checks whether or not a password is valid.
    Input:
        password_validator: "string"
    Output:
        bool: If password is valid then the program will return True, if not the program will return False. 
        
    * A special character would be considered @, !, $, or a #
    '''
    if (len(password) < 8) or (len(password) > 12): #Checking to make sure length is between 8-12 characters
        return False
            
    elif not re.search("[A-Z]", password): #Checking to make sure there's an uppercase letter
        return False
         
    elif not re.search("[a-z]", password): #Checking to make sure there's a lowercase letter
        return False
       
    elif not re.search("[0-9]", password): #Checking to make sure there's a numerical letter
        return False
         
    elif not re.search("[@!$#]", password): #Checking to make sure there's special characters 
        return False
    else:
        return True

def valid_card_no(card_no):
    '''
    detects whether a credit card number is valid using luhn's algorithm
    
    input: 
        card_no: (int) the card number

    output:
        bool: if the card number is valid (True) or invalid (False)
    '''
    if type(card_no) != str:
        card_no = str(card_no).strip()
    
    summ = 0
    for x in range(len(card_no)):
        indx = -1 - x
        if indx%2 == 0:
            num = int(card_no[indx])*2
            if num >= 10:
                num = num//10 + num % 10
            summ += num
        else:
            summ += int(card_no[indx])
    return summ%10 == 0

def token_generator(token_length):
    '''
    Alphenumeric creates a variable that holds a selection of randomly generated letters and digits
    
    The while loop creates a process in which the selection of letters and digits are chosen to create the token variable.
    
    The last line returns to Token variable so that it can be used throughout the rest of the code

    input:
        token_length: determine length of token

    output:
        token: a string of compiled letters and numbers
    '''
    alphenumeric = string.ascii_letters + string.digits
    while True:
        token = ''.join(secrets.choice(alphenumeric) for i in range(token_length))
        if (any(c.islower() for c in token)
                and any(c.isupper() for c in token)
                and sum(c.isdigit() for c in token) >= 3):
            return(token)

def relative_time(_time):
    '''
    gives the relative time from a datetime object passed in as an argument
    
    input: 
        _time: (datetime) the datetime object

    output:
        str: the time relative to now
    '''
    diff = datetime.now() - _time
    days = (diff.days, "day")
    seconds = (diff.seconds, "second")
    minutes = (int(seconds[0]/60), "minute")
    weeks = (int(days[0]/7), "week")
    months = (int(days[0]/30), "month")
    years = (int(days[0]/365), "year")

    for x in [years, months, weeks, days, minutes, seconds]:
        if x[0] != 0:
            if x[1] == 1 or x[1] == -1:
                output = str(x[0]) + " " + x[1]
            else:
                output = str(x[0]) + " " + x[1] + "s"
            
            if x[0] < 0:
                return "in " + output[1:]
            else:
                return output + " ago"
    return "just now"
