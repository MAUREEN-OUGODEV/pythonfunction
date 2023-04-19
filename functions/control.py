def even_numbers():
    x=range(10)
    for i in x:
        if i%2==0:
            print(i)



def odd_number():
    x=range(20)
    for i in x :
        if(i%2!=0):
            print(f"{i}")
        else:
            print(i)    


def divisible_by_five() :
    x=range(50) 
    for i in  x:
       if(i%5==0) :
           print(f"{i} is divisible by 5")   
       else:
           print(f"{i} is not divisible by 5")  


def multiply_comparison():
    x= range(50)
    for i in x:
        if(i%5==0):
            print(f"{i} is divisible by 5")
        elif(i%7==0):
            print(f"{i} is divisible by 7") 
        elif(i%9==0):
            print(f"{i} is divisible by 9")   
        else:
            print(f"{i} is not divisiible by 5,7,9")      

def odd_or_even():
    x =range(20)
    for i in x:
        if(i%2==0 and i%3==0):
            print(f"{i} is divisible by both 3 and 2 ")
        elif(i%2==0 or i%3 ==0):
            print(f"{i} is divisible by either 2 or 3")
        else:
            print(f"{i} is not divisible br either 2 or3")    



