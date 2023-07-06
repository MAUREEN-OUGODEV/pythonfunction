def while_loop():
    x=1
    while(x<10):
        print("hello")
        x+=1

def break_statement():
    x=1
    while(x<10):
        print(f"hello")
        x+=1
        if(x==5):
            break



def continue_statement():
    x=0
    while x <=20:
      x+=1
      if x %3==0:
          continue
      print(x)

continue_statement()


