import random
import re
import json
import itertools
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import zipfile
import io
from PIL import Image

# https://w.atwiki.jp/tokimekicn/pages/16.html
# https://tokimemo.fandom.com/wiki/Category:TM1_Characters

game_state = {}


# Characters
characters = {
    "Shiori Fujisaki": {
        "name": {
            "en": "Shiori Fujisaki",
            "jp": "ふじさき しおり",
            "cn": "藤崎 诗织",
        },
        "profile": "She is the primary protagonist of Tokimeki Memorial, and the main character's best friend from childhood. Over the years, your relationship has slowly started to drift apart, but you two are still friends. However, in order to make the next leap you must become closer to Shiori.\nShiori is loved by all the guys in Kirameki High. She's beautiful, smart, kind, and good at everything from academics to sports; there's very little Shiori can't do. About the only thing Shiori isn't good at inside-out is anything that involves love, something still awkward for her.\nDue to their initial relationship, Shiori is perhaps the easiest to make fall in love with the protagonist (the blushing stage) but is considered to be one of the hardest characters to win in the game, having very high demands for anyone who wants to be her boyfriend. You must have high stats in everything to win her over, as well as get her into the blushing stage. You must also get into a first-class university, as that is what Shiori aims for upon completion of high school.\nHer best friend is Megumi Mikihara, though early promotion art often showed her with Yumi Saotome and Rei Ijuuin as well (who's liked by the girls in school in the same manner as Shiori is by the guys).",
        "date_events": [
            "Spring: Reminiscing about your childhood memories at Kirameki Central Park.",
            "Summer: Having fun on the water slide at the pool.",
            "Fall: Rediscovering your old height comparison notches on a tree at the local playground.",
            "Winter: The Ferris wheel at the Amusement Park leaves you both stuck at the top, and Shiori is scared until you move in close and take her mind off the ride stalling with the great view."
        ],
        "special_events": [
            "When you enter both Shiori's and your birthday on the same date in March and it is a holiday in either Year 2 or Year 3, (e.g. 21st of March on PlayStation version for 1996/1997), a special event may occur. On that day if she is in Tokimeki State, Shiori will call you and celebrate your birthday together in her room. During that time, Shiori will show you a ring which you gave her as a birthday present 10 years ago.",
            "If Shiori is in Tokimeki State at Rei's Christmas party, afterwards you will walk home with her and see snow falling for a white Christmas."
        ],
        "ending_requirements": "Health 30+, Culture 130+, Logic 130+, Art 130+, Fitness 110+, Insight 110+, Looks 100+, Spirit 100+, Stress 50-."
    },
    "Mio Kisaragi": {
        "name": {
            "en": "Mio Kisaragi",
            "jp": "きさらぎ みお",
            "cn": "如月 未绪",
        },
        "first_dialgoue": "Nice to meet you. I am Mio Kisaragi. I am in the same class as you. I hope we can get along.",
        "profile": "Mio is a gentle and polite girl who has a weak body, and as such she's not good with sports. She always has her nose in a book, and her favorite author is Goethe. Her best friend is Saki Nijino.\nShe is also one of the only two characters in Tokimeki Memorial to feature an alternate ending. The primary difference between the endings is whether or not she chooses to switch to contacts, depending on what the player told her during her date event at the movie theater. After graduation, she plans to go to a first-rate university.",
        "date_events": [
            "Spring: If she is in Tokimeki State during a date to the Amusement Park in year 3, you can convince Mio to ride the new scream machine, but she faints during the intense ride.",
            "Summer: At the beach, you spend the time hiding from the sun together under a large beach umbrella.",
            "Fall: Mio loses herself in a book at the library during your date, and cannot hear you calling her name."
            "Winter: Mio cannot keep herself from crying at the romance movie you are watching together on a date during year 3. She is not confident in how she looks without her glasses and asks your opinion. This choice determines which ending (glasses or contacts) you will get.",
            "Super Famicom: While shopping, you find a love compatibility machine and give it a try."
        ],
        "special_events": [
            "During school, you come across her in the hallway carrying a large stack of books and offer to help."
        ],
        "ending_requirements": "Culture 130+, Fitness 100+ and Looks 100+."
    },
    "Miharu Tatebayashi": {
        "name": {
            "en": "Miharu Tatebayashi",
            "jp": "たてばやし みはる",
            "cn": "館林 見晴",
        },
        "first_dialgoue": "Hello. I am Miharu Tatebayashi. I am in the same class as you. I hope we can get along.",
        "profile": "She is often referred to as the \"consolation prize\" girl in the first series. She is a hidden character who cannot be scheduled for dates, although she will frequently \"misdial\" the player in the evenings, bump into him in the halls at school, or run into him before dates.",
        "date_events": [
        ],
        "special_events": [
            "In her only in-game event, known as the \"222 Event\", she invites the player out on a date at the end of which she tearfully gives up on him. To trigger this event, you must have no dates on February 22th of the 3rd Year and have at least one girl in Tokimeki State."
        ],
        "ending_requirements": "The ending requirements for Miharu are uncertain, but make sure you have no girls in Tokimeki State."
    },
    "Megumi Mikihara": {
        "name": {
            "en": "Megumi Mikihara",
            "jp": "みきはら めぐみ",
            "cn": "美树原爱",
        },
        "profile": "Megumi is Shiori's best friend, and is a shy girl who is afraid to speak to boys. She has a soft spot for animals, and has a pet Yorkshire Terrier named Muku.",
        "date_events": [
            "Spring: Megumi is nearly \"kidnapped\" as part of the hero stage show at the Amusement Park, until you tell the actor to back off. She worries that she was mistaken for a child, but you reassure her, telling her that she was too cute to leave alone.",
            "Summer: If she is in Tokimeki State, Megumi introduces you to a family member--her dog, Muku. Muku is not so pleased to meet you, however, and bites you out of jealousy over Megumi's attentions.",
            "Fall: Megumi is engrossed in watching the monkeys at the zoo and doesn't hear you when you want to look at a weird animal with her.",
            "Winter: If she is in Tokimeki State, Megumi topples over at the skating rink, landing squarely against your chest. She almost doesn't want to try to stand on her own..."
        ],
        "special_events": [
            "A downpour occurs after school, but Megumi has forgotten her umbrella. You offer to share yours with her, and the two of you walk home together under the same umbrella if her affection is high enough. Otherwise, you simply lend her your umbrella as sharing it would be far too embarrassing for her, and she returns it the next day."
        ],
        "ending_requirements": "Culture 50+, Culture 100+, Logic 100+, Art 100+, Fitness 100+, Insight 100+, Looks 100+, Spirit 70+, Stress 30-."
    },
    "Yuina Himoo": {
        "name": {
            "en": "Yuina Himoo",
            "jp": "ひもお ゆいな",
            "cn": "纽绪结奈",
        },
        "profile": "Yuina is a technophile who one day hopes to rule the world through the use of giant robots. She likes to bully Kyoko Izumi around, but her true archnemesis is the dreaded KOALA.",
        "date_events": [
            "Spring: On a date at the zoo, Yuina is attacked by a koala.",
            "Summer: Yuina bowls a perfect game--according to the scoring computer she hacked. Her actual game was definitely not that good.",
            "Fall: Taking her to the medal corner at the arcade, you see Yuina racking up the jackpots... and notice a suspicious cord trailing from her sleeve into the machine she is playing.",
            "Winter: The mad scientist in Yuina is laid bare, and she goes hog wild at the junk shop's big sale. The bad news is that you have to carry EVERYTHING she buys...",
            "SFC: On your birthday, if Yuina is in Tokimeki State, she will drop by your house with a \"present\"--you get to be a guinea pig and test one of her three experimental medicines. (The good one is orange, and will raise your science stat to 999 for one week.)"
        ],
        "special_events": [
            "At school, you find Yuina sighing on the rooftop. She is in a slump, but you snap her out of it."
        ],
        "ending_requirements": "Logic 120+, Insight 100+, Looks 60+. Also, you should aim for better grades than her."
    },
    "Saki Nijino": {
        "name": {
            "en": "Saki Nijino",
            "jp": "にじの さき",
            "cn": "虹野沙希",
        },
        "profile": "Saki is a big fan of baseball and soccer, and even serves as the manager of the soccer team at Kirameki High (later installments from the franchise seem to skew her interests exclusively toward soccer). Her motto is \"Have guts!\". She's more of a cheerleader than a sports player, though, and is often seen raising morale for the team she coaches. Thus, her type of boys are those who are strong-willed, and perserverant in everything they're doing.\nShe also loves to cook and is very talented at it, and if you (the player) are friendly towards Saki, she'll even make you a bentō (boxed lunch). She'll enter a professional college of cooking after graduation.\nMio Kisaragi and she are best friends.\nFor dating spots, she's very versatile: unlike most of the girls of the game, there's no real date spot she hates ; however, she tends to like sports-themed places the most. It also helps if you join the sports club she's part of.",
        "date_events": [
            "Spring: Saki brings a picnic for both of you to have on the lawn at Kirameki Central Park.",
            "Summer: If she is in Tokimeki State, Saki nearly drowns at the swimming pool, but comes to just as you were about to administer rescue breathing... cursing her bad timing.",
            "Fall: Saki cheers very enthusiastically at a baseball game.",
            "Winter: A lost child clings to Saki at the fancy shop and refuses to leave her, forcing you to go to the lost child station to call for his mother.",
            "SFC: While shopping, Saki finds a prize roulette for you to give a spin."
        ],
        "special_events": [
            "At lunch, Saki asks you to taste test her new bento recipe before she starts making them for her club. She later asks you to try it again after she's made a few changes. The first bento event is actually necessary to trigger Yumi's bento event."
        ],
        "ending_requirements": "Culture 120+, Fitness 100+, Looks 100+."
    },
}


def initialize_game_state(lang: str = "en"):
    global game_state
    new_characters = {}
    relationships = {}
    all_characters = list(characters.keys())

    for character, details in characters.items():
        new_characters[character] = {
            "display_name": details["name"].get(lang, details["name"]["en"]),
            "profile": details["profile"],
            "date_events": details["date_events"],
            "special_events": details["special_events"],
            "ending_requirements": details["ending_requirements"]
        }
        relationships[character] = {
            "tokimeki_degree": 30,
            "friendly_degree": 30,
            "heart_broken_degree": 30,
            "bomb": False
        }

    game_state = {
        "stats": {
            "health": 100,
            "culture": 100,
            "logic": 100,
            "art": 100,
            "fitness": 100,
            "insight": 100,
            "looks": 100,
            "spirit": 100,
            "stress": 0
        },
        "all_characters": all_characters,
        "characters": new_characters,
        "relationships": relationships
    }
    return game_state
#


def show_characters(lang: str = "en"):
    # Open the zip file
    with zipfile.ZipFile("/mnt/data/characters.zip", "r") as characters_zip:
        # Create a 1x3 grid of subplots with black background and no axis number values
        fig, axes = plt.subplots(2, 3, figsize=(10, 6), facecolor='black')

        # Loop through the remaining subplots
        for i in range(2):
            for j in range(3):
                # Get the character name from the "characters" list
                character_name = game_state["all_characters"].pop(0)

                # Create the image path for the character
                character_image_path = f"{character_name}.jpg"
                with characters_zip.open(character_image_path) as file:
                    character_image_data = file.read()

                # Display the character image using PIL (Pillow)
                character_image = Image.open(io.BytesIO(character_image_data))
                name = characters[character_name]["name"].get(
                    lang, characters[character_name]["name"]["en"])
                axes[i, j].imshow(character_image)
                axes[i, j].set_title(character_name, color='white')
                axes[i, j].axis('off')

        # Adjust layout and display the grid of images
        plt.tight_layout()
        plt.show()


def show_character(character_name):
    # Path to the zip file containing character images
    zip_file_path = '/mnt/data/characters.zip'
    # zip_file_path = 'characters.zip'

    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as characters_zip:
        character_image_file = f"{character_name}.jpg"

        if character_image_file in characters_zip.namelist():
            with characters_zip.open(character_image_file) as file:
                character_image = Image.open(io.BytesIO(file.read()))

            # Create a figure with a specific aspect ratio and face color
            # Example size, can be adjusted
            fig, ax = plt.subplots(figsize=(8, 2.5))
            fig.patch.set_facecolor('black')

            # Calculate padding for width to create a wide banner effect
            padding_width = character_image.size[0] * 1.5
            total_width = padding_width * 2 + character_image.size[0]

            # Calculate the extent of the image to be at the center
            left_extent = padding_width
            right_extent = padding_width + character_image.size[0]

            # Set title properties
            plt.title(character_name, color='white', fontsize=15)

            # Display the image
            ax.imshow(character_image, aspect="1", extent=(
                left_extent, right_extent, character_image.size[1], 0))

            # Set the plot limits to include padding
            ax.set_xlim(0, total_width)
            # Inverted to correct upside down issue
            ax.set_ylim(character_image.size[1], 0)

            # Remove axis
            ax.axis('off')

            # Show the plot with the image centered
            plt.show()
        else:
            print(f"Image for '{character_name}' not found in the zip file.")


def update_relationship(character_name, adjust_tokimeki_degree, adjust_friendly_degree, adjust_heart_broken_degree):
    if character_name in game_state['relationships']:
        game_state['relationships'][character_name]['tokimeki_degree'] = min(max(
            game_state['relationships'][character_name]['tokimeki_degree'] + adjust_tokimeki_degree, 0), 100)
        game_state['relationships'][character_name]['friendly_degree'] = min(max(
            game_state['relationships'][character_name]['friendly_degree'] + adjust_friendly_degree, 0), 100)
        game_state['relationships'][character_name]['heart_broken_degree'] = min(max(
            game_state['relationships'][character_name]['heart_broken_degree'] + adjust_heart_broken_degree, 0), 100)
    else:
        print(f"Character {character_name} does not exist.")
    return game_state
