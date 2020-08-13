import re
#? in regular expressions(Regex) means that the group appears 0 or 1 time(s)
batRegex = re.compile(r'Bat(wo)?man') #? allows you to search for both batman and woman 
mo = batRegex.search('The advetures of Batman')
print(mo.group()) #will print batman 
ma = batRegex.search('Batwoman is better anyway')
print(ma.group()) #will print Batwoman
#ma = batRegex.search('Batwowowowoman is better anyway') To many "wo" ? mark means it can only appear once