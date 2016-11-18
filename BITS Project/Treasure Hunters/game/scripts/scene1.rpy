## The game scene here.

label scene1:

    scene scene1

    show harry
    show benji at right
    show penny at left
    show jax at Position(xpos =100) 
    
    # Dialogue for scene1

    all_characters happy "Happy Birthday dear Harry, happy birthday to you"
    jax bark "Woff Woof"
    all_characters happy "Yay!"

    grandma happy "Open your present Harry!"

    $ harry_name = renpy.input("Enter a new name for Harry!")
    $ harry_name = harry_name.strip()
    if harry_name == "":
        $ harry_name = "Harry"

    $ benji_name = renpy.input("Enter a new name for Benji!")
    $ benji_name = benji_name.strip()
    if benji_name == "":
        $ benji_name = "Benji"

    $ penny_name = renpy.input("Enter a new name for Penny!")
    $ penny_name = penny_name.strip()
    if penny_name == "":
        $ penny_name="Penny"

    harry happy "It's a new phone!, thanks Grandma!!"

    jump scene2

    return