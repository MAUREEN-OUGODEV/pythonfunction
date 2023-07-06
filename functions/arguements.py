def year_of_birth (name,age):

    year =2023-age
    print(f"Hello {name}, you are born in {year}")

def my_country(country="Kenya"):
    print(f'Hello , you are from {country}')


def hello(*names) : 
 
 for name in names:
    print(f"hello,{name}")

def sum(*nums) :
   answer = 0
   for  num in nums:
      answer +=num
   return (answer)  
 
   
def multiplymany(**kwargs) :
    answer =1
    for num in kwargs.values():
       answer *= num  
    return answer

 


 #Assignment
def concatenate_args(*names):
    
   joining="".join(names)
   return(joining)


def concatenate_kwargs(**kwargs):
    answer =""
    for name in kwargs.values():
        answer += name
    return answer
