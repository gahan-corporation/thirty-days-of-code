#!/usr/bin/env python3

import select
import sys

def get_total_cost_of_meal():
    try: 
        meal_cost = select.select([sys.stdin], [], [], 1)
        meal_cost = float(meal_cost[0][0].readline())

        tip_percent = select.select([sys.stdin], [], [], 1)
        tip_percent = int(tip_percent[0][0].readline())

        tax_percent = select.select([sys.stdin], [], [], 1)
        tax_percent = int(tax_percent[0][0].readline())
    except:
        meal_cost = 269.82
        tip_percent = 100
        tax_percent = 9

    # Write your calculation code here
    tip = float(meal_cost * tip_percent/100) # calculate tip
    tax = float(meal_cost * tax_percent/100) # caclulate tax

    # cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = int(round(meal_cost + tip + tax))
    
    return str(total_cost)

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
