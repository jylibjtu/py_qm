import math
import random
from enum import Enum


class WeaponType(Enum):
    # 剑-刀
    SWORD = (1, '剑')
    KNIFE = (2, '刀')
    # 弓箭-弩
    BOW = (3, '弓')
    CROSSBOW = (4, '弩')
    # 魔杖
    WAND = (5, '杖')
    GUN = (6, '枪')

    def __init__(self, v, n):
        self.v = v
        self.n = n

    @classmethod
    def v2n(cls, v):
        for weapon in WeaponType:
            if weapon.v == v:
                return weapon.n
        return ''


class WeaponColor(Enum):
    def __init__(self, v, n):
        self.v = v
        self.n = n

    RED = (5, '传说')
    ORIANGE = (4, '稀世')
    PURPLE = (3, '罕见')
    BLUE = (2, '珍品')
    GREEN = (1, '可用')
    WHITE = (0, '破烂')


def _color(gold):
    if gold <= 0:
        return WeaponColor.WHITE
    add_rate = math.log(gold, 10) * 10 * random.randint(0, 100) * 0.01
    print(add_rate)
    rr = random.randint(0, 70)
    print(rr)
    final_r = rr + add_rate
    print(final_r)
    if final_r >= 90:
        return WeaponColor.RED
    elif final_r >= 75:
        return WeaponColor.ORIANGE
    elif final_r >= 60:
        return WeaponColor.PURPLE
    elif final_r >= 45:
        return WeaponColor.BLUE
    elif final_r >= 30:
        return WeaponColor.GREEN
    return WeaponColor.WHITE


def create_weapon(name, major, gold):
    color_str = _color(gold)
    weapon_type = WeaponType.v2n(major)
    descs = [
        ['日用', '军团', '二手'],
        ['珍宝', '收藏家'],
        ['闪耀', '辉煌'],
        ['无双', '巨力', '收割者'],
        ['天崩地裂', '般若奔雷'],
        ['洪荒', '宇宙', '界灭']
    ][color_str.v]
    desc = descs[random.randint(0, len(descs) - 1)]
    return print(f'【{name}】获得了{color_str.n}的{desc}{weapon_type}')


if __name__ == '__main__':
    create_weapon('jy', 6, 70000)