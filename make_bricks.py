#Description:
#We want to make a row of bricks that is goal inches long. We have a
#number of small bricks (1 inch each) and big bricks (5 inches each).
#Print True if it is possible to make the goal by choosing from the
#given bricks. 

from random import randint

small = randint(1,10) #small bricks amount
big = randint(1,10)   #big bricks amount
goal = randint (10,50)#goal

small_length = 1 #length of the small brick
big_length = 5   #length of the big brick
total_length = small * small_length + big * big_length #total length

#next 4 lines are optimization, they only affect the speed of the
#code and deleting them will still yield the same correct answers

#checking if the total length would be enough to achive the goal
if goal > total_length:
    print(False)
#checking if the total length is equal to the goal
elif goal == total_length:
    print(True)

#how many big bricks are needed to achieve the goal
num_big = goal // 5

#subtracting the length of big bricks
goal -= min(big, num_big) * big_length

#checking if small bricks would be sufficient in achieving the goal      
if goal <= small: 
    print(True)
else:
    print(False)