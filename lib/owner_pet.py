class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
    


class Owner:
    def __init__(self, name):
        self.name = name
    
    '''def pets(self):
        return [pet for pet in self.pets if pet.owner == self.name]'''
    
    '''def add_pet(self,pet):
        if pet in self.pets:
            self.pets.append(pet)'''