def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: # -sig可去除'/ufeff'符號
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None # 代表'剛開始沒有', 否則如果開頭不是人名會crash(當掉)
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: # person有值才做這行
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main() # 最先被執行