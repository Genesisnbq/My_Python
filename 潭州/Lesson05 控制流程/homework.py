#  打印 9*9乘法表
for i in range(1, 10):  # 因为类似于切片, 所以所以+1
    for j in range(1, i + 1):
        print('%d * %d = %d' % (j, i, i * j), end='\t')
    print('')

# 对一段英文文字进行词频统计，如（可自行选择英文内容）
print('=' * 20)

for i in range(1, 10):
    for j in range(1, i+1):
        print('{} * {} = {}'.format(j, i, i*j), end='\t')
    print("")

# Chapter = “””
# I have a dream that one day this nation will rise up and live out the true meaning of its creed:
# "We hold these truths to be self-evident, that all men are created equal.I have a dream that
# one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners
# will be able to sit down together at the table of brotherhood.I have a dream that one day even
# the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat
# of oppression, will be transformed into an oasis of freedom and justice.
# “””
# 要求：按倒序 输出出现次数最多的前3个单词和它出现的次数

# 提示：需要综合运用，字符串，列表，字典，控制流程等基础知识

print('=' * 20)

str = """I have a dream that one day this nation will rise up and live out the true meaning of its creed:
"We hold these truths to be self-evident, that all men are created equal.I have a dream that 
one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners
will be able to sit down together at the table of brotherhood.I have a dream that one day even 
the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat 
of oppression, will be transformed into an oasis of freedom and justice."""

word = {}
cur = ""
for i in range(0, len(str) + 1):
    while ((str[i] != ',' or str[i] != '.' or str[i] != '"' or str[i] != ' ') and i <= len(str)):
        cur += str[i]
        i += 1
    if word.get(cur, False) == False:
        word.setdefault(cur, 1)
    else:
        word.setdefault(cur, word[cur]+1)
    cur = ""
sorted(word.keys())
# for i in range(0, 3):
#     print()
