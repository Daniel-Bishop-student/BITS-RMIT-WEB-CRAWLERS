## Declare characters used by this game. The color argument colorizes the name
## of the character.

label character_declarations:


    define all_characters = Character('All', image="all_side")
    image side all_side happy = "side_images/side_image_all_happy_03.png"
    image side all_side surprised = "side_images/side_image_all_surprised_03.png"
    define choice_character = Character('', image="choice_side")
    image side choice_side choice = "side_images/side_image_make_choice_03.png"

    # Main Characters & Side Images

    define harry = Character('harry_name', dynamic=True, image="harry_side")
    image side harry_side happy = "side_images/side_image_harry_happy_03.png"
    image side harry_side excited = "side_images/side_image_harry_excited_03.png"
    image side harry_side mad = "side_images/side_image_harry_mad_03.png"
    image side harry_side surprised = "side_images/side_image_harry_surprised_03.png"
    image side harry_side confused = "side_images/side_image_harry_confused_03.png"

    define benji = Character('benji_name', dynamic=True, image="benji_side")
    image side benji_side happy = "side_images/side_image_benji_happy_03.png"
    image side benji_side excited = "side_images/side_image_benji_excited_03.png"
    image side benji_side mad = "side_images/side_image_benji_mad_03.png"
    image side benji_side surprised = "side_images/side_image_benji_surprised_03.png"

    define penny = Character('penny_name', dynamic=True, image="penny_side")
    image side penny_side happy = "side_images/side_image_penny_happy_03.png"
    image side penny_side mad = "side_images/side_image_penny_mad_03.png"
    image side penny_side sad = "side_images/side_image_penny_sad_03.png"
    image side penny_side surprised = "side_images/side_image_penny_surprised_03.png"

    define jax = Character('Jax', image="jax_side")
    image side jax_side bark = "side_images/side_image_jax_bark_03.png"
    image side jax_side mad = "side_images/side_image_jax_mad_03.png"

    define grandma = Character('Grandma', image="grandma_side")
    image side grandma_side happy = "side_images/side_image_grandma_happy_03.png"

    define slim = Character('Slim', image="slim_side")
    image side slim_side happy = "side_images/side_image_slim_happy_03.png"
    image side slim_side excited = "side_images/side_image_slim_excited_03.png"
    image side slim_side mad = "side_images/side_image_slim_mad_03.png"
    image side slim_side proud = "side_images/side_image_slim_proud_03.png"

    define killsalot = Character('Killsalot', image="killsalot_side")
    image side killsalot_side mad1 = "side_images/side_image_killsalot_mad1_03.png"
    image side killsalot_side mad2 = "side_images/side_image_killsalot_mad2_03.png"
    image side killsalot_side mad3 = "side_images/side_image_killsalot_mad3_03.png"
    image side killsalot_side surprised = "side_images/side_image_killsalot_surprised_03.png"


    define xeena = Character('Xeena', image="xeena_side")
    image side xeena_side happy = "side_images/side_image_xeena_happy_03.png"
    image side xeena_side proud = "side_images/side_xeena_proud_03.png"

    define soldiers = Character('Soldiers', image="soldiers_side")
    image side soldiers_side gang =  "side_images/side_image_soldiers_03.png"

    return