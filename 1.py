fib = []
fibStr = ''
fib1 = 1
fib2 = 1
fib.append(fib1)
fib.append(fib2)
fibStr = fibStr + str(fib1) + str(fib2)
for i in range(498):
    fib1, fib2 = fib2, fib1 + fib2
    fib.append(fib2)
    fibStr += str(fib2)


print("Наивный алгоритм")
ans = [0]*100

for i in range(len(fibStr) - 1):
    ans[int(fibStr[i:i+2])] += 1

print('Числа встечающиеся наибольшое количество раз')
print('Число', ans.index(max(ans)), 'сколько раз:', max(ans))
ans[ans.index(max(ans))] = 0
print('Число', ans.index(max(ans)), 'сколько раз:', max(ans))
ans[ans.index(max(ans))] = 0
print('Число', ans.index(max(ans)), 'сколько раз:', max(ans))


print('')
print("Алгоритм Рабина-Карпа")
ans1 = [0]*100

hashs = []
for i in range(1, 10):
    for j in range(10):
        hashs.append(i*10+j)

for i in hashs:
    for j in range(len(fibStr)-1):
        if i == int(fibStr[j])*10+int(fibStr[j+1]):
            if i == int(fibStr[j:j+2]):
                ans1[int(fibStr[j:j+2])] += 1

print('Числа встечающиеся наибольшое количество раз')
print('Число', ans1.index(max(ans1)), 'сколько раз:', max(ans1))
ans1[ans1.index(max(ans1))] = 0
print('Число', ans1.index(max(ans1)), 'сколько раз:', max(ans1))
ans1[ans1.index(max(ans1))] = 0
print('Число', ans1.index(max(ans1)), 'сколько раз:', max(ans1))


print('')
print("Алгоритм Бойера-Мура")
ans2 = [0]*100

for i in range(10, 100):
    j = 0
    while j < len(fibStr)-1:
        if str(i)[1] == fibStr[j+1]:
            if str(i)[0] == fibStr[j]:
                ans2[int(fibStr[j:j+2])] += 1
                j += 1
            else:
                j += 1

        else:
            if fibStr[j+1] not in str(i):
                j += 2
            else:
                j += 1

print('Числа встечающиеся наибольшое количество раз')
print('Число', ans2.index(max(ans2)), 'сколько раз:', max(ans2))
ans2[ans2.index(max(ans2))] = 0
print('Число', ans2.index(max(ans2)), 'сколько раз:', max(ans2))
ans2[ans2.index(max(ans2))] = 0
print('Число', ans2.index(max(ans2)), 'сколько раз:', max(ans2))


print('')
print("Алгоритм  Кнута-Морриса-Пратта")
ans3 = [0]*100

for i in range(10, 100):
    if i % 11 == 0:
        pref = [0, 1]
    else:
        pref = [0, 0]

    j = 0
    while j < len(fibStr) - 1:
        if str(i)[0] == fibStr[j]:
            if str(i)[1] == fibStr[j+1]:
                ans3[int(fibStr[j:j+2])] += 1
                j += 1
            else:
                j += pref[1] + 1
        else:
            j += pref[0] + 1

print('Числа встечающиеся наибольшое количество раз')
print('Число', ans3.index(max(ans3)), 'сколько раз:', max(ans3))
ans3[ans3.index(max(ans3))] = 0
print('Число', ans3.index(max(ans3)), 'сколько раз:', max(ans3))
ans3[ans3.index(max(ans3))] = 0
print('Число', ans3.index(max(ans3)), 'сколько раз:', max(ans3))