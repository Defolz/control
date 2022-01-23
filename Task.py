def acceleration():
    global a
    global t
    try:
        V = int(input())
        V0 = int(input())
        t = int(input())
        b = V - V0
        a = b/t
    except ValueError:
        print('Это не число. Выходим.')
    except ZeroDivisionError:
        print('Ноль нельзя.')
    print(a)
def Decorate(acceleration):
    def wrapper():
        acceleration()
        s = (a*t*t)/2
        print(s)
    return wrapper

big = Decorate(acceleration)
acceleration()
