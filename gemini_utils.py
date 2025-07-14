import google.generativeai as genai

# ✅ Directly configure API key here
genai.configure(api_key="AIzaSyBOICX3pQNQAU29gH9KAG5uMYf4n6qm_oU")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_script(topic, audience):
    prompt = f"""
You are a scriptwriter for YouTube videos. Generate a detailed script with:
- Scene-by-scene breakdown
- Voiceover narration
- Optional background actions or visuals
- A compelling call-to-action at the end

Topic: {topic}
Target Audience: {audience}

Format:
Scene 1: [Title]
Voiceover: ...
Visuals: ...

Scene 2: ...

CTA: ...
"""
    response = model.generate_content(prompt)
    return response.text
