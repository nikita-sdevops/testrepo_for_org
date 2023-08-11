def do_something(a,b,c,d): return c*a-b+d if (a > 10 and b < c or d == 0) else (a+b-c)*d

a = [1, 2, '3', 4, 5]
result = 0
for i in range(len(a)):
  if type(a[i]) is str:
    a[i] = int(a[i])
  result += a[i]
print("Result is " + str(result + do_something(12, 4, 5, 6) * 3 - 4))
