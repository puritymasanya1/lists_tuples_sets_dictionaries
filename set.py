# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))


it_companies.update({'Twitter', 'Netflix', 'Tesla'})

it_companies.pop()

print(it_companies)


#intersection
set_1 = {"Car", "Boat", "Plane", "Train"}
set_2 = {"Train", "Boat"}

print(set_1.intersection(set_2)) #returns a set of common elements.