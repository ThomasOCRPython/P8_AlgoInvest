def clean_price(tab):
    n=len(tab)
    tab1=[]
    for i in range(n):
            if float(tab[i]['price']) > 0:
                    tab1.append(tab[i])   
    return tab1