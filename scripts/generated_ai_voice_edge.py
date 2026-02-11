import asyncio
import edge_tts
import os

#save location
OUTPUT_DIR="data/raw/ai-generated/test"
os.makedirs(OUTPUT_DIR , exist_ok=True)

#text to convert
texts = [
"During my internship at 8Queens Software Pvt Ltd.",
"I gained practical experience working on real-world full-stack tasks.",
" where I enhanced my skills in Java, web development, and UI/UX principles.",
" I have also built projects such as a voice authentication system using FastAPI and React.",
" integrating audio processing with machine learning features.",
"which strengthened my problem-solving and system- integration capabilities."
]

#voices (male + female)
voices = [
    "en-US-GuyNeural",  # male voice
    "en-US-JennyNeural" # female voice
]

async def generate():
    count=39
    for voice in voices:
        for text in texts:
            file_name=f"{OUTPUT_DIR}/ai_{count}.wav"
            communicate=edge_tts.Communicate(text=text,voice=voice)
            await communicate.save(file_name)
            print(f"Saved:{file_name}")
            count+=1

asyncio.run(generate())
