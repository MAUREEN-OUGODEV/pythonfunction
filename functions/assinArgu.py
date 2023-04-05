def concatenate_args(*names):
    
   joining="".join(names)
   return(joining)


def concatenate_kwargs(**kwargs):
    answer =""
    for name in kwargs.values():
        answer += name
    return answer
