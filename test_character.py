from character import *


def test_character_hitpoints():
    character = Character()
    assert character.hit_points >= 5
    assert character.hit_points <= 8


def test_character_default_weapon_is_a_sword():
    character = Character()
    weapon = Weapon(name='sword')
    assert character.weapon.name == 'sword'


def test_character_name_creation():
    character = Character(name='tony')
    assert character.name == 'tony'


def test_character_initiative():
    character = Character(name='tony')
    assert character.initiative() >= 1
    assert character.initiative() <= 10


def test_character_takes_damage():
    character = Character()
    assert type(character.takes_damage(1)).__name__ == 'int'


def test_character_attack():
    character = Character(name='tony')
    troll = Troll()
    attack_value = character.attack(troll, 'punch')
    assert attack_value >= 2
    assert attack_value <= 10


def test_Troll_default_weapon_is_a_club():
    character = Troll()
    assert character.weapon.name == 'club'
