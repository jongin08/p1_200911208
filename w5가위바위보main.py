sel1 = raw_input("Do rock,scissor,paper : ")
sel2 = raw_input("Do it again : ")

def rsp(h1,h2):
    if h1 == h2:
        res="draw."
    elif h1 == 'scissor' and h2 == 'rock':
        res="rock won."
    elif h1 == 'scissor' and h2 == 'paper':
        res="scissor won."
    elif h1 == 'rock' and  h2 == 'paper':
        res="paper won."
    elif h1 == 'rock' and  h2 == 'scissor':
        res="rock won."
    elif h1 == 'paper' and h2 == 'rock':
        res="paper won."
    elif h1 == 'paper' and h2 == 'scissor':
        res="scissor won."
    else:
        res="You did not enter one of 'rock,scissor or paper'"
    return res

rsp(sel1,sel2)