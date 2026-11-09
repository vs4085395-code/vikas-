import asyncio
import edge_tts

VOICE = "hi-IN-MadhurNeural"

async def create_audio(text, output_file="voice.mp3"):
    communicate = edge_tts.Communicate(
        text,
        VOICE
    )

    await communicate.save(output_file)

def generate_voice(text, output_file="voice.mp3"):
    asyncio.run(create_audio(text, output_file))
    print("Hindi male voice generated successfully!")
