from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str

def make_bot(path: str):
    env = Env()
    env.read_env(path)
    return TgBot(token=env('TOKEN'))


