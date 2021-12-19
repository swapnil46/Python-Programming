# sWAP cASE

# HackerRank problem solved using Python.

def swap_case(s):
    n=len(s)
    t=""
    for i in range(n):
        u=s[i]
        if u.isupper()==True:
            t+=u.lower()
        elif u.islower()==True:
            t+=u.upper()
        else:
            t+=u
    return t
