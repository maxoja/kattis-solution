#https://open.kattis.com/problems/delivery

def compare_key( element ) :
    return element['distance']

def get_cost( destinations ) :
    cost = 0
    
    while len(destinations) > 0 :
        farest = destinations[0]
        del destinations[0]
        distance = farest['distance']
        letter = farest['letter']
        round = letter//truck_size + ( 1 if letter%truck_size > 0 else 0 )
        cost += round*2*distance
        left_over = round*truck_size - letter
        
        while left_over > 0 and len(destinations) > 0 :
            amount = min([left_over, destinations[0]['letter']])
            destinations[0]['letter'] -= amount
            left_over -= amount
            
            if destinations[0]['letter'] == 0 :
                del destinations[0]

    return cost
    
n_destinations, truck_size = tuple(map(int, input().split()))

right_destinations = []
left_destinations = []

for _ in range(n_destinations) :
    dist, letter = tuple(map(int, input().split()))
    new_destination = {'letter':letter}
    
    if dist > 0 :
        new_destination['distance'] = dist
        right_destinations.append(new_destination)
    else :
        new_destination['distance'] = -dist
        left_destinations.append(new_destination)

right_destinations.sort(key=compare_key, reverse=True)
left_destinations.sort(key=compare_key, reverse=True)

cost = 0
cost += get_cost(right_destinations)
cost += get_cost(left_destinations)

print(cost)
    
