#knight's possible moves
x0=int(input( " x0= "))
y0=int(input( " y0= "))

coordinates=[x0,y0] 
moves=[]
for a in range(-2,3): 
  if a==0: 
    continue 
  for b in range(-2,3):
    if b==0 or abs(b)==abs(a): 
      continue 
    else: 
      moves.append([x0+a, y0+b])

for x in moves:
  print(x) 