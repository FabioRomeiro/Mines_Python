from classes.field import Field
from classes.mine import Mine
from classes.merlin import Merlin
from classes.system import Game

def play():
    game = Game()
    mines = Mine()
    field = Field()
    player = Merlin()

    game.introduction
    field.load_field
    field.minesCoord(mines.spread_mines(field))
    player.name = game.playerName

    while not mines.it_exploded and not mines.all_flagged:
        game.progress(field)
        move = player.action
        field.processAction(move, mines, game)

    game.progress(field)
    if mines.it_exploded: game.gameOver(field)
    elif mines.all_flagged: game.won

    again = game.play_again
    if again == 'Y': play()

if __name__ == '__main__':
    play()
