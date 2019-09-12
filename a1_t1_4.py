def f_to_k(Jimmy):
    # Forumla = (f-32)*5/9+273.15
    # I took this formula from this link: http：//contractor quote
    k = (f-32)*5/9+273.15
    return k

f = 60
k = f_to_k(f)

print("Fahrenheit is" + str(f) + "is" + str(k) + "in Kelvin")
