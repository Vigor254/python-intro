class Dad:
    def football(self):
        print("dad likes watching football")
class Mum:
    def cooking(self):
        print(" mum likes cooking")
class Boy(Dad):
    def Boyage(self):
        print(" boy is 15 years old")
my_boy = Boy()
my_boy.Boyage()
my_boy.football()
class Girl(Mum):
    def charting(self):
        print(" girl likes charting")
my_girl = Girl()
my_girl.charting()
my_girl.cooking()

