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
    field.minesCoord(mines.spread_mines)
    player.name = game.playerName

    while not mines.it_exploded and not mines.all_flagged:
        game.progress(field.map,field.flags_location,field.flagged_mines)
        move = player.action
        field.processAction(move, mines)

    game.progress(field.map,field.flags_location,field.flagged_mines)

if __name__ == '__main__':
    play()
