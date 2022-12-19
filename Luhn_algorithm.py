# run this program and then just change json file in directory python file and save it


import json
import os
import time
 

def validate_credit_card(card_number: str):
    print("card number: ",card_number)
    print("lenght card number: " ,len(card_number))
    print("card number is: " , "even" if len(card_number)%2==0 else "odd" )
    """This function validates a credit card number."""
    # 1. Change datatype to list[int]
    card_number = [int(num) for num in card_number]

    # 2. Remove the last digit:
    checkDigit = card_number.pop(-1)

    # 3. Reverse the remaining digits:
    card_number.reverse()

    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0 else num for idx, num in enumerate(card_number)]

    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    # 6. Add the checkDigit back to the list:
    card_number.append(checkDigit)

    # 7. Sum all digits:
    checkSum = sum(card_number)
    print("sum all: ",checkSum)


    # 8. If checkSum is divisible by 10, it is valid.
    print("remainder of the division: ",checkSum % 10)
    print("card number is correct" if checkSum % 10 == 0 else "card number is incorrect")
    # return

# # American Express
# print(validate_credit_card('378282246310005'))  # True
# print(validate_credit_card('371449635398431'))  # True
# # American Express Corporate
# print(validate_credit_card('378734493671000'))  # True
# # Australian BankCard
# print(validate_credit_card('5610591081018250'))  # True
# # Diners Club
# print(validate_credit_card('30569309025904'))  # True
# print(validate_credit_card('38520000023237'))  # True
# # Discover
# print(validate_credit_card('6011111111111117'))  # True
# print(validate_credit_card('6011000990139424'))  # True
# # MasterCard
# print(validate_credit_card('5555555555554444'))  # True
# print(validate_credit_card('5105105105105100'))  # True
# # Visa
# print(validate_credit_card('4111111111111111'))  # True
# print(validate_credit_card('4012888888881881'))  # True

# # Invalid Credit Card Number
# print(validate_credit_card('7762888103111881'))  # False
# print(validate_credit_card('37612555227841800'))  # False


json.dump({"enter_your_Card_Number":None}, open('luan.json', 'w')) # creat json file to enter yuor Card_Number
f=0
while 1:
    time.sleep(0.05) # it for control use cpu
    try:
        if os.path.isfile("luan.json"): # check if file exist in directory
            luan=json.load(open('luan.json')) # take json file
            if luan["enter_your_Card_Number"]!=None: # check if you enter a new Card_Number
                Card_Number=luan["enter_your_Card_Number"]
                validate_credit_card(Card_Number)
                json.dump({"enter_your_Card_Number":None}, open('luan.json', 'w'))
                f=0
        if f==0:
            print("enter your Card_Number")
            f=1
    except Exception as error: #control error
        # print(error)
        pass
