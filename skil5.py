#Skil5
import math

class trapisa:
    def __init__(self,a=2,b=5,c=7,d=8):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def fall(self):
        return self.a + +self.b + self.c + self.d

    def fall2(self):
        s=(self.a + self.b+ self.c+ self.d)/2
        d=math.sqrt((s- self.c)*(s - self.a)*(s-self.c-self.b)*(s-self.c-self.d))
        x=(self.a+self.c)/abs(self.a-self.c)
        f =x*d
        return f
    def fall3(self,h):
        f = h*self.a + self.b/2
        return f
    def fall4(self):
        if self.b == self.d:
           return True
        else:
           return False
    def fall5(self):
        return "Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða."


class bill:
    def __init__(self,tegund,argerd,hradi,bensin,eydsla):
        self.tegund = tegund
        self.argerd = argerd
        self.hradi = hradi
        self.bensin = bensin
        self.eydsla = eydsla

    def upplysingar(self):
        print (bill1)
        print (bill2)
        print(bill3)

class Players:
    playCount = 0

    def __init__(self, name, goals):
        self.name = name
        self.goals = goals
        Players.playCount += 1

    def displayCount(self):
        print("Total Players %d" % Players.playCount)

    def displayPlayers(self):
        print("Name : ", self.name, ", goals: ", self.goals)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x * 2) + (self.y * 2)) ** 0.5

    def print_point(self):
        print('({0}, {1})'.format(self.x, self.y))

svar = "Ja"
while svar == "Ja":
    print("1. Trapisa")
    print("2. Froskar")
    print("3. Bíll")
    print("4. Fótboltaspilari")
    print("5. Hætta")
    val = int(input("veldu þér lið: "))

    if val == 1:
        u = trapisa(2,5,7,8)
        h = int(input("Veldu hæð: "))
        print(u.fall())
        print(u.fall2())
        print(u.fall3(h))
        if u.fall4():
            print("jafn-arma trapisa")
        else:
            print("ekki jafn-arma trapisa")
            pass
        print(u.fall5())
        print("")
    if val == 2:
        print("XD gat ekki :/")


    if val==3:
        print("---------------------------------------------------------------------------")
        bill1 = bill("nissan gtr", "2017", 120, 5.2, 0.5)
        bill2 = bill("lamborghini huracan", "2017", 150, 10, 0.7)
        bill3 = bill("ferrari 488", "2017", 140, 10, 0.9)
        timi_1=(1000/bill1.hradi)
        timi_2 = (1000/bill2.hradi)
        timi_3 = 1000/bill3.hradi
        print(timi_1)
        print(timi_2)
        print(timi_3)
        eydsla_1 = 10*bill1.eydsla
        eydsla_2 = 10*bill2.eydsla
        eydsla_3 = 10*bill3.eydsla
        if timi_1 < timi_2:
            print("bill 1 vann á timanum",timi_1,"og eyðslan var",eydsla_1,"L")
        if timi_1 < timi_3:
            print("bill 1 vann á timanum",timi_1,"og eyðslan var",eydsla_1,"L")

        if timi_2 < timi_1:
            print("bill 2 vann á timanum", timi_2, "og eyðslan var", eydsla_2,"L")
        if timi_2 < timi_3:
            print("bill 2 vann á timanum", timi_2, "og eyðslan var", eydsla_2,"L")

        if timi_3 > timi_1:
            print("bill 3 vann á timanum", timi_3, "og eyðslan var", eydsla_3,"L")
        if timi_3 < timi_2:
            print("bill 3 vann á timanum", timi_3, "og eyðslan var", eydsla_3,"L")
        print("---------------------------------------------------------------------------")

    if val == 4:
        print("--------------------------------------------")
        play1 = Players("Jens", 10000)
        play2 = Players("Skúli", 50000)
        play1.displayPlayers()
        play2.displayPlayers()
        print("Total Players %d" % Players.playCount)


        p = Point(1, 5)
        p.print_point()
        print("--------------------------------------------")
        
    if val == 5:
        print("Bæææ")
        break
        
