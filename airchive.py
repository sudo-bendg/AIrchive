import os
from pathlib import Path
from google import genai

geminiKey = os.getenv("GOOGLE_GEMINI_KEY")

client = genai.Client(api_key=geminiKey)

def generateFileSummary(file):
    fileContent = Path(file).read_text()
    prompt = "Give a a brief description of the following file. Make the description a maximum of 5 sentences long, but make it as short as possible while giving a good description. Give metainformation, not an exact description of the contents:\n" + fileContent
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    print(response.text)

generateFileSummary("testfile")