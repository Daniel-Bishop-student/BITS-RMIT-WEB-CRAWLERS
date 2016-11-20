label scene3a:
    
    scene scene3a
    with fade

    $ renpy.music.set_volume(0.3, 0, channel='music')
    $ renpy.music.set_volume(0.3, 0, channel='sound')

    play music "FX/scene3aFXbirds.mp3" fadeout 2.0 fadein 1.0

    show harry excited at Position(xpos=0.5, ypos=0.95)
    with dissolve
    show benji excited at Position(xpos=0.25, ypos=0.95)
    with dissolve
    show penny happy at Position(xpos=0.70, ypos=0.95)
    with dissolve
    show slim happy at Position(xpos=0.37, ypos=0.95)
    with dissolve
    show jax at right
    with dissolve
 
    # fade all characters in and make transperent?

    # Dialogue for scene3a

    slim "Brenner-456 used to be warm, bright and full of life. There was plenty of food, happiness and community spirit."

    slim proud "Kids ran free in the fields without worry and people worked together to build, teach and enjoy life."

    slim excited "The people would gather on the seventh day and pay tribute to the Ora."

    benji excited "What's the Ora?"

    slim "The Ora is the Great Mountain, it is the life source and in return for our loyalty the Ora provides us with Kia, a precious earth gem which holds great power."

    harry "What kind of power?"

    slim happy "Great powers of healing and growth. It fertilises our soil and purifies our water and regulates our seasons and much more."

    slim mad "One day a cloud descended upon Brenner. This cloud bore fire and the noise of thunder, only much louder."

    slim mad "Soldiers descended from the cloud as an endless waterfall. The soldiers ran through the Ora attacking the Protectors."

    penny "The Protectors?"

    slim proud "Those assigned the task of protecting the Ora and maintaining the rate of Kia extraction. The Ora is generous but too much Kia extraction forces an imbalance in our eco-system and makes soil acidic so nothing will grow." 


    jump scene3b

    return 
