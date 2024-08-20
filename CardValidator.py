# for Checking the card number is valid or not we taking the following steps
#step 1 Remove any dashes and spaces
#step 2 reverse the card number
#step 3 add every secound digit number in odd digit variable
#step 4 double up of every second place number and in even digit number
#step 5 total the sum odd digit number and even digit number
#step 6 divide the total by 10 if the answer is 0 then the card is valid otherwise its invalid

sum_odd_digits = 0
sum_even_digits = 0
total = 0
card_number = input("Enter Your Card Number with Dashes = ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
print(card_number)
# reverse the caed number
card_number = card_number[::-1]
for x in card_number [::2]:
    sum_odd_digits = sum_odd_digits + int(x)   
print(sum_odd_digits)
 # double up of every digit
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits = sum_even_digits + (1 + (x % 10))
    else:
        sum_even_digits = sum_even_digits + x
        
# total the sum digit and odd digit         
total = sum_odd_digits + sum_even_digits
print(total)
#check validation
if total % 10 ==0 :
    print("Valid Card")
    
else:
    print("Invalid Card")