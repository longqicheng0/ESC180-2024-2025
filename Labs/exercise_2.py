def string_times(str, n):
  return str*n
def front_times(str, n):
  return str[0:3]*n
def array_count9(nums):
  count = 0
  for i in range (0, len(nums)):
    if nums[i] == 9:
      count += 1
  return count
def array_front9(nums):
  for i in range (0, len(nums)):
    if i < 4 and nums[i]==9:
      return True
    
  return False
def array123(nums):
  for i in range (0, len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False
def string_match(a, b):
  cnt = 0
  if len(a) < len(b):
    ref = a
    other = b
  else:
    ref = b
    other = a
  for i in range (len(ref)-1):
    if ref[i:i+2] == other[i:i+2]:
      cnt += 1
  return cnt
def first_half(str):
  return str[0:len(str)//2]
def without_end(str):
  return str[1:len(str)-1]
def combo_string(a, b):
  if len(a) > len(b):
    return b+a+b
  return a+b+a
def left2(str):
  return str[2:len(str)] + str[0:2]
def near_ten(num):
  return num % 10 - 2 == 0 or num % 10 + 2 == 10 or num % 10 - 1 == 0 or num % 10 + 1 == 10 or num % 10 == 0
def count_code(str):
  count = 0
  for i in range (0, len(str)-3):
    if str[i:i+2] == "co" and str[i+3] == "e":
      count+=1
  return count
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if a[len(a)-3:len(a)] == b[len(b)-3:len(b)]:
    return True
  return False
def centered_average(nums):
  nums.sort()
  if len(nums) % 2 == 0:
    return (nums[len(nums)//2] + nums[len(nums)//2 - 1])//2
  else:
    return nums[(len(nums) - 1)//2]

dgCount = 0
pi = [3,1,4,1,5,9,2,6,5,3]

def next_digit_pi():
    global dgCount, pi  
    cur = pi[dgCount]
    dgCount += 1
    return (cur)

if __name__ == "__main__":
    print(next_digit_pi())
    print(next_digit_pi())