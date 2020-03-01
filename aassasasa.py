import re

print(re.match(r'(?:\w)\1{2}', 'aaa').group())