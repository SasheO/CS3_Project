import re 

def password_validator(password):
    bool_ = True
    while bool_:
        if (len(password) < 8) or (len(password) > 12): #Checking to make sure length is between 8-12 characters
            return False
            break
        elif not re.search("[A-Z]", password): #Checking to make sure there's an uppercase letter
            return False
            break
        elif not re.search("[a-z]", password): #Checking to make sure there's a lowercase letter
            return False
            break
        elif not re.search("[0-9]", password): #Checking to make sure there's a numerical letter
            return False
            break
        elif not re.search("[@!$#]", password): #Checking to make sure there's special characters 
            return False
            break
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