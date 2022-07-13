#ตัวดำเนินการทางตรรกศาสตร์
x = 1
y = 2
#F and T
z = (x>3) and (y>1)
print(type(z))
print("F and T :"+str(z))
#T and T
z = (x>0) and (y>1)
print("T and T :"+str(z))
#T and F
z = (x>0) and (y>3)
print("T and F :"+str(z))
#F and F
z = (x>1) and (y>3)
print("T and T :"+str(z))
#F or T
z = (x>3) or (y>1)
print("F or T :"+str(z))
#F or F
z = (x>1) or (y>3)
print("T or T :"+str(z))
#T or F
z = (x>0) or (y>3)
print("T or F :"+str(z))
#T or T
z = (x>0) or (y>1)
print("T or T :"+str(z))
#not T =F
z = not((x>0) and (y>1))
print("not True :"+str(z))
#not F =T
z = not((x>1) or (y>3))
print("not False :"+str(z))