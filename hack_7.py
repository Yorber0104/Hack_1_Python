"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    inicio = 5
    while(inicio >= 0):
        result.append(inicio)
        inicio -= 1
    return result  


r =fn_hack_7()
print(r)


