# from bruteforce import brute_force, tab_action 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def algo_loop_table(function, table,nom):
    n = len(table)
    x = []
    y = []
    cp = 0
    tab = []
    for i in range(n):
        tab.append(table[i])
        cp += 1
        x.append(cp)
        y.append(function(tab)[1]) 
    # print('Mes list x & y ',tab,'x:',x,'y :',y)
    graph_figure(x,y,nom)

def graph_figure(x,y,nom):
    name=nom
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r")
    plt.plot(x,y)
    plt.xlabel('nb actions')
    plt.ylabel('time in ms')
    plt.savefig('img/'+name+'.png',format="png")
    plt.show()  
    plt.close()
# algo_loop_table(brute_force, tab_action)









