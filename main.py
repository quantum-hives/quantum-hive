# Internals modules

# Projects modules
from Classes.Objects import Objects

# Externals modules

grain = Objects("Grain", "Consommable", "Des grains pour faire le café.", 64, None)
cafetiere = Objects("Cafetière", "Petit électro-ménager", "Une cafetière, pour faire le café.", 1, grain)

print(cafetiere.get_name())
print(cafetiere.get_type())
print(cafetiere.get_desc())
print(cafetiere.get_stock())
print(cafetiere.get_child())
