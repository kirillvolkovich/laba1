file = open('orig.txt', encoding="utf8")
wiki = open('wiki.txt', encoding="utf8")
f = wiki.read()
s = file.read()
sum = 0
a = s.split(' ')
i = 0
while i < len(a) - 2:
    if a[i] + ' ' + a[i + 1] + ' ' + a[i + 2] in f:
        sum += len(a[i]) + len(a[i + 1]) + len(a[i + 2])
        i += 3
    else:
        i += 1
all_symbols = 0
for k in a:
    all_symbols += len(k)
print('Плагиат', (sum / all_symbols) * 100, '%')

