first_name,sec_name= input("Enter your First Name and Second Name:").split()
ph_no = input("Enter the phone number: ")
gmail=input("Enter your gmail id:")
#for name
print("Name:",first_name.capitalize(),sec_name.capitalize())
#for phone no.
length = len(ph_no)
if length == 10 and ph_no[:].isdigit() :
    print("Phone Number:",ph_no)
else :
    print("Invalid Phone Number, Please re-enter!!!")
#for email
if gmail.endswith("@gmail.com")==True and gmail[:-10].isalnum():
  print("Email Address:",gmail)
else:
  print("Invalid gmail id, Please re-enter!!!")