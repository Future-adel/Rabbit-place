
print("Welcome to place the rabbit")
grille = [["🌴","🌴","🌴"],
          ["🌴","🌴","🌴"],
          ["🌴","🌴","🌴"]]
rabbit = "🐇"
row = ''
col = ''
direct = input("where should the rabbit go ? Please choose a row and column :")
if direct and  len(direct) == 2 and int(direct) <= 22:
    chaine = direct.split()
    row = int(chaine[0][0])
    col = int(chaine[0][1])
    grille[row][col] = rabbit
    print("Success....")
    print(grille)
else:
    print("Please choose deux digits entre ces trois chiffres; 0, 1 ou 2 without space")