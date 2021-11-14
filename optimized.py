
from tool.decorator import timer
from data.action_table import table_action
from tool.update_table import new_array
import time

# tab_action = new_array(table_action)
# print(tab_action)

price_max = 500

def price(action):
    return action['price']

def profit(action):
    return action['profit']

@timer
def glouton(tab_action, price_max=500):
    start = time.time()
    table_triee = sorted(tab_action, key =  profit, reverse = True)
    # print('tableau trie                         \n',table_triee)
    price_total = 0
    solution_gloutonne = []
    i = 0
    while i < len(table_triee) and price_total < price_max :
        action = table_triee[i]
        price_action = float(price(action))
        if price_total + price_action <= price_max:
            solution_gloutonne.append(action)
            price_total += price_action
        i += 1
    print('prix total : ',price_total)
    print("profit total",profit_total(solution_gloutonne))
    end = time.time()
    elapsed1 = end - start
    return solution_gloutonne, elapsed1

def profit_total (table_action):
    profit_t = 0
    for action in table_action:
        profit_t+=float(action['profit'])
    return profit_t

# solut_gloutonne = glouton(tab_action, price_max)
# print('profit total : ',profit_total(solut_gloutonne))
# print(glouton(tab_action, price_max))