# You can place the script of your game in this file.

label scene3:

    scene scene3
    with fade

    play music "FX/scene3FX.mp3" fadeout 0.5 fadein 5.0 

    show harry surprised
    show benji surprised at right
    show penny happy at left
    show jax at Position(xpos =100)

    #show # harry surprised
    #show # penny surprised at Position right
    #show # benji surprised at Position left
    #show jax at Position (xpos = 100)
    

    # Dialogue for scene 3

    # code for playing music

    benji "Ahh, what happened?"

    "It is the prophecy foretold!"

    show slim excited at Position(xpos=0.4, xanchor='center') # fade in

    harry "Wah!?"

    penny "Who... Who are you?"

    slim "My name is Slim and who I am is not important ... but who YOU are is!"

    harry "Us?"

    slim "No ... YOU Harry, you"

    jump scene3a

    return
