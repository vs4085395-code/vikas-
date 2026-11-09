import os
from google import genai

def generate_script(topic):

    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found!")

    client = genai.Client(api_key=api_key)

    prompt = f"""
    You are a professional Hindi YouTube Shorts script writer.

    Create a 30-60 second YouTube Shorts script.

    Topic: {topic}

    Requirements:
    - Language: Simple Hindi
    - Start with a powerful hook.
    - Explain the topic in an interesting way.
    - Include useful facts.
    - End with a call to action.
    - No unnecessary introduction.

    Return only the script.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    topic = "Artificial Intelligence"
    script = generate_script(topic)

    print("\nGENERATED SCRIPT:\n")
    print(script)
