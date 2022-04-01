#this is simplae game charactor using of objects

class game():
    damage = 10     

    def name(self):
        self.hero = input("enter hero name: ")
        self.enemy =  input("enter your aponant name: ")
    
    def helth(self):
        self.hero_helth = 100
        self.enemy_helth = 100
    
    def attack(self):
        if(h.attack(e)):
            enemy_helth -= damage
            return enemy_helth
        elif(e.attack(h)):
            hero_helth -= damage 
            return hero_helth


h = game()     # this is the object of class   creat
e = game()

h.name()

h.attack(e)

    