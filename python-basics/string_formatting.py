# Name : Millward Jeremy
# Date : 12/02/2026
# string

# Get string length
sentence = "Better late than never" 

string_length = len(sentence)

print(f"The length is: {string_length}")

# spliting a string 
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is: ", split[0])


# Make evrything CAPS
mpesa_code = "ub21ddsfhg"

capitalised = mpesa_code.upper()

print("New mpesa code: ", capitalised)

#Make to lower 
lowercase_code = mpesa_code.lower()

print("New M-pesa code", lowercase_code)

#Replacing characters in a string

balance = "100kes"
amount_added ="50kes"

amount_added = balance.replace("kes", "")

print("cleaned balance:", cleaned_balance)

cleaned_amount_added = amount_added.replace("kes","")

print("cleaned amount added: ", cleaned_amount_added)

#Milward answer 
new_balance = int(cleaned_balance) + int(cleaned_amount_added)

print(f"The new baalnce is:",new_balance)

