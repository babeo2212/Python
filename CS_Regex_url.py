import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://www.etsy.com/listing/849036484/personalized-1-year-anniversary?ref=shop_home_feat_1&pro=1
'''

pattern = re.compile(r'https?://(www.)?(\w+)(\.\w+)') 

# subbed_urls = pattern.sub(r'\2\3', urls) # --> to subsitute group 2 and 3 in pattern, matchin in urls
# print(subbed_urls)
matches = pattern.search(urls)
print(matches)
# for match in matches:
#     print(match)