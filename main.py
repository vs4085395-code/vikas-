import random

print("AI YouTube Automation Started!")

# Read topics
with open("topics.txt", "r", encoding="utf-8") as file:
    topics = [
        line.strip()
        for line in file
        if line.strip()
    ]

if not topics:
    raise ValueError("No topics found!")

# Select a random topic
topic = random.choice(topics)

print("Today's Topic:", topic)
print("Topic selection successful!")
