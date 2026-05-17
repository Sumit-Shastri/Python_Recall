# functions with *args and **kwargs

# *args

def average(*n):

    total = 0
    avg = 0

    for i in n:
        total = total + i
        avg = total / len(n)
        
    return avg

ans = average(4, 5, 7, 8)
print(ans)

# **kwargs

def info(**names):

    print(f"Good Morning, {names["fname"]} {names["mname"]} {names["lname"]}")

info(fname = "Sumit", mname = "Satishkumar", lname = "Shastri")