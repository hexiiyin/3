import random
import string

def randomPlate():
    plate = ""
    x = ["new", "old"]
    type = random.choice(x)
    
    if type == "new":
        plate += random.choice(string.ascii_letters)
        plate += random.choice(string.ascii_letters)
        plate += random.choice(string.ascii_letters)
        plate += random.choice(string.ascii_letters)
        
        plate += str(random.randint(0,9))
        plate += str(random.randint(0,9))
        plate += str(random.randint(0,9))

    elif type == "old":
        plate += random.choice(string.ascii_letters)
        plate += random.choice(string.ascii_letters)
        plate += random.choice(string.ascii_letters)
        
        plate += str(random.randint(0,9))
        plate += str(random.randint(0,9))
        plate += str(random.randint(0,9))

    return plate

print(randomPlate())