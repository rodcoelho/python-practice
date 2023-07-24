#!/usr/bin/env python3

# Create an insurance product for cats and dogs (pets). 

class Pets():
    
    
    def __init__(self, name=None, gender=None, breed=None, age=0, zipcode=None):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.zipcode = zipcode
        self.base_price = 40
        self.zipcode_d = {
            11217: 0.01,
            90210: 0.02,
            "02481": 0.03,
        }
        self.age_d = {
            3: 0.12,
            4: 0.22,
            8: 0.34,
        }
        self.breed_d = {
            "tabby": 0.11,
            "maine coon": 0.13,
            "golden retriever": 0.11,
            "chocolate lab": 0.17,
        }


class Dogs(Pets):
    
    def __init__(self, **kwargs):
        self.species = "dog"
        self.factor = 1
        super(Dogs, self).__init__(**kwargs)


class Cats(Pets):
    
    def __init__(self, **kwargs):
        self.species = "feline"
        self.factor = 0.9
        super(Cats, self).__init__(**kwargs)
        
    def get_quote(self):
        total = 0
        total += self.zipcode_d[int(self.zipcode)]
        total += self.age_d[self.age]
        total += self.breed_d[self.breed]
        total += self.factor
        return total * 40
        

fluffy = Cats(zipcode = "02481", age = 4, breed = "tabby")
quote = fluffy.get_quote()
print(quote)
    

# fido = Dogs(
#     name = "Fido",
#     gender = "Male",
#     breed = "Dalmation")

# print(fido.age)


# calculate quote for Fluffy: zip 11217, age 4, breed: tabby, species: cat


# base price: 40

# zipcode
# 11217: 0.01
# 90210: 0.02
# 02481: 0.03

# age
# 3: 0.12
# 4: 0.22
# 8: 0.34
    
# breed
# "tabby": 0.11
# "maine coon": 0.13
# "golden retriever": 0.11
# "chocolate lab": 0.17
    
# species
# dog: 1
# cat: 0.9
