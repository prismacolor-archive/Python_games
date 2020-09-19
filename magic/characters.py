import random


class Wizard:
    def __init__(self, name, experience, strength, staff, element):
        self.name = name
        self.experience = experience
        self.strength = strength
        self.staff = staff
        self.element = element

    def list_spells(self, spells):
        print(spells)

    def list_attack(self, attacks):
        print(attacks)

    def cast_spell(self, invocation, spells, experience, strength):
        choose_spell = input("Give the name of the spell you wish to cast. ")
        if choose_spell in spells.keys():
            print(self.invocation)
            self.experience += 1.5
            self.strength += 1
            damage_caused = (strength * experience) * 0.3
            return damage_caused
        else:
            print("The mage says, 'I know not that spell. I must try something else.'")

    def attack(self, catchphrase, attacks):
        pass


class EarthWitch(Wizard):
    def __init__(self, name, experience, strength, staff, element):
        super().__init__(name, experience, strength, staff, element)

    spells = {
        'Speak': 'Allows you to speak to trees and plants',
        'Grow': 'Allows you to grow vines into things like ladders and bridges',
        'Garden': 'Allows you to grow healing plants'
    }

    attacks = {'Quake': 'Causes the Earth to shake and open, swallowing enemies',
               'Throw': 'Hurls rocks and debris at enemies',
               'Snare': 'Shoots vines which wrap up your enemies for a time',
               'Spores': 'Causes poisonous spores to put your enemies to sleep '}

    invocation = 'Gaia, aid me.'
    catchphrase = "In the name of Gaia, I unleash the power of the Earth!"


sequoia_Redwood = EarthWitch('Sequoia', 1, 15, 'redwood', 'earth')
hazel = EarthWitch('Hazel', 15, 10, 'rowan', 'earth')
ubuntu = EarthWitch('Ubuntu', 3, 12, 'baobab', 'earth')

ubuntu_attack = ubuntu.cast_spell()
