# 將清單中相連的字串分割成不同字串

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    s = line.split(' ')
    time = s[0][:5] # split把line變清單並宣告為s, s清單中的第0個index為字串
    name = s[0][5:] # 清單切割可用在字串上, 故可以把s[0]再進行切割
    print(time)
    print(name)