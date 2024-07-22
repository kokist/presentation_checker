import edge_tts
import asyncio

async def text_to_mp3(text):
    filename = "temp/pronunciation.mp3"
    voice_type = "en-US-AriaNeural"
    
    communicate = edge_tts.Communicate(text, voice_type)
    await communicate.save(filename)

    return filename

def text_to_mp3_sync(text):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    filename = loop.run_until_complete(text_to_mp3(text))
    loop.close()

    return filename
