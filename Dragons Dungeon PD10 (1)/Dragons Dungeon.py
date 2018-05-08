
#The Gamers!
#Dragons Dungeon
#Kyle Afzali, Kenny Burgos, and Justin M.
#You have to get through the maze, to the queen and pass the dragons minions.
#Then you must go back through the maze and bring the Queen back to the palace.

from gamelib import*#import game library
#Creat variable
game = Game(800, 800,"Dragons Dungeon")
bk = Image("images\\background.jpg",game)
bk.resizeTo(800, 800)
king = Animation("images\\upk.png",4,game,128/4,41)
maze = Image("Images\\maze.jpg",game)
health = Image("Images\\heart.png",game)
health2 = Image("Images\\h2.png",game)
health3 = Image("Images\\h3.png",game)
#dragon = Animation("images\\dragon.png",32,game,572/4,1089/8)
goblin= Animation("images\\goblin.png",12,game,160/4,115/3)
#slime= Animation("images\\slime.png",12,game,217/9,53/2)
#move/resize
health.resizeTo(50,50)
health2.resizeTo(50,50)
health3.resizeTo(50,50)
maze.resizeTo(600,600)
king.resizeTo(30,30)
goblin.moveTo(500,235)
king.moveTo(440,250)
health.moveTo(30,50)
health2.moveTo(75,50)
health3.moveTo(120,50)
#dragon.resizeTo(100,100)
#slime.moveTo(400,235)

#Level One game loop

while not game.over:
   game.processInput()
   bk.draw()
   maze.draw()

   
   health3.draw()
   health2.draw()
   health.draw()
   king.draw()
   #dragon.draw()
   goblin.draw()
   #slime.draw()
  
   #if goblin.collidedWith(King) :

   #health.visible = False
     




      
   if keys.Pressed[K_UP]:

                   king.y -=4
   if keys.Pressed[K_DOWN]:
                    king.y +=4
                   
   if keys.Pressed[K_RIGHT]:
                   king.x +=4

   if keys.Pressed[K_LEFT]:
                   king.x -=4





   
   
   


   game.update(30)






                   

#LIST
dragonattack = []
