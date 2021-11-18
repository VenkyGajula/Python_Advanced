# Regular Expression**************
print("***findall()*******")
import re
a='my studies are compled 2020 2021 my favorate number is 9'
b=a.split()
for i in b:
    if re.search('^[0-9]+',i) :
        print(i)

print("*******Mobile number*******")
s=input("enter the mobile number")
m=re.fullmatch('[6-9]\d{9}',s)
if m!=None:
    print(s,"is valid Mobile Number")
else :
    print(s,"is not Valid mobile Number")

print("******search()*******")
file=open("C://Users/user/Desktop/sample.txt","r")
for line in file :
    line=line.rstrip()
    if re.search('From',line):
        print(line)

print("****match()*******")
i=input("enter the input")
ma=re.match(i,'abcdfef')
if ma!=None :
    print('start{},end{}'.format(ma.start(),ma.end()))
else :
    print("not available")

print("*****finditer()******")
count=0
pattern=re.compile('ab')
mat=pattern.finditer('abbbaaab')
for match in mat :
    count=count+1
    print('start index :',match.start())
print("the num of occurs ",count)

print("***character classes******")
matcher=re.finditer('\w\W','a7b@k9z')

#[abc][^abc][a-z][a-zA-Z][0-9][a-zA-Z0-9]
#\w\W(word)
#\d\D(digit)
#\s\S(space)
# . Every character

for matc in matcher :
    print(matc.start(),'---',matc.group(),'---',matc.end())

print("********function in re module*******")
print("match()")
print("fullmatch()")
print("finditer()")
print("search()")
print("findall()")
print("sub()")
print("subn()")
print("split()")
print("compile()")

print("*******Quatifiers 1********")
import re
matcher=re.finditer("a","abaabaaab")
for match in matcher:
 print(match.start(),"......",match.group())

print("*******Quatifiers 2(+)********")
matcher=re.finditer("a+","abaabaaab")
for match in matcher:
  print(match.start(),"......",match.group())

print("*******Quatifiers 3(*)********")
matcher=re.finditer("a*","abaabaaab")
for match in matcher:
  print(match.start(),"......",match.group())

print("*******Quatifiers 4(?)********")
matcher=re.finditer("a?","abaabaaab")
for match in matcher:
  print(match.start(),"......",match.group())

print("*******Quatifiers 5{n}********")
matcher=re.finditer("a{5}","abaabaaab")
for match in matcher:
  print(match.start(),"......",match.group())

print("*******functions******")
print("*****fullmatch()********")
import re
s='ababab'
m=re.fullmatch(s,"ababab")
if m!= None:
    print("Full String Matched")
else:
    print("Full String not Matched")

print("*****findall()*********")
l=re.findall("[0-9]","a7b9c5kz")
print(l)

print("*****sub()*********")
s=re.sub("[a-z]","#","a7b9c5k8z")
print(s)

print("*****subn()*********")
t=re.subn("[a-z]","#","a7b9c5k8z")
print(t)
print("The Result String:",t[0])
print("The number of replacements:",t[1])

print("*****split()*********")
l=re.split(",","sunny,bunny,chinny,vinny,pinny")
print(l)
for t in l:
    print(t)

print("*****symbol(^)*********")
s="Learning Python is Very Easy"
res=re.search("^Learn",s)
if res != None:
    print("String starts with Learn")
else:
    print("String Not starts with Learn")

print("*****symbol($)*********")
s="Learning Python is Very Easy"
res=re.search("Easy$",s)
if res != None:
    print("String ends with Easy")
else:
    print("String Not ends with Easy")

print("*****MObile number(10 or 11 or 12)digits")
s=input("Enter Mobile Number:") 
m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
if m!=None:
    print("Valid Mobile Number");
else:
    print("Invalid Mobile Number")
