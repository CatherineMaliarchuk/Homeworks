from abc import ABC, abstractmethod

class Animals:
    def __init__(self, hunt, eat, walk, jump):
        self.hunt = hunt
        self.eat = eat
        self.walk = walk
        self.jump = jump
class Cow(Animals):
    def chew(self):
        return self.eat

a = Cow(1, 2, 3, 4)
print(type(a))
class Wolf(Animals):
    def gnaw(self):
        return self.eat + self.hunt
class Bird(Animals):
    def fly(self, fly):
        self.fly = fly
class Tiger(Animals):
    def fress(self):
        return self.eat + self.jump
class Mice(Animals):
    def bite(self):
        return self.eat + self.walk

class Human():
    def __init__(self, think, speak):
        self.think = think
        self.speak = speak
        print("Hi!")
class Centaurus(Animals, Human):
    def centaurus(self):
         print("Centaurus exist.")



class Person():
    def __init__(self, upper_limbs, lower_limbs):
     self.upper_limbs = upper_limbs
     move = print("move")
     self_lower_limbs = lower_limbs
class Arm(Person):
    def __init__(self, upper_limbs):
        self.upper_limbs = upper_limbs
        move = print("move fast")
        self.obj_person = Person(self, upper_limbs, lower_limbs)

    def play_the_violin(self):
        return obj_person + "play music"
class CellPhone():
    def __init__(self, light, sound):
        self.light = light
        self.sound = sound

class Screen():
    def __int__(self, light):
        self.light = light

        def brightness():
            return light + 100


    class Profile:
        def __init__(self, name, last_name, phone_number,
                     address, email, birthday, age, sex):
            self.name = name
            self.last_name = last_name
            self.phone_number = phone_number
            self.address = address
            self.email = email
            self.birhday = birthday
            self.age = age
            self.sex = sex
            self.lst = [name, last_name, phone_number,
                        address, email, birthday, age, sex]
        def str_repr(self):
            print(("Den","Sloan","+38 098 66543","Kiev","Den.Sloan@bgmail.com",
             "01.01.2000","21","male"))

class Laptop():
    def __init__(self, Screen, Keyboard, Touchpad, Webcam, Ports, Dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics

        def screen(self):
            return screen + 5

        def keyboard(self):
            return keyboard + 3

        def touchpad(self):
            return touchpad + 10

        def webcam(self):
            return webcam + 6

        def ports(self):
            return ports + 1

        def dynamics(self):
            return dynamics + 0

