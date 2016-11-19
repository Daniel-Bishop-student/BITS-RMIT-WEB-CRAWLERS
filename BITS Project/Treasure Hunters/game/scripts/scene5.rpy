label scene5:
    
    scene scene5
    with fade

    $ renpy.music.set_volume(0.6, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 1.0 

    show benji surprised at Position(xpos=0.25, ypos=0.95)
    show penny surprised at Position(xpos=0.70, ypos=0.95)
    show jax at right
    show slim excited at Position(xpos=0.37, ypos=0.95)
 

    # Dialogue for scene5

    slim "Ah here look!, Kia stone.  The stone will look after the chosen one. Sometimes a traumatic event or emotion can trigger the Kia stone to protect the chosen one. Where did you get this 'phone'?"

    harry surprised "My grandmother gave it to me. She must have known."

    jax "Woof!"

    stop music fadeout 1.0

    jump scene6
    

    return 
