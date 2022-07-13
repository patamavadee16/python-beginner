#BMI = นน(kg)*(สส*สส(m))
weight = int(input("Enter your weight(kg) : "))
high = int(input("Enter your high(cm) : "))
high /= 100
BMI = weight/(high**2)
print("Your BMI = "+str(BMI))
if BMI <= 18.5 :
    print("ผอมเกินไป")
elif BMI>=18.6 and BMI<=22.9 :
    print("น้ำหนักปกติ")
elif BMI>=23 and BMI<=24.9 :
    print("น้ำหนักเกิน")
elif BMI>=25 and BMI<=29.9 :
    print("อ้วน")
else :
    print("อ้วนมาก")
print("คุณผอม") if BMI<=18.5 else print("ไม่ผอม")
