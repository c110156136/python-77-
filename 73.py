n1=input("請輸入時間1:")
n1l=n1.split(":")
mi=int(n1l[0])*60+int(n1l[1])
se=mi*60+int(n1l[2])
print("時間1(",n1,")的格式轉會後為:",se,"秒")
n2=int(input("請輸入時間2:"))
se1=n2%60
mi1=(n2//60)%60
hr=(n2//60)//60
print("時間1(",n1,")=",hr,":",mi1,":",se1)