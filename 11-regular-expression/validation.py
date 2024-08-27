# https://regex101.com/

import re

# [Email validator]
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'bb.com'
a = pattern.search(string)
print(a)



#[Password validator]
# at least 8 char long
# contain any sort letters, numbers %$#@
# end with a number

pattern2 = re.compile(r"^[a-zA-Z0-9%$#@]{8,}\d")
password = 'dsajfsadkjgak437598$%$$#8'
check = pattern2.fullmatch(password)
print(check)