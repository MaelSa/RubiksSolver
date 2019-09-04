from fonctions_deplacement import *
from Scrambler import *
from graphic_interpreter import *
import matplotlib.pyplot as plt
from resolution import *
from Simplify import *
#On génere un mélange
list_scramble = generate_scramble()

scramble_readable = readable_scramble(list_scramble)
print("Le mélange est :")
print(scramble_readable)

#On l'execute:
aretes,coins,centres = execute_move(list_scramble,Arretes_res,Coins_res,Centres_res)

graphic_inter(aretes,coins,Centres_res,Arretes_graph,milieu_graph,Coins_graph, True)

#On solve les coins :
aretes,coins,centres,list_move_coins,nb_coins_parité, nbb = resolution_coins(aretes,coins,centres)


#On solve les aretes :
aretes,coins,centres,list_move_aretes,nb_aretes_parité, nbb = resolution_aretes(aretes,coins,centres)
#On affiche :
list_move = list_move_coins

list_move += list_move_aretes
readable_list_move = readable_scramble(list_move)
print("La solution est :")
print(readable_list_move)

graphic_inter(aretes,coins,Centres_res,Arretes_graph,milieu_graph,Coins_graph,False)
