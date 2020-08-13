import re


vowelRegex = re.compile(r'[aeiouAEIOU]') #same as r'(a|e|i|o|u). use brackets to look for more than 1 character
print(vowelRegex.findall("Coming straight outta Compton a crazy motherfucker named Ice Cube"))
#re.I ignores case put it after the raw string
    #ex. the_list = re.compile(r'hello', re.I) will compile all instances of hello, HelLo HELLo, etc.

vowelRegex = re.compile(r'[^aeiouAEIOU]') #^ means DO NOT find these. A negative find. Includes spaces and punctuation
print(vowelRegex.findall("Coming straight outta Compton a crazy motherfucker named Ice Cube"))