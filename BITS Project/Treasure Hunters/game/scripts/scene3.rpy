# You can place the script of your game in this file.

label scene3:

    scene scene3
    with fade

    $ renpy.music.set_volume(0.8, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play sound "FX/transporter.mp3"

    play music "FX/scene3FXwind.mp3" fadeout 0.5 fadein 5.0 

    show harry surprised at Position(xpos=0.5, ypos=0.95)
    show benji surprised at Position(xpos=0.25, ypos=0.95)
    show penny surprised at Position(xpos=0.70, ypos=0.95)
    show jax at right


    # Dialogue for scene 3

    # code for playing music

    benji "Ahh, what happened?"

    play sound "FX/scene3_slim_enigma.mp3"

    show slim excited at Position(xpos=0.37, ypos=0.95)
    with dissolve

    slim "IT IS THE PROPHECY FORETOLD!"

    harry "Wah!?"

    stop sound

    penny "Who... Who are you?"

    jax mad "Grr Grr..."

    slim "My name is Slim and who I am is not important ... but who YOU are is!"

    show jax at right

    harry excited "Us?"

    slim "No ... YOU %(harry_name)s, you."

    stop music fadeout 1.0

    jump scene3a

    return
