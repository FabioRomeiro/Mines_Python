from field import Field
from mine import Mine
from merlin import Merlin
from system import Game

def play():
    game = Game()
    mines = Mine()
    field = Field()
    player = Merlin()

    game.introduction
    field.load_field
    print(mines.spread_mines)
    field.minesCoord(mines.spread_mines)
    player.name = game.playerName

    while not mines.it_exploded and not mines.all_flagged:
        game.progress(field.map,[],0)


if __name__ == '__main__':
    play()
