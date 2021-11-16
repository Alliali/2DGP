# class Star:
#
#     type = 'Star'   #클래스 변수
#     x = 100
#
#     def change():
#         x = 200         #로컬 변수
#         print('x is ', x)
#
# print('x IS ', Star.x)
# Star.change()
# print('x IS ', Star.x)
#
# Star = Star()
# print('x IS ', Star.x)
# Star.change()

class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

Player = Player()
Player.where()

print(Player.type)

Player.where()
Player.where(Player)