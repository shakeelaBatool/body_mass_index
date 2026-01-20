def my_fun(a,b):
    bmi= weight/height**2
    print(bmi)                  
   
    return bmi                                   #return output
weight=int(input("Enter weight in kg : ")) 
height=float(input("Enter height in meter: "))
resent=my_fun(weight,height)                     # function call
print(resent)    

print(round(resent,2))                           # roundoff 

