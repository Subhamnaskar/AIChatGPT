import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "subham"
bot_name = "pawan"

while True:
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
    print("no longer listening")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=conversation,
        temperature=0.10,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    conversation+= response_str +"\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
    