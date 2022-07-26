# 1. Determine the total distance travelled and the
# total time it takes to get there by summing up
# the total distance and the total time in the list below

trips = [
    { "distance": 34, "time": 10 },
    { "distance": 90, "time": 50 },
    { "distance": 59, "time": 25 },
    { "distance": 83, "time": 60 },
    { "distance": 27, "time": 15 },
    { "distance": 68, "time": 90 }
]

# 2. Implement a 'pluck' function. 
# Pluck should accept a list and a string representing a 
# property name and return a list containing that property from each object.

# example
paints = [{"color": 'red', "text-align": "right"}, {"color": 'blue', "margin": "0px"}, {"color": 'yellow', "padding": "5px"}]
# pluck(paints, 'color')
# returns =>>>>> ['red', 'blue', 'yellow']



def pluck(list, val):

    nList = []
    for x in range(len(list)):
        nList.append(list[x][val])
    print(nList)

pluck(paints, 'color')





sumD = 0
sumT = 0
for i in trips:
    sumD += i['distance']
    sumT += i['time']

print(sumD)
print(sumT)