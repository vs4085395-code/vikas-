import random
from script_generator import generate_script
from voice_generator import generate_voice
print("AI YouTube Automation Started!")

with open("topics.txt", "r", encoding="utf-8") as file:
    topics = [line.strip() for line in file if line.strip()]

if not topics:
    raise ValueError("No topics found!")

topic = random.choice(topics)

print("Selected Topic:", topic)

script = generate_script(topic)
generate_voice(script)
print("Voice generation completed!")
with open("script.txt", "w", encoding="utf-8") as file:
    file.write(script)

print("Hindi script generated successfully!")
