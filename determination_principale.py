from math import pi,degrees
import time


def determination_principale(numerateur,denominateur):
    from math import pi


    if numerateur<denominateur and numerateur > 0:
        print(f"\n\n\nla détermination principale est {numerateur}π/{denominateur}")
    elif numerateur >0:
        quotient = numerateur//denominateur
        if quotient%2==0:
            reste = numerateur%denominateur
            print(f"{quotient}π + {reste}π/{denominateur}")
        else:
            reste = numerateur%denominateur
            print(f"\n<=>{numerateur//denominateur}π + {reste}π/{denominateur}\n<=>{(numerateur//denominateur)+1}π - π + {reste}π/{denominateur}\n<=> {quotient+1}π {reste - denominateur}π/{denominateur}")
            if(reste+denominateur<= denominateur):
                print(f"\net c'est aussi égale à\n\n<=>{numerateur//denominateur}π + {reste}π/{denominateur}\n<=>{(numerateur//denominateur)-1}π + π + {reste}π/{denominateur}\n<=>{quotient-1}π + {reste + denominateur}π/{denominateur}")
    else:
        quotient = numerateur//denominateur
        if quotient%2==0:
            reste = numerateur%denominateur
            print(f"{quotient}π + {reste}π/{denominateur}")
        else:
            reste = numerateur%denominateur
            print(f"\n<=>{numerateur//denominateur}π + {reste}π/{denominateur}\n<=>{(numerateur//denominateur)+1}π - π + {reste}π/{denominateur}\n<=>{quotient+1}π {reste - denominateur}π/{denominateur}")
            if(reste+denominateur<= denominateur):
                print(f"\net c'est aussi égale à\n\n<=>{numerateur//denominateur}π + {reste}π/{denominateur}\n<=>{(numerateur//denominateur)-1}π + π + {reste}π/{denominateur}\n<=>{quotient-1}π + {reste + denominateur}π/{denominateur}")

def degres_to_radians(degres):
    from math import radians,pi

    def fraction_approximation(decimal):
        epsilon = 1e-6  # Précision souhaitée
        num = 1
        den = 1
        while abs(decimal - num / den) > epsilon:
            if num / den < decimal:
                num += 1
            else:
                den += 1
        return num, den

    radians = radians(degres/pi)
    num, den = fraction_approximation(radians)
    print(f"{degres}*180/π = {num}π/{den} rad")

def radian_to_degres(numerateur,denominateur):
    print(f"({numerateur}/{denominateur})*π/180 = {round(degrees((numerateur/denominateur)*pi))}°")

def cours():
    print("relation fondamental :\ncos(x)2+sin(x)2=1\n\ncos(b) = ajacent/hypoténuse \n= sin(c)\nsin(b) = opposé/hypoténuse \n= cos(b)\ntan(b) = sin(b)/cos(c)\n=opposé/adjacent = 1/tan(c)")


#lancement du programme
try:
    while True:
        try:
            rep = int(input("\nveuillez choisir votre type de calcul\n1) degrés => radians\n2) radians => degrés\n3) détermination principale\n"))
            if rep == 1:
                while True:
                    try:
                        degres_to_radians(int(input("entrer le nbr de degrées :")))
                    except:
                        print("\nla valeur renseigné n'est \npas sous la bonne forme")
                        break
            elif rep == 2:
                while True:
                    try:
                        radian_to_degres(int(input("\nentrer le numérateur :")), int(input("entrer le dénominateur :")))
                    except:
                        print("\nla valeur renseigné n'est \npas sous la bonne forme")
                        break
            elif rep == 3:
                while True:
                    try:
                        determination_principale(int(input("\nentrer le numérateur :")), int(input("entrer le dénominateur :")))
                    except:
                        print("\nla valeur renseigné n'est \npas sous la bonne forme")
                        break
            elif rep == 4:
                cours()
                time.sleep(10)
            else:
                print("choisissez un calcul dispo")
        except:
            print("\nune erreur est survenue\n veuillez reesayer\n")
            break
except:
    pass


    