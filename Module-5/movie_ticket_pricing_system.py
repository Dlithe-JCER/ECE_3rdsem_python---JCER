age=int(input("enter an age"))
show_time=int(input("enter a show-time in [1(matinee)-2(evening)]"))
if age <0 or show_time not in [1,2]:
    print("invalid input try again ")
else:    
    if age<5:
        price=0
    elif age<=18:
        price=100  
    elif age <= 59:
        price= 150
    else:
        price=120    
    if show_time==1:
        price=price-(price * 0.10)
    print("total price",int(price))    

