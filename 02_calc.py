# Exercises 2-2 #
################

# The volume of a sphere with radius r is 4/3(pi)r**3.
# What is the volume of a sphere with radius 5?

pi = 3.14159
#r = 5

def sphere(r):
    vol = (4/3)*pi*r**3
    print(round(vol, 2))

sphere(5)


# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
# the total wholesale cost for 60 copies?
price = 24.95
discount = 0.4
ship_1 = 3
ship_n = 0.75

#n = 60

def wholesale(n):
    price_disc = (price * n) * (1 - discount)
    #print(price_disc)
    ship = ship_1 + (ship_n * (n-1))
    price_tot = price_disc + ship
    print('$' + str(round(price_tot, 2)))
    
wholesale(60)

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3
# miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I get
# home for breakfast?

import math

#start_hr = 6
#start_min = 52
easy_min = 8+(15/60)
fast_min = 7+(12/60)

def run_time(start_hr, start_min):
    st_time_min = (start_hr*60) + start_min
    fin_time_min = st_time_min + (2 * easy_min) + (3 * fast_min)
    f_hr = fin_time_min / 60
    f_floor = math.floor(f_hr)
    rem = f_hr - f_floor
    f_min = math.floor(rem * 60)
    if f_min >= 10:
        print(str(f_floor) + ':' + str(round(f_min, 0)))
    else:
        print(str(f_floor) + ':' + '0' + str(round(f_min, 0)))


run_time(6, 52)
