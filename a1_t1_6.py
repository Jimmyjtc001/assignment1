def k_to_f(Jimmy):
    # Forumla = (k-273.15)*9/5+32
    # I took this formula from this link: http：//contractor quote
    f = (k-273.15)*9/5+32
    return f

k = 288
f = k_to_f(k)

print("Kevin is" + str(k) + "is" + str(f) + "in Fahrenheit")
