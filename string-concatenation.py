#String concatenation

#operator overloadind
message1 = "Hi,"
message2 = "How are you?"
print(message1 + " " + message2)

#insert full Name
a = "prasad"
b = "aketi"
print("Full name :" ,a + "" + b)

#f'string/interpolation
message1 = "How are you?"
message2 = "Iam fine."
print( f'{message1}{message2}')

#insert Fullname
a = "prasad"
b = "aketi"
print("Full name :" ,f'{a} {b}')

#string join
message1 = "What is your name?"
message2 = "My name is prasad."
lst = (message1,message2)
print(" ".join(lst))

#insert full name=
a = "prasad"
b = "aketi"
c = ("Full name" ,a , b)
print(" ".join(c))

#split
email = "devisriprasad123@gmail.com"
print(email.split("@"))

#splitlines
address = """5-9,
Sivalayam street,
elamanchili,
west godavari dist,
andhra pradesh"""
print(address.splitlines())

#partition
email = "devisriprasad123@gmail.com"
print(email.partition("@"))

#rpartition
email = "b@devisriprasad123@gmail.com"
print(email.rpartition("@"))