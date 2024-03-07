"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = list("fooziman")
    new_result = ["F","0","0","Z","1","M","@","N"]

    for i in range(len(result)):
        result[i] = new_result[i]
    print(result)
    
    return result


fn_hack_10()



