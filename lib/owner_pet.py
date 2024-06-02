class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Valid pet types are: {', '.join(Pet.PET_TYPES)}")
        


class Owner:
    def __init__(self, name):
        self.name = name
    # In this pets method we use isinstance to ensure that each item in Pet.all is a valid Pet instance 
    # and that the owner of the pet matches the current owner instance (self)
    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet, Pet) and pet.owner == self]
    
    # Alternatively we can handle it this way without the isinstance
    '''def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]'''

    # We start by checking if the pet is an instance of the Pet class
    # If it is, we set the pet's owner to the current instance of Owner 
    # If it is not, raise a an Exception
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("The pet must be an instance of the Pet class")
        pet.owner = self 

# Alternatively we can handle it this way without the isinstance
    '''def add_pet(self, pet):
        if pet.owner is not self:
            pet.owner = self'''
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)