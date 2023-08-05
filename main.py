
# Создать класс Animal: name, color
# Создать класс Cat(Animal): свойства(get, set) по всем атрибутам, метод выводит мяу
# Создать класс Dog(Animal): свойства(get, set) по всем атрибутам, метод выводит гав

class Animal:
    def __init__(self, name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

    def get_print_voice(self):
        print(f'Скажи: {self.voice}')

class Cat(Animal):
    def __init__(self, name, color, voice, cat_breed):
        super().__init__(name, color, voice)
        self.cat_breed = cat_breed

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if new_name != '':
            self.name = new_name

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        if new_color != '':
            self.color = new_color

    def get_breed(self):
        return self.cat_breed

    def __str__(self):
        return 'Cat name: ' + self.name + '\nCat color: ' + self.color + '\nBreed: ' + self.cat_breed

    # Необязательно, т.к. возьмет этот метод из "родительского класса" Animal
    # def get_print_voice(self):
    #     super().get_print_voice()


class Dog(Animal):
    def __init__(self, name, color, voice, dog_breed):
        super().__init__(name, color, voice)
        self.dog_breed = dog_breed

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        if new_name != '':
            self.name = new_name

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        if new_color != '':
            self.color = new_color

    def get_breed(self):
        return self.dog_breed

    def __str__(self):
        return 'Dog name: ' + self.name + '\nDog color: ' + self.color + '\nBreed: ' + self.dog_breed


catName = input('Enter cat name: ')
catColor = input('Enter cat color: ')
catBreed = input('Enter cat breed: ')
catVoice = input('Enter cat voice: ')
print('-------------------------')
dogName = input('Enter dog name: ')
dogColor = input('Enter dog color: ')
dogBreed = input('Enter dog breed: ')
dogVoice = input('Enter dog voice: ')

cat = Cat(catName, catColor, catVoice, catBreed)
dog = Dog(dogName, dogColor, dogVoice, dogBreed)

print('-------------------------')
#  Вывод на печать через метод __str__
print(cat)
print('-----------------')
print(dog)

print('-----------------')

# Вывод на печать через метод get_...
# print('Cat name: ', cat.get_name())
# print('Cat color: ', cat.get_color())
# print('Cat breed: ', cat.get_breed())

cat.set_name('tom')
cat.set_color('black and white')
print(cat.get_name())
print(cat.get_color())

print('-----------------')
dog.set_name('bim')
dog.set_color('brown')
print(dog.get_name())
print(dog.get_color())

print('-----------------')
cat.get_print_voice()
dog.get_print_voice()
