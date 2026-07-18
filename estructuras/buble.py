for i in range(1, 6):  # 1, 2, 3, .... , 6
  for j in range(i):    # 0...i
    print("*", end="")
  print()

print("=========== opcion 2 ==============")
i=1
j=0
while i < 6:
  while j< i :
    print("*", end="")
    j=j+1
  print()
  i=i+1
  j=0



for i in range(3):
 if i % 2 == 0:
        print(f"{i} par")
 else:
        print(f"{i} impar")