#start
temps: list[int] = [21, 30, -999, 26, -999, 17, 33, -999, 28]
print('count:', len(temps))
print('first three:', temps[:3])
print('last three:', temps[-3:])
print('every second:', temps[::2])
while -999 in temps:
    temps.remove(-999)
print('cleand:', temps)
print('dropped the first reading:', temps.pop(0))
temps.append(31)
print('after append:', temps)
max_temp = temps[0]
for temp in temps:
    if temp > max_temp:
        max_temp = temp
min_temp = temps[0]
for temp in temps:
    if temp < min_temp:
        min_temp = temp
sum_temp = 0
for temp in temps:
    sum_temp += temp
avg = sum_temp / len(temps)
print('max:',max_temp, end=' ')
print('min:',min_temp, end=' ')
print('sum:',sum_temp, end=' ')
print(f'average: {avg:.2f}', end=' ')
print()
for temp in temps:
    if temp > avg:
        print('above average:', temp)
#stop
