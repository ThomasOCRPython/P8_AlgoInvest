def new_array(tab):
    n = len(tab)
    for i in range(n):              
            tab[i]['profit'] = float(tab[i]['price'])*(float(tab[i]['profit'])/100)
        #     print('profit : ',tab[i]['profit'])
        #     print('price : ',tab[i]['price'])

    
    return tab