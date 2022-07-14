name = "Patamavadee : 20"
name1 = "bangkok"
nickname = "pear"
thainame ="นางสาวปฐมาวดี"
print(name[1:9])
print(name[-1])
name.strip()
print(name)
name.lstrip()
print(name)
print(name.upper())
print(name.lower())
print(name1.capitalize())
text="ชื่อจริง :{0}\tชื่อเล่น :{1}\t ที่อยู๋ :{2}"
print(text.format(name,nickname,name1))
print(name.count("a"))
print(name1.replace("bankok","monza",1))
if thainame.startswith("นางสาว") :
    print("คุณอายุมากกว่า15")