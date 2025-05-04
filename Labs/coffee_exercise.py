def drink_coffee():
    global last_coffee_time, current_time, last_coffee_time2, too_much_coffee
    
    too_much_coffee = current_time - last_coffee_time2 < 120
    
    if (current_time - last_coffee_time2)  < 120:
        too_much_coffee == True
    else:
        last_coffee_time2 = last_coffee_time
        last_coffee_time = current_time
  
def study(minutes):
    global last_coffee_time, current_time, knols, too_much_coffee
    
    coffeeed = last_coffee_time == current_time 
    
    if too_much_coffee == True:
        knols += 0
    elif too_much_coffee == False:
        if coffeeed :
            knols += 10 * minutes
        elif not coffeeed: 
            knols += 5 * minutes
    
    current_time += minutes


def initialize():
      global too_much_coffee
      global current_time
      global last_coffee_time
      global last_coffee_time2
      global knols
      global coffee_count
      
      too_much_coffee = False
      current_time = 0
      knols = 0
      coffee_count = 0
      
      last_coffee_time = -100
      last_coffee_time2 = -100
      
if __name__ == '__main__':
    initialize()
    study(60)      # knols = 300
    study(20)      # knols = 400
    drink_coffee() # knols = 400 l2 = 0 l = 80 cur = 80
    study(10)      # knols = 500
    drink_coffee() # knols = 500 l2 = 80 l = 90
    study(10)      # knols = 600
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes l2 = 90 l = 100, cur = 100
    print(knols)
    study(10)      # knols = 600
    
    print(knols)