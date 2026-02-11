from gtts import gTTS

texts = [ 
"I am writing to express my interest in the Software Developer position at Posmark carrers." 
]

for i, text in enumerate(texts):
    tts = gTTS(text=text, lang='en')
    tts.save(f"data/raw/ai-generated/ai_{i}.wav") 
