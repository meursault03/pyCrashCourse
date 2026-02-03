from pathlib import Path

learned_concepts = Path('learning_python.txt').read_text()
print(learned_concepts)
concepts_string = ''
for concept in learned_concepts.splitlines():
    concepts_string += concept.strip() + "\n"

print(concepts_string)

concepts_string = concepts_string.replace("Python", "C")
print(concepts_string)
