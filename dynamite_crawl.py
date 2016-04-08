from character import *
import time

troll_name = [
                'big hands'[::-1],
                'logicalgambit'[::-1],
                'aquanine'[::-1],
                'dash16'[::-1],
                'budiak'[::-1],
                'jeff'[::-1],
            ]

troll_attacks = [
                    'punch',
                    'bite',
                    'headbutt'
                ]

WAIT_TIME = 10

hero_name = raw_input('What is your name? ')

hero = Character(name=hero_name)
troll = Troll(name=random.choice(troll_name))

print('You see Troll named ' + troll.name)
attack_type = raw_input("How do you attack (e.g. punch, kick, etc.)? ")

if hero.initiative() > troll.initiative():
    print('{} WON the intiative. Hell Yeah.'.format(hero.name))
    time.sleep(WAIT_TIME)

    damage = hero.attack(troll, attack_type)

    print('You hit the troll for {} damage'.format(damage))
    time.sleep(WAIT_TIME)

    if troll.is_dead():
        print('That was enough to kill the filthy {}'.format(troll.name))
        print('{} Wins!'.format(hero.name))
    else:
        print('{} is WEAK. {} is too strong.'.format(hero.name, troll.name))
        print('{} is dead. You Lose!'.format(hero.name))
else:
    print('{} LOST the intiative. Oh No!'.format(hero.name))
    time.sleep(WAIT_TIME)

    troll.attack(hero, random.choice(troll_attacks))
    if hero.is_dead():
        time.sleep(WAIT_TIME)
        print("{} rips {}'s arms off and beats him to death."
              .format(troll.name, hero.name))
        print('{} is dead. You Lose!'.format(hero.name))
    else:
        time.sleep(WAIT_TIME)
        print('{} only angers {} with his pitiful attack.'
              .format(troll.name, hero.name))
        print('{} goes Berserk. You Win!'.format(hero.name))
