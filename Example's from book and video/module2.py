import re
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #use parenthesis to seperate what you want searched for. You can put groups inside of groups
mo = phoneRegex.search('My number is 415-555-4545')
print(mo.group(1)) ##using the number 1 in the here will return area code, 2 will return 7 didgit number
print(mo.group(2))

#find just a prefix
batRegex = re.compile(r'Bat(man|mobile|copter|bat)') #the pipt character"|" can seperate the sufffixes 
ma = batRegex.search('Did Bats want the Batcopter the Batmobile or the Batbat')
print(ma.group())