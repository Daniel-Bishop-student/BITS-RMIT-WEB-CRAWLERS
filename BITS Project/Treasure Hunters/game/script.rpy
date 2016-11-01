## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define harry = Character('harry')
define benji = Character('benji')
define penny = Character('penny')
define jax = Character('jax')
define grandma = Character('grandma')

image harry happy ="scene1/harry happy.png"
image benji neutral ="scene1/benji-single.png"
image penny neutral ="scene1/penny-single.png"
image jax = "scene1/jax.png"
## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene scene1/scene1

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    show harry happy
    show benji neutral at right
    show penny neutral at left
    show jax at Position(xpos =100) 
    ## These display lines of dialogue.

    "Happy Birthday dear Harry, happy birthday to you"

    grandma "Open your present Harry"

    harry "It's a new phone!, thanks Grandma"

    ## This ends the game.

    return
