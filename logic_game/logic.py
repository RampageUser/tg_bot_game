import random

STONE: str = 'Камень'
PAPER: str = 'Бумага'
SCISSORS: str = 'Ножницы'

def spin_random_wheel() -> str:
    option: int = random.randint(1,3)
    if option == 1:
        return STONE
    elif option == 2:
        return PAPER
    else:
        return SCISSORS

def compare_option(player: str, random_option: str) -> bool | None:
    player = player.capitalize()
    random_option = random_option.capitalize()
    if player == random_option:
        return None
    elif player == STONE and random_option == SCISSORS:
        return True
    elif player == PAPER and random_option == STONE:
        return True
    elif player == SCISSORS and random_option == PAPER:
        return True
    else:
        return False