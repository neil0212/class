class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=' ')
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Dom","Tsi","Da"])
    
    def self_combust(self):
        print("Drummer is on fire")
        
    def count(self):
        print('One, Two, Three, Four')
        print("Let's go")
        

class Band(): 
  def __init__(self, name, members):
    self.name = name
    self.members = members
    
  def hire(self,musicican):
    self.members.append(musicican)
  
  def fire(self,musicican):
    self.members.remove(musicican)
        
    
     
nigel=Guitarist()
ringo=Bassist()
aba  = Drummer()
park = Drummer()


print(aba.sounds)
rock=Band('rock',[nigel,ringo])
rock.hire(aba)
rock.fire(aba)
rock.hire(park)
#print(rock.members)

park.count()
for musician in rock.members:
    if type(musician).__name__!='Drummer':
        musician.solo(7)
