
#The Gamers!
#Dragons Dungeon
#Kyle Afzali, Kenny Burgos, Mingjie Li, and Justin M.
#You have to get through the maze, to the queen and pass the dragons minions.
#Then you must go back through the maze and bring the Queen back to the palace.

from gamelib import*#import game library
#Creat variable
game = Game(1000, 800,"Dragons Dungeon")
bk = Image("images\\bk.jpg",game)
bk.resizeTo(1000, 800)
gameover = Image("images\\gameover.jpg",game)
gameover.resizeTo(1000, 800)
#end sc


bk.draw()
gameover.draw()

game.update()
game.wait(K_RETURN)
game.quit()
