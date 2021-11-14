import os
import sys
from data.action_table import table_action
from tool.update_table import new_array
from tool.csv_converter import read_csv
from tool.clean_table import clean_price
from optimized import glouton
from bruteforce import brute_force
from chart import algo_loop_table


def get_choice():
    # os.system('clear')
    choice = input(" Algo force brute = 1\n Algo glouton = 2\n Algo glouton data_0 = 3\n Algo glouton data_1 = 4\n Enter yout choice : ")
    
    
    if choice == "1":
        tab_action_0 = new_array(table_action)
        # print(tab_action)
        algo_loop_table(brute_force, tab_action_0,"data_0") 
    elif choice == "2":
        tab_action_1 = new_array(table_action)
        algo_loop_table(glouton, tab_action_1,"data_1")
        
    elif choice == "3":
        tab_action_3 = read_csv('data/dataset1_Python+P7.csv')
        tab_action_4 = new_array(tab_action_3)
        glouton(tab_action_4)

    elif choice == "4":
        tab_action_4 = read_csv('data/dataset2_Python+P7.csv')
        tab_action_5 = new_array(clean_price(tab_action_4))
        glouton(tab_action_5)
        
    # elif self.choice == "5": 

    else:
        print('OUAOU')
        sys.exit()

# def enter_choice():
#     choice = input()
#     return choice

