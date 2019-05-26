str1='hello 123'
print(str1.isalnum()) #有空白就算兩個字串
print(str1.isalpha())
print(str1.isdigit())
print(str1.isidentifier())
str2='hello'
print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str2.isidentifier())
print(str2.isspace())

str5='hello world'
print(str5.startswith('he'))
print(str5.endswith("d"))
print(str5.find('x'))
print(str5.rfind('o'))
print(str5.count('o'))
print(str5.capitalize())
print(str5.lower())
print(str5.upper())
print(str5.title())
print(str5.swapcase())

str4='    he  y y  eyye   '
print(str4.lstrip())
print(str4.rstrip())
print(str4.strip())
'''print(str4.center())'''

str8 ='hello'
print("\\"+str8.center(15)+"/")
