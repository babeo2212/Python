import re
# help(re)
# dir(re)
text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
abc
Ha HaHa

MetaCharacters (Need to be escaped)
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
900.555.1234
800.555.1234

Mr. Schafler
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
pat
sat
bat

'''
sentence = 'Start a sentence and then bring it to an end'

# print(r'\tTab') # 'raw' string interpretes a whole string

# pattern = re.compile(r'abc') # search for abc <re.Match object; span=(1, 4), match='abc'>
# pattern = re.compile(r'\.') # special character needs to be escaped by '\'. If (r'.') will search for everything in a string
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\bHa') #(1st, 2nd Ha)<re.Match object; span=(70, 72), match='Ha'>,<re.Match object; span=(73, 75), match='Ha'>
# pattern = re.compile(r'\BHa') #(3rd Ha)<re.Match object; span=(75, 77), match='Ha'>
# pattern = re.compile(r'^Start') #-->Search at the begging
# pattern = re.compile(r'end$') #-->Search at the end of the string
# pattern = re.compile(r'start', re.IGNORECASE) # flag to find upper or lowercase

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #inside the bracket only match 01 character
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') #patterns that match only 800 or 900
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # search for thee exact 3 digits.3 digits.4 digits

# pattern = re.compile(r'[1-5]') # specify a range between 1 and 5.
# pattern = re.compile(r'[a-zA-Z0-9]') # specify a range between a and z, A and Z, 0 and 9.
# pattern = re.compile(r'[^a-zA-Z0-9]') # specify a range NOT between a and z, A and Z, 0 and 9.
# pattern = re.compile(r'[^b]at') # 'cat', 'pat', 'sat' but not 'bat'

# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # using group inside parentheses ()
# pattern = re.compile(r'M[rs]\w*\.?\s[A-Z]\w*') 
pattern = re.compile(r'\d*') 
matches = pattern.finditer(text_to_search) #to find 1 match of abc letters

for match in matches:
    print(match)

# with open('Rex_data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)
