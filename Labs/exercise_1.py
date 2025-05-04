def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  else:
    return False

def sum_double(a, b):
  if a == b:
    return 2*(a+b)
  else:
    return a+b

def sleep_in(weekday, vacation):
  if weekday == True and vacation == True:
    return True
  elif weekday == True:
    return False
  return True

def set_square(x):
    global ret_square
    
    ret_square = x**2

if __name__ == '__main__':
    ret_sqaure = 0
    
    set_square(2)
    print (ret_square)
    
    
    