from weapon import Weapon


def test_weapon_name():
    weapon = Weapon(name='sword')
    assert weapon.name == 'sword'


def test_weapon_damage_is_between_2_and_5():
    weapon = Weapon(name='sword')
    assert weapon.damage >= 2
    assert weapon.damage <= 5
