def valid_card_no(card_no):
    # https://www.geeksforgeeks.org/luhn-algorithm/
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