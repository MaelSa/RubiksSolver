from Scrambler import *

'''On prends pour piece buffer en coins la piece [2,3,6] 
    pour l'arrete buffer on prends la [1,3]'''

#Résolution des coins
#Il y a donc impossibilité des déplacement U,B,L



def echange_coins(coins):
        move = []

        if coins[5] == [2,3,6] or coins[5] == [3,6,2] or coins[5] == [6,2,3]:
            Coins_res = [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]
            n=0
            end_loop = False
            while n<8 and not end_loop:

                if coins[n] != Coins_res[n] and n != 5:
                    end_loop = True
                    number_of_the_corner = n
                n += 1
            if number_of_the_corner == 0:
                move = PLL_Y
            elif number_of_the_corner == 1:
                move = ["'R"]+PLL_Y+["R"]
            elif number_of_the_corner == 2:
                move = J_sym_mod
            elif number_of_the_corner == 3:
                move = ["R"] + J_sym_mod + ["'R"]
            elif number_of_the_corner == 4:
                move = ["F"] + PLL_Y + ["'F"]
            elif number_of_the_corner == 6:
                move = ["'F"] + J_sym_mod + ["F"]
            elif number_of_the_corner == 7:
                move = ["2D"] + J_sym_mod + ["2D"]
        elif coins[5] == [3,5,1]:
            move = ["'R"] + J_sym_mod + ["R"]
        elif coins[5] == [5,1,3]:
            move = ["F"] + J_sym_mod + ["'F"]
        elif coins[5] == [1,3,5]:
            move = PLL_Y
        elif coins[5] == [5,4,1]:
            move = J_sym_mod
        elif coins[5] == [1,5,4]:
            move = ["R"] + PLL_Y + ["'R"]
        elif coins[5] == [4,1,5]:
            move = ["'F"] + PLL_Y + ["F"]
        elif coins[5] == [5,3,2]:
            move = ["2F"] + J_sym_mod + ["2F"]
        elif coins[5] == [2,5,3]:
            move = ["F","'R"] + J_sym_mod + ["R","'F"]
        elif coins[5] == [3,2,5]:
            move = ["F"] + PLL_Y + ["'F"]
        elif coins[5] == [6,3,1]:
            move = ["2R"] + J_sym_mod + ["2R"]
        elif coins[5] == [3,1,6]:
            move = ["'R","F"] + J_sym_mod + ["'F","'R"]
        elif coins[5] == [1,6,3]:
            move = ["'R"] + PLL_Y + ["R"]
        elif coins[5] == [1,4,6]:
            move = ["'D"] + J_sym_mod + ["D"]
        elif coins[5] == [6,1,4]:
            move = ["'D","R"] + PLL_Y + ["'R","D"]
        elif coins[5] == [4,6,1]:
            move = ["R"] + J_sym_mod + ["'R"]
        elif coins[5] == [6,4,2]:
            move = ["2D"] + J_sym_mod + ["2D"]
        elif coins[5] == [2,6,4]:
            move = ["2D","R"] + PLL_Y + ["'R","2D"]
        elif coins[5] == [4,2,6]:
            move = ["2D","'F"] + PLL_Y + ["F","2D"]
        elif coins[5] == [2,4,5]:
            move = ["D"] + J_sym_mod + ["'D"]
        elif coins[5] == [4,5,2]:
            move = ["'F","R"]+ PLL_Y + ["'R","F"]
        elif coins[5] == [5,2,4]:
            move = ["'F"] + J_sym_mod + ["F"]
        return(move)

def resolution_coins(aretes,coins,centres):
    '''A partir d'une liste des coins mélangés , renvoie les différents movements  à effectuer pour résoudre les coins'''
    coins_solved = False
    Coins_res = [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]
    list_move = []
    nb_move=0
    nb_perm = 0

    while not coins_solved:

        Coins_res = [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]
        move = echange_coins(coins)
        list_move += move
        aretes,coins,centres = execute_move(move,aretes,coins,centres)
        nb_move+=1
        nb_perm += 1
        if coins == Coins_res:
            coins_solved = True
    return aretes,coins,centres,list_move,nb_move, nb_perm


#Résolution des arretes
#On ne bouge pas selon U,F,B et R (sauf U pour la PLL Jsym qui nécessite un U avant)

def echange_aretes(aretes):
    move = []

    if aretes[0] == [1,3] or aretes[0] == [3,1]:
        Arretes_res = [[1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 5], [3, 6], [4, 5], [4, 6]]
        n = 1
        end_loop = False
        while n < 12 and not end_loop:

            if aretes[n] != Arretes_res[n]:
                end_loop = True
                number_of_the_aretes = n
            n += 1
        if number_of_the_aretes == 1:
            move = ["2D","2L"] + PLL_T + ["2L","2D"]
        elif number_of_the_aretes == 2:
            move = ["'E","'L"] + PLL_T + ["L","E"]
        elif number_of_the_aretes == 3:
            move = ["E","L"] + PLL_T + ["'L","'E"]
        elif number_of_the_aretes == 4:
            move = PLL_T
        elif number_of_the_aretes == 5:
            move = ["2L"] + PLL_T + ["2L"]
        elif number_of_the_aretes == 6:
            move = ["'L"] + PLL_T + ["L"]
        elif number_of_the_aretes == 7:
            move = ["L"] + PLL_T + ["'L"]
        elif number_of_the_aretes == 8:
            move = PLL_J
        elif number_of_the_aretes == 9:
            move = J_sym
        elif number_of_the_aretes == 10:
            move = ["'M"] + PLL_J +["M"]
        elif number_of_the_aretes == 11:
            move = ["M"] + J_sym + ["'M"]
    elif aretes[0] == [3,6]:
        move = ["M"] + PLL_J + ["'M"]
    elif aretes[0] == [6,3]:
        move = ["'U"] + J_sym + ["U"]
    elif aretes[0] == [5,3]:
        move = PLL_J
    elif aretes[0] == [3,5]:
        move = ["'M"] + ["'U"] + J_sym + ["U"] + ["M"]
    elif aretes[0] == [2,3]:
        move = PLL_T
    elif aretes[0] == [3,2]:
        move = ["'L"] + ["E"] + ["'L"] + PLL_T + ["L"] + ["'E"] + ["L"]
    elif aretes[0] == [2,5]:
        move = ["'L"] + PLL_T + ["L"]
    elif aretes[0] == [5,2]:
        move = ["'E"] + ["L"] + PLL_T + ["'L"] + ["E"]
    elif aretes[0] == [2,6]:
        move = ["L"] + PLL_T + ["'L"]
    elif aretes[0] == [6,2]:
        move = ["E"] + ["'L"] + PLL_T + ["L"] + ["'E"]
    elif aretes[0] == [1,6]:
        move = ["2E"] + ["'L"] + PLL_T + ["L"] + ["2E"]
    elif aretes[0] == [6,1]:
        move = ["E"] + ["L"] + PLL_T + ["'L"] + ["'E"]
    elif aretes[0] == [1,5]:
        move = ["2E"] + ["L"] + PLL_T + ["'L"] + ["2E"]
    elif aretes[0] == [5,1]:
        move = ["'E"] + ["'L"] + PLL_T + ["L"] + ["E"]
    elif aretes[0] == [1,4]:
        move = ["2D"] + ["2L"] + PLL_T + ["2L"] + ["2D"]
    elif aretes[0] == [4,1]:
        move = ["'D"] + ["'M"] + PLL_J + ["M"] + ["D"]
    elif aretes[0] == [5,4]:
        move = ["'D"] + ["2L"] + PLL_T + ["2L"] + ["D"]
    elif aretes[0] == [4,5]:
        move = ["'M"] + PLL_J + ["M"]
    elif aretes[0] == [2,4]:
        move = ["2L"] + PLL_T + ["2L"]
    elif aretes[0] == [4,2]:
        move = ["D"] + ["'M"] + PLL_J + ["M"] + ["'D"]
    elif aretes[0] == [6,4]:
        move = ["2M"] + PLL_J + ["2M"]
    elif aretes[0] == [4,6]:
        move = ["M"] + ["'U"] + J_sym + ["U"] + ["'M"]
    return(move)


def resolution_aretes(aretes,coins,centres):
    Arretes_res = [[1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 5], [3, 6], [4, 5], [4, 6]]
    Coins_res = [[1, 3, 5], [1, 3, 6], [1, 4, 5], [1, 4, 6], [2, 3, 5], [2, 3, 6], [2, 4, 5], [2, 4, 6]]
    aretes_solved = False
    list_move = []
    #print('first')
    nb_move = 0
    nb_perm = 0
    while not aretes_solved:


        #print(aretes)
        #print(Arretes_res)
        #print('Lel')
        Arretes_res = [[1, 3], [1, 4], [1, 5], [1, 6], [2, 3], [2, 4], [2, 5], [2, 6], [3, 5], [3, 6], [4, 5], [4, 6]]
        move = echange_aretes(aretes)


        list_move += move
        aretes,coins,centres = execute_move(move,aretes, coins,centres)
        nb_move+=1
        nb_perm += 1
        if aretes == Arretes_res:

            aretes_solved = True
    return(aretes,coins,centres,list_move,nb_move,nb_perm)

