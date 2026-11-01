from list_ import List
from super_heroes_data import superheroes

class Superheroe:
     def __init__(self, name,alias, real_name, short_bio, first_appearance, is_villain):
          self.name=name
          self.alias=alias
          self.real_name=real_name
          self.short_bio=short_bio
          self.first_appearance=first_appearance
          self.is_villain=is_villain

    def__str__(self):
        return f"{self.name}-{self.alias}-{ self.real_name}-{self.short_bio}-{self.first_appearance}-{self.is_villain}"

listaHeroes=list()

