# return a string (animals must be in order of appearance) with the number of times an animal is repeated
with open("message_01.txt") as f:
    text = f.read()
    
# string to array  -> separate from spaces
animals = {}
listOfAnimals = text.split()
for animal in listOfAnimals:
    # if it´s registered increase it's valu
    if animals.get(animal) is not None:
        animals[animal] = animals[animal]+1

    # if it isn't registered create a new key 
    else:
        animals.update({animal: 1})

numerOfAnimals = ""
for animal, count in animals.items():
    numerOfAnimals +=  animal + str(count)
print(numerOfAnimals)