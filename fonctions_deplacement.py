from ressources import *
from graphic_interpreter import*



def right_prime(arretes, coins):
    A = coins[0]
    A[0], A[1], A[2] = A[0], A[2], A[1]
    coins[0] = A
    A = coins[1]
    A[0], A[1], A[2] = A[0], A[2], A[1]
    coins[1] = A
    A = coins[2]
    A[0], A[1], A[2] = A[0], A[2], A[1]
    coins[2] = A
    A = coins[3]
    A[0], A[1], A[2] = A[0], A[2], A[1]
    coins[3] = A
    coins[0],coins[1], coins[2], coins[3] = coins[1], coins[3], coins[0], coins[2]
    arretes[0], arretes[1], arretes[2], arretes[3] = arretes[3], arretes[2], arretes[0], arretes[1]
    return (arretes,coins)


def right(arretes, coins):
    for i in range(0,3):
        arretes, coins = right_prime(arretes, coins)
    return arretes, coins


def left_prime(arretes , coins):
    coins_cinq = coins[4]
    coins_cinq[0], coins_cinq[1], coins_cinq[2] = coins_cinq[0], coins_cinq[2], coins_cinq[1]
    coins[4] = coins_cinq
    coins_six = coins[5]
    coins_six[0], coins_six[1], coins_six[2] = coins_six[0], coins_six[2], coins_six[1]
    coins[5]=coins_six
    coins_sept = coins[6]
    coins_sept[0], coins_sept[1], coins_sept[2] = coins_sept[0], coins_sept[2], coins_sept[1]
    coins[6] = coins_sept
    coins_huit = coins[7]
    coins_huit[0], coins_huit[1], coins_huit[2] = coins_huit[0], coins_huit[2], coins_huit[1]
    coins[4], coins[5], coins[6], coins[7] = coins[6], coins[4], coins[7], coins[5]
    arretes[4], arretes[5], arretes[6], arretes[7] = arretes[6], arretes[7], arretes[5], arretes[4]
    return (arretes,coins)


def left(arretes, coins):
    for i in range(0,3):
        arretes, coins = left_prime(arretes, coins)
    return(arretes , coins)


def up_prime(arretes, coins):
    liste_coins = [0,1,4,5]
    liste_arretes = [0,4,8,9]
    #coins
    for i in liste_coins:
        coins_1_2_5_6 = coins[i]
        coins_1_2_5_6[0], coins_1_2_5_6[1], coins_1_2_5_6[2] = coins_1_2_5_6[2], coins_1_2_5_6[1], coins_1_2_5_6[0]
        coins[i] = coins_1_2_5_6
    coins[0], coins[1], coins[4], coins[5] = coins[4], coins[0], coins[5], coins[1]
    for j in liste_arretes:
        arretes_1_5_9_10 = arretes[j]
        arretes_1_5_9_10[0], arretes_1_5_9_10[1] = arretes_1_5_9_10[1], arretes_1_5_9_10[0]
        arretes[j] = arretes_1_5_9_10
    arretes[0], arretes[4], arretes[8], arretes[9] = arretes[8], arretes[9], arretes[4], arretes[0]
    return (arretes,coins)


def up(arretes, coins):
    for i in range(0,3):
        arretes, coins = up_prime(arretes, coins)
    return arretes, coins


def down(arretes,coins):
    liste_coins=[2,3,6,7]
    liste_arretes=[1,5,10,11]
    for i in liste_coins:
        coins_trois_quatre_sept_huit = coins[i]
        coins_trois_quatre_sept_huit[0], coins_trois_quatre_sept_huit[1], coins_trois_quatre_sept_huit[2] = coins_trois_quatre_sept_huit[2], coins_trois_quatre_sept_huit[1], coins_trois_quatre_sept_huit[0]
        coins[i] = coins_trois_quatre_sept_huit
    coins[2], coins[3], coins[6], coins[7] = coins[6], coins[2], coins[7], coins[3]
    for j in liste_arretes:
        arrete_trois_quatre_onze_douze = arretes[j]
        arrete_trois_quatre_onze_douze[0], arrete_trois_quatre_onze_douze[1] = arrete_trois_quatre_onze_douze[1], arrete_trois_quatre_onze_douze[0]
        arretes[j] = arrete_trois_quatre_onze_douze
    arretes[1], arretes[5], arretes[10], arretes[11] = arretes[10], arretes[11], arretes[5], arretes[1]
    return (arretes,coins)


def down_prime(arretes, coins):
    for i in range(0,3):
        arretes, coins = down(arretes, coins)
    return arretes, coins


def front_prime(arretes,coins):
    liste_coins=[0,2,4,6]
    for i in liste_coins:
        coins_1_3_5_7 = coins[i]
        coins_1_3_5_7[0], coins_1_3_5_7[1], coins_1_3_5_7[2] = coins_1_3_5_7[1], coins_1_3_5_7[0], coins_1_3_5_7[2]
        coins[i] = coins_1_3_5_7
    coins[0], coins[2], coins[4], coins[6] = coins[2], coins[6], coins[0], coins[4]
    arretes[2], arretes[6], arretes[8], arretes[10] = arretes[10], arretes[8], arretes[2], arretes[6]
    return (arretes,coins)


def front(arretes, coins):
    for i in range(0,3):
        arretes, coins = front_prime(arretes, coins)
    return arretes, coins


def back_prime(arretes,coins):
    liste_coins = [1,3,5,7]
    liste_arretes = [3,7,9,11]
    for i in liste_coins:
        coins_2_4_6_8 = coins[i]
        coins_2_4_6_8[0], coins_2_4_6_8[1], coins_2_4_6_8[2] = coins_2_4_6_8[1], coins_2_4_6_8[0], coins_2_4_6_8[2]
        coins[i] = coins_2_4_6_8
    coins[1], coins[3], coins[5], coins[7] = coins[5], coins[1], coins[7], coins[3]
    arretes[3], arretes[7], arretes[9], arretes[11] = arretes[9], arretes[11], arretes[7], arretes[3]
    return (arretes,coins)


def back(arretes, coins):
    for i in range(0,3):
        arretes, coins = back_prime(arretes, coins)
    return arretes, coins


def middle(arretes,centres):
    liste_centres = [2,3,4,5]
    liste_arretes = [8,9,10,11]
    centres[2], centres[3], centres[4], centres[5] = centres[5], centres[4], centres[2], centres[3]
    for i in liste_arretes:
        arretes9_10_11_12 = arretes[i]
        arretes9_10_11_12[0] , arretes9_10_11_12[1] = arretes9_10_11_12[1], arretes9_10_11_12[0]
        arretes[i] = arretes9_10_11_12
    arretes[8] , arretes[9] , arretes[10] , arretes[11] = arretes[9] , arretes[11] , arretes[8] , arretes[10]
    return(arretes,centres)


def middle_prime(arretes,centres):
    for i in range(0,3):
        arretes,centres = middle(arretes,centres)
    return arretes, centres


def equator(arretes,centres):
    liste_arretes = [2,3,6,7]
    centres[0], centres[1], centres[4], centres[5] = centres[4], centres[5], centres[1], centres[0]
    for i in liste_arretes:
        arrete3_4_7_8 = arretes[i]
        arrete3_4_7_8[0], arrete3_4_7_8[1] = arrete3_4_7_8[1], arrete3_4_7_8[0]
        arretes[i] = arrete3_4_7_8
    arretes[2], arretes[3], arretes[6], arretes[7] = arretes[6], arretes[2], arretes[7], arretes[3]
    return(arretes, centres )


def equator_prime(arretes , centres):
    for i in range(0,3):
        arretes,centres = equator(arretes,centres)
    return arretes, centres

J_sym = ["'R","U","'L","2U","R","'U","'R","2U","R","L","'U"]
J_sym_mod = ['R','U',"'L","2U","R","'U","'R","2U","L","R","'U","2R"]
PLL_J = ["R","U", "'R","'F", "R", "U", "'R", "'U", "'R", "F", "2R", "'U", "'R", "'U"]
PLL_Y = ['F', 'R',"'U","'R","'U",'R','U',"'R","'F",'R','U',"'R","'U","'R",'F','R',"'F"]
PLL_T = ['R', 'U', "'R", "'U", "'R", "F", "2R", "'U", "'R", "'U", "R", "U", "'R", "'F"]