def c_to_k(Jimmy):
    #Forumla = (c + 273.15 )
    # I took this formula from this link: //contractor quote
    k = (c + 273.15)
    return k

c = 2
k = c_to_k(c)

print("Celius of" + str(c) + "is" + str(k) + "in Keivin")
