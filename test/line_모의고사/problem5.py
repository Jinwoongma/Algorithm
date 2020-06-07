
def get_factorial(num):
  if num == 1 or num == 0:
    return 1
  else:
    return num * get_factorial(num - 1)

R, C = map(int, input().split())
ey, ex = map(int, input().split())
if ey < 0 or ey >= R or ex < 0 or ex >= C:
  print('fail')
elif ey == 0 and ex == 0:
  print('fail')
else:
  print(ey + ex)
  print(get_factorial(ey + ex) // (get_factorial(ey) * get_factorial(ex)))