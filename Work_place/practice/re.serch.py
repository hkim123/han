import re

patterns = ['software testing', 'guru99']
text = 'software testing is fun'

for pattern in patterns:
    print('looking for "%s" in "%s" ->' % (pattern, text), end = '') #end = '' means ends without newline, which means it add next line.this case, add found a match or no match without new line

    if re.search(pattern, text):
        print('found a match!')

    else:
        print('no match')