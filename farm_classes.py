from pprint import pprint
class Animals:
    STATUS_SLEEP = 'спит'
    STATUS_EAT = 'ест'
    STATUS_WALK = 'пасётся'
    STATUS_MAKE_SOUNDS = 'издает звук'
    sound = ''

    animals_type = None
    animals_status = STATUS_SLEEP
    def wake_up_animal(self):               #разбудить
        pass
    def put_to_sleep(self):                 #уложить спать
        pass
    def distinguish_by_voice(self):         #различать по голосам
        pass
    def feed(self):                         # кормить
        pass
    def get_animals_type(self):             #получить тип животного
        return self.animals_type
    def get_animals_status(self):           #получить статус животного
        return self.animals_status

    def __init__(self, weight):
        self.weight = weight
         

class Wild_animals(Animals):
    animals_type = 'дикие животные'
    

  

class Pets(Animals):
    animals_type = 'домашние животные'
    
    def distinguish_by_voice():
        pets_sounds = {'га-га-га' : 'гуси', 'ко-ко-ко' : 'куры',
        'кря-кря-кря' : 'утки', 'муу' : 'коровы',
         'мее' : 'козы', 'бее' : 'овцы' }

        sound = input('Введите, какой звук издает животное:\n')
        if sound in pets_sounds.keys():
            print(f'Такой звук издают {pets_sounds.get(sound)}')
        return

    def __init__(self, weight, name):
        self.name = name
        super().__init__(weight)
        
    

class Feathered(Pets):                      #пернатые
    def feed(self):
        print(f'Налить для {self.name} воды, дать зерна')
        self.animals_status = self.STATUS_EAT
        print(f'В данный момент {self.name} {self.animals_status}')
        return self.animals_status

    def pick_eggs(self):
        print(f'Проверить гнездо {self.name}, забрать яйца')
        eggs = int(input(f'Cколько собрано яиц у {self.name}?\n'))
        return eggs
        
    
class Geese(Feathered):                     
    animals_type = 'гуси'
    sound = 'га-га-га'

class Hens(Feathered):                      
    animals_type = 'куры'
    sound = 'ко-ко-ко'

class Ducks(Feathered):                     
    animals_type = 'утки'
    sound = 'кря-кря-кря'



class Artiodactyls(Pets):                   #парнокопытные
    def feed(self):
        print(f'Налить для {self.name} воды, дать сена')
        self.animals_status = self.STATUS_EAT
        print(f'В данный момент {self.name} {self.animals_status}')
        return self.animals_status

class Cows(Artiodactyls):                 
    animals_type = 'коровы'
    sound = 'муу'
    
    def get_milk(self):
        print(f'Подоить {self.name}')
        milk_liters = input('Сколько литров молока получилось?:\n')
        return milk_liters 

class Goats(Artiodactyls):                 
    animals_type = 'козы'
    sound = 'мее'

    def get_milk(self):
        print(f'Подоить {self.name}')
        milk_liters = input('Сколько литров молока получилось?:\n')
        return milk_liters 


class Sheeps(Artiodactyls):                 
    animals_type = 'овцы'
    sound = 'бее'

    def get_wool(self):
        print(f'Постричь {self.name}')
        wool_mass = input('Сколько грамм шерсти получилось?:\n')
        return wool_mass


goose1 = Geese(7, 'Серый')
goose2 = Geese(6, 'Белый')
hen1 = Hens(3, 'Ко-ко')
hen2 = Hens(4, 'Кукареку')
duck = Ducks(5, 'Кряква')
cow = Cows(200, 'Манька')
goat1 = Goats(30, 'Рога')
goat2 = Goats(33, 'Копыта')
sheep1 = Sheeps(25, 'Барашек')
sheep2 = Sheeps(28, 'Кудрявый')

animals_list = [goose1, goose2, hen1, hen2, duck, cow, goat1, goat2, sheep2, sheep1]

total_weight = 0
weight_count = 0
for animal in animals_list:
    total_weight += animal.weight
    if animal.weight > weight_count:
        weight_count = animal.weight
        heaviest_animal = animal.name
        a_type = animal.animals_type

    
print('Общий вес всех животных:', total_weight)
print(f'Самое тяжелое животное относится к классу {a_type },'
      f'его вес - {weight_count},'
      f'его имя - {heaviest_animal}')




##goose.feed()
##print(goose.pick_eggs())
##pprint(Animals.__dict__)


