# Tuples are immutable, ordered collections of elements. They are similar to lists, but they cannot be changed.
# Tuples are defined using parentheses ().

girls = ("Katty", "Betty", "Bella")
boys = ("Joe", "Ben", "Nick")

siblings = girls + boys

family_members = list(siblings)
family_members.append("mother")
family_members.append("father")
family_members = tuple(family_members) 

*siblings, mother, father = family_members #unpacking

print(siblings)
print(mother)
print(father)



nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Iceland" in nordic_countries)  #Check if an element is in a tuple