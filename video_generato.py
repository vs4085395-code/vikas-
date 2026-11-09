from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_video(script, output="short.mp4"):

    width, height = 1080, 1920

    image = Image.new(
        "RGB",
        (width, height),
        (15, 25, 45)
    )

    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(
            "DejaVuSans.ttf", 55
        )
    except:
        font = ImageFont.load_default()

    title_font = ImageFont.truetype(
        "DejaVuSans.ttf", 75
    )

    draw.text(
        (70, 200),
        "TECH & AI",
        font=title_font,
        fill=(0, 200, 255)
    )

    y = 450

    for line in textwrap.wrap(script, width=25):
        draw.text(
            (70, y),
            line,
            font=font,
            fill="white"
        )
        y += 100

    draw.text(
        (70, 1700),
        "FOLLOW FOR MORE!",
        font=font,
        fill=(0, 200, 255)
    )

    os.makedirs("videos", exist_ok=True)

    image.save("videos/thumbnail.png")

    print("Video design created successfully!")


if __name__ == "__main__":

    sample_script = """
    Artificial Intelligence is changing
    the world. AI can help us learn,
    work and solve difficult problems.
    """

    create_video(sample_script)
