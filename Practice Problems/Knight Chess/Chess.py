# cook your dish here
def knight(x, y):
    offsets = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    for dx, dy in offsets:
        nx = x + dx
        ny = y + dy
        attacked.add((nx, ny))

for _ in range(int(input())):
  n = int(input())
  attacked = set()
  for i in range(n):
    x, y = map(int, input().split()) 
    knight(x, y)
  a, b = map(int, input().split()) 
  ans = 'YES'
  offsets = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
  for da, db in offsets:
    nx = a + da
    ny = b + db
    if (nx, ny) not in attacked:
      ans = 'NO'
      break
  print(ans)
