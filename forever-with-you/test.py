import forever_with_you as fwy
import sys
sys.path.insert(0, '/mnt/data')
# Example argument, use the language depending on context, supports: en, jp, cn
game_state = fwy.initialize_game_state("cn")

# image_grid = fwy.show_characters("cn")


# character_image = fwy.show_character("Mio Kisaragi")

print(game_state["all_characters"])

game_state = fwy.update_relationship("Mio Kisaragi", -5, +5, +5)
game_state = fwy.update_relationship("Shiori Fujisaki", +5, -5, 0)


print(game_state["relationships"])
