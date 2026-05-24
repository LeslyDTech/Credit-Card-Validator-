# Python Credit Card Validator Program


sum_odd_digits = 0
sum_even_digits = 0
total = 0

# remove any '_' or ' '
card_number = input("Enter a credit card number: ")
card_number = card_number.replace("-","") #removes dashes between card numbers
card_number = card_number.replace(" ", "") #removes spaces user types in between numbers
card_number = card_number[::-1] #reverses strings
print(card_number)

# add all digits in the odd places from right to left

for x in card_number[::2]:
    sum_odd_digits += int(x)

# double every second digits from right to left
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# add together the sum of the odd_digits and the sum of the even_digits
total = sum_odd_digits + sum_even_digits

# if total is % 10 = 0 then print valid, else print invalid
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")
