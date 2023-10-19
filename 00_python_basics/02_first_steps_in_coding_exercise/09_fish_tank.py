aquarium_height = int(input())
aquarium_width = int(input())
aquarium_length = int(input())
percentage_filled = float(input())
percentage_filled = (percentage_filled * 0.01)
aquarium_volume = (aquarium_width * aquarium_length * aquarium_height) * 0.001
aquarium_volume_available = float(aquarium_volume * (1 - percentage_filled))
print(aquarium_volume_available)