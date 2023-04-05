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


if __name__ == "__main__":
    assert valid_card_no(49927398716) == True, "49927398716 = True"
    assert valid_card_no(49927398717) == False, "49927398717 = False"
    assert valid_card_no(1234567812345620) == False, "1234567812345620 = False"
    assert valid_card_no(1234567890) == False, "1234567890 = False"
    assert valid_card_no(1234567812345678) == False, "1234567812345678 = False"
    assert valid_card_no(61789372994) == True, "61789372994 = True"
    assert valid_card_no(5146716835430) == True, "5146716835430 = True"
    assert valid_card_no(5146716835431) == False, "5146716835431 = False"
    assert valid_card_no(4661074345770850) == True, "4661074345770850 = True"
    
    
    
import re 

def password_validator(password):
    bool = True
    while bool:
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

          
                        
                      
        
          
            
                            
        
        



