f=(int("First"))
s=(int("second"))
L=[1,2,3]
try:
     result=f/s
     print(L[1])
except ZeroDivisionError as e:
    print("0 se divide mat kar")
except IndexError as e:
    print("khatm")
except Exception as e:
    print("error hai")
else:
    print(result)
finally:
    print("DB close")
