import random

PATH = "./data/secret"
MAX_HEIGHT = 1000
NUMBER_OF_FILES = 20

def generate(height: int, name: int) -> None:
	nums = "\n".join(
		" ".join(str(random.randint(-1000, 1000)) for _ in range(i))
		for i in range(height + 1)
	).strip()

	print(f"⏳ Generating {name}.in with height {height}")
	
	with open(f"{PATH}/{name}.in", "w") as file:
		file.writelines(str(height) + "\n" + nums + "\n")

	print(f"✅ Generated {name}.in")

for i in range(NUMBER_OF_FILES):
	generate(random.randint(1, MAX_HEIGHT), i)

generate(NUMBER_OF_FILES + 1, 21)