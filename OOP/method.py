class Hero:
    #class variabel
    jumlah_hero = 0

    def __init__(self,inputname,inputhealth,inputpower,inputarmor):
        #instace variabel
        self.name = inputname
        self.health = inputhealth
        self.power = inputpower
        self.armor = inputarmor
        Hero.jumlah_hero += 1

    # void function, method tanpa return
    def siapa(self):
        print("classku adalah " + self.name)

    # method dengan argumen
    def hp(self,up):
        self.health += up
    #method dengan return
    def gethp(self):
        return self.health
hero1 = Hero('warior',100,10,5)
hero2 = Hero('support',80,5,20)

hero1.siapa()
hero1.hp(12)

print(hero1.gethp())