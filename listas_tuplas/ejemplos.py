#      [ 0, 1 , 2 ,  3, 4 ,  5,  6,  7, 8 , ] 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 100, 12]
# num[i, j-1 ]
# i = indice incial
# j = indice hasta donde queremos obtener 
#resultado = nums[2:6]
#resultado = nums[:7]
#resultado = nums[6:]
#resultado = nums[::3]
# resultado = nums[::-3]
resultado = nums[1:10:3] # inicio , final, incremento
print(resultado)
