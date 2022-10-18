
# ex


#ex
#parents = ("Marc", "Caroline")

# ex
#print("2" + " + " + "6" + " + " + "3")
#print(2, 6, 3, sep=" + ")

#ex
#from cmath import pi
#from pickle import FALSE

#ray=int(input("ENTREZ LE RAYON DE LA SPHERE: "))

#vol=(4*pi)/3 *ray**3

#print("LE VOLUME DE LA SPHERE EST DE ",vol)
#print("MERCI D'AVOIR CHOISIR RL INDUSTRIES")

#ex

done=False
while(not done):
    val=""
    while not isinstance(val,int):
        val=input("entrez un nombre: ")
    if(val==10):
        print("vous avez entré 10, BRAVO!")
    elif(val<10):
        print("votre nombre est trop petit, DOMMAGE")
    else:
        print("votre nombre est trop grand, PAS DE BOL")

#autre

class test:
    field=323

    def fn1():
        return 1