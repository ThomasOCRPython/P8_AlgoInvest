from tool.decorator import timer
# from data.action_table import table_action
# from tool.update_table import new_array


# tab_action = new_array(table_action)

@timer
def brute_force(tab_action) :
    n = len(tab_action)
    # print ('array : ',tab_action)
    # print('numbers of line',(n))
    tab_entier = [i for i in range(2**n)]
    # print(tab_entier)
    tab_binair = [bin(i)[2:] for i in tab_entier ]
    # print (tab_binair)
    combinaisons = ['0'*(n-len(k)) + k for k in tab_binair]
    # print('nb of combinaison :',len(combinaisons))
    # print(combinaisons)
    price_max = 500
    combinaisons_valides = []

    for combi in combinaisons :
        price = 0
        profit = 0
        for i in range(n):
            if  combi[i] == '1': 
                price += float(tab_action[i]['price'])
                profit += tab_action[i]['profit']           
        if price <= price_max:
            combinaisons_valides.append((combi, profit))
    # print('combinaisons valides : ',combinaisons_valides,'rrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    # print('numbers of combinaisons : ',len(combinaisons_valides))
    solution_optimale = combinaisons_valides[0][0]  
    profit_max = combinaisons_valides[0][1]

    for combi in combinaisons_valides:
        if combi[1]>profit_max:
            profit_max = combi[1]
            # print('profit max ',profit_max)
            solution_optimale = combi[0]
    # print('profit maximum : ',profit_max)
    # print('solution optimal : ',solution_optimale)
    list_optimal = []
    somme = 0
    total = 0
    for i in range(len(solution_optimale)):
        if solution_optimale[i] == '1':
            total += tab_action[i]['profit']
            # print('total',total)
            somme += tab_action[i]['price']
            list_optimal.append(('name:',tab_action[i]['name'],'price:',tab_action[i]['price'],'profit:',tab_action[i]['profit']))
            # list_optimal.append((tab_action[i]['name'],tab_action[i]['profit']))
    # print('la liste',list_optimal)
    print('total :',total)
    print('somme',somme)
    # print('list forcebrute :',list_optimal)
    
# brute_force(tab_action)

    
