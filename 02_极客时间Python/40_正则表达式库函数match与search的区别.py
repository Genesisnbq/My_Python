import re
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.search('aa2018-05-10bb'))
