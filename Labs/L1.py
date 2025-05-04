def quad_r1(a,b,c):
    temp = b**2 -4*a*c
    if temp < 0:
        return ("no root")
    return str((-b + (temp**.5))/(2*a)) + ", " + str((-b - (temp**.5))/(2*a))
    
if __name__ == '__main__':
    print(quad_r1(1,3,2))

a = "awd"
print(f"{a}")