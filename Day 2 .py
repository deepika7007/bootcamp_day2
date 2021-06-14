#Day 2 string practice

# print a value 
print("30 days 30 hour challenge")
print('30 days Bootcamp')

#Assigning string to Variable
Hours="Thirty"
print(Hours)

#Indexing using String 
Days="Thirty days"
print(Days[0])
print(Days[3])

#Print particular character from certin text
Challenge="I will win"
print(challenge[7:10])

#print the length of the character
Challenge="I will win"
print(len(Challenge))

#convert String into lower character
Challenge="I Will win"
print(Challenge.lower())

#String concatenation - joining two strings
A="30 days"
B="30 hours"
C = A+B
print(C)

#Adding space during Concatenation 
A="30days"
B="30hours"
C=A+" "+B
print(C)

#Casefold() - Usage
text="Thirty Days and Thirty Hours"
x=text.casefold()
print(x)

#capitalize() usage
text="Thirty Days and Thirty Hours"
x=text.capitalize()
print(x)

#find()
text="Thirty Days and Thirty Hours"
x=text.find()
print(x)

#isalpha()
text="Thirty Days and Thirty Hours"
x=text.isalpha()
print(x)

#isalnum()
text="Thirty Days and Thirty Hours"
x=text.isalnum()
print(x)


Result:
30 days 30 hour challenge
30 days Bootcamp
Thirty
T
r
win
10
i will win
30 days30 hours
30days 30hours
thirty days and thirty hours
Thirty days and thirty hours
-1
False
False


** Process exited - Return Code: 0 **
Press Enter to exit terminal
