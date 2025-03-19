print('#2.1')
print(100, '+', 200, '=', 100 + 200)
print(200, '+', 300, '+', 400, '=', 200+300+400)
print('')
print('#2.2')
weight = 30
height = 60
print(weight)
print(height)
print('')
print('#2.3')
width = 30
height = 60
area = width * height
print(area)
print('')
print('#2.4')
width = 40
height = 20
area = width * height * 1/2
print(area)
print('')
print('#2.5')
print('밑변 길이를 사용자가 입력하는 방법')
r=int(input('정사각형의 밑변을 입력하시오:'))
print('#2.6')
t=1+2+3+4+5+6+7+8+9+10
print('1에서 10까지의 합:', t)
print('')
print('#2.7')
t=1*2*3*4*5*6*7*8*9*10
print('10! =', t)
print('')
print('#2.8')
print('a  n  a**n')
for a in range(2, 7):
    n = 2
    print(a, n, a**n)
    print('')
print('#2.9')
print('섭씨', '화씨')
for C in range(0, 51, 10):
    F = (9/5) * C + 32
    print(C, F)
print('')
print('#2.10')
celsius = int(input('섭씨 온도를 입력하세요:'))
fahrenheit = (celsius * 9/5) + 32
print('섭씨', celsius, '도는 화씨', fahrenheit, '도입니다.')
print('')
print('#2.11')
fahrenheit = int(input('화씨 온도를 입력하세요:'))
celsius = (fahrenheit - 32) * 5/9
print('화씨', fahrenheit, '도는 섭씨', celsius, '도입니다.')
print('')
print('#2.12')
r = 11
PI = 3.141592
s1 = 2*r*PI
s2 = (r**2)*PI
print('원의 둘레:', s1)
print('원의 넓이:', s2)
print('')
print('#2.13')
r=int(input('반지름을 입력하세요:'))
PI=3.141592
s1=2*r*PI
s2=(r**2)*PI
print('원의 둘레:', s1)
print('원의 넓이:', s2)
print('')
print('#2.14')
for i in range(1, 11):
    print(f'{i}의 제곱근 = {repr(i**0.5)}')
    print('')
print('#2.15')
a=int(input('밑변을 입력하세요:'))
b=int(input('높이를 입력하세요:'))
c=(a**2 + b**2)**0.5
print('빗변:', c)
print('')
print('#2.16')
import cmath
z1=complex(1,2)
rotation_90=cmath.exp(1j*cmath.pi/2)
z1_rotated=z1*rotation_90
print(f'회전하기 전: {z1}')
print(f'90도 회전한 후: {z1_rotated}')
z2=complex(1,2)
rotation_30=cmath.exp(1j*cmath.pi/6)
z2_rotated=z2*rotation_30
print(f'회전하기 전: {z2}')
print(f'30도 회전한 후: {z2_rotated}')
print('')
print('#2.17')
result = [2 << i for i in range(0,10)]
print(*result, sep=' ')
print('')
print('#2.18')
n = int(input('정수를 입력하세요:'))
if n % 2 == 0:
    print('이 수가 짝수인가요? True')
else:
    print('이 수가 짝수인가요? False')
print('')
print('#2.19')
n = int(input('정수를 입력하세요:'))
result = 0 <= n <= 100 and n % 2 == 0
print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?', result)
print('')
print('#2.20')
a = 5 & 6
b = 5 | 6
c = 5 ^ 6
print(bin(5),'&',bin(6),bin(a))
print(bin(5),'|',bin(6),bin(b))
print(bin(5),'^',bin(6),bin(c))
print('')
print('#2.21')
n=int(input('정수를 입력하세요:'))
b=bin(n)
print(n, '의 2진수 값:', b)
bn = bin(~n)
print(n, '의 비트단위 부정값:', bn)
print('')
print('#2.22')
a = int(input('정수 a를 입력하시오:'))
b = int(input('정수 b를 입력하시오:'))
print('a/b의 몫:', a//b)
print('a/b의 나머지:', a%b)
print('')
print('#2.23')
n = int(input('세 자리 정수를 입력하시오:'))
백의자리 = n // 100
십의자리 = (n%100) // 10
일의자리 = n % 10
print('백의 자리:', 백의자리)
print('십의 자리:', 십의자리)
print('일의 자리:', 일의자리)
print('')
print('#2.24')
n = int(input('세 자리 정수를 입력하시오:'))
백의자리 = n // 100
십의자리 = (n%100)//10
일의자리 = n%10
print(일의자리)
print(십의자리)
print(백의자리)
print('')
