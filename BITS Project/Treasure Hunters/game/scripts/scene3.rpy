﻿# You can place the script of your game in this file.

label scene3:

    scene scene3
    with fade

    play sound "FX/scene3FX.mp3" fadeout 0.5 fadein 5.0 

    show harry
    show benji at right
    show penny at left
    show jax at Position(xpos =100)

    #show # harry surprised
    #show # penny surprised at Position right
    #show # benji surprised at Position left
    #show jax at Position (xpos = 100)
    

    # Dialogue for scene 3

    # code for playing music

    benji excited "Ahh, what happened?"

    slim proud "It is the prophecy foretold!"

    #show slim happy at Position ? fade in

    harry confused "What!?"

    penny surprised "Who... Who are you?"

    jax mad "Grr Grr..."

    slim proud "My name is Slim and who I am is not important... but who YOU are is!"

    harry confused "Us?"

    slim "No ... YOU Harry, you!"

    jump scene3a

    return
