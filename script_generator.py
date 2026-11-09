def generate_script(topic):

    script = f"""
क्या आप जानते हैं?

आज हम बात करेंगे {topic} के बारे में।

यह technology हमारी दुनिया को
तेजी से बदल रही है।

इसका इस्तेमाल education,
business और daily life में
लगातार बढ़ रहा है।

आने वाले समय में यह technology
हमारे काम करने का तरीका बदल सकती है।

ऐसी ही interesting technology
जानकारी के लिए follow करें!
"""

    return script


if __name__ == "__main__":
    topic = "Artificial Intelligence"
    print(generate_script(topic))
