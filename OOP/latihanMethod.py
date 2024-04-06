class Hero:

    def __init__(self,name,health,attack,armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_lawan):
        print(self.name + ' diserang ' + lawan.name)
        demek_diterima = attack_lawan/self.armor
        print('demek diterima : ' + str(demek_diterima))
        self.health -= demek_diterima
        print('hp ' + self.name + ' tersisa : ' + str(self.health)) 

warior = Hero('warior',100,10,5)
mamat = Hero('mamat',100,5,10)

warior.serang(mamat)
print('\n')
mamat.serang(warior)