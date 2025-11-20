import re

# ---------------------------------------------------
# SYMPTOM DICTIONARIES (C-level: multi-symptom system)
# ---------------------------------------------------

RESPIRATORY = [
    "cough", "cold", "fever", "sore throat", "throat pain", "blocked nose",
    "runny nose", "sneezing", "mucus", "phlegm"
]

DIGESTIVE = [
    "stomach pain", "gas", "acidity", "bloating", "nausea", "vomiting",
    "loose motion", "diarrhea", "indigestion"
]

SKIN = [
    "rash", "itching", "redness", "dry skin", "acne", "bumps", "irritation"
]

MUSCLE = [
    "body pain", "back pain", "leg pain", "cramp", "joint pain", "muscle pain"
]

MENTAL = [
    "stress", "anxiety", "overthinking", "headache", "tiredness",
    "fatigue", "insomnia"
]

HYDRATION = [
    "dry mouth", "dizzy", "dizziness", "light headed", "thirsty"
]


# ---------------------------------------------------
# HELPER FUNCTION — CHECK MATCHES IN CATEGORY
# ---------------------------------------------------

def detect_symptoms(text, symptom_list):
    found = []
    for symptom in symptom_list:
        if symptom in text:
            found.append(symptom)
    return found


# ---------------------------------------------------
# MAIN FALLBACK LOGIC
# ---------------------------------------------------

def analyze_symptoms(text):
    text = text.lower()

    # Detect symptoms by category
    resp = detect_symptoms(text, RESPIRATORY)
    dig = detect_symptoms(text, DIGESTIVE)
    skin = detect_symptoms(text, SKIN)
    muscle = detect_symptoms(text, MUSCLE)
    mental = detect_symptoms(text, MENTAL)
    hydro = detect_symptoms(text, HYDRATION)

    # Nothing detected
    if not (resp or dig or skin or muscle or mental or hydro):
        return None

    # ---------------------------------------------------
    # CATEGORY RESPONSES (Medium length, 4–6 lines)
    # ---------------------------------------------------

    if resp:
        return (
            f"It looks like you're experiencing respiratory discomfort: {', '.join(resp)}. "
            "These symptoms often come from irritation or a mild infection. "
            "Try warm fluids, steam inhalation, and avoid cold foods for a day. "
            "Rest well, stay hydrated, and keep your throat warm. "
            "Monitor it calmly — most cases settle with proper rest and care."
        )

    if dig:
        return (
            f"You mentioned digestive symptoms: {', '.join(dig)}. "
            "This usually happens due to food irritation, indigestion, or acidity. "
            "Try warm water, light meals, avoid oily/spicy foods, and consider ORS if needed. "
            "Ginger tea or jeera water can help reduce discomfort. "
            "Take it easy for a bit and give your stomach time to settle."
        )

    if skin:
        return (
            f"These skin-related symptoms were detected: {', '.join(skin)}. "
            "Skin irritation can come from dryness, sweat, friction, or mild allergies. "
            "Keep the area clean, avoid harsh products, and moisturize gently. "
            "Aloe vera gel or cold compress can calm irritation. "
            "Watch how your skin reacts and avoid scratching to prevent worsening."
        )

    if muscle:
        return (
            f"You’re experiencing muscular discomfort: {', '.join(muscle)}. "
            "This often happens due to strain, posture issues, or lack of rest. "
            "Try light stretching, a warm compress, and avoid heavy activity for today. "
            "Stay hydrated and include salt/electrolytes if needed. "
            "Gentle movement usually helps relax tight muscles."
        )

    if mental:
        return (
            f"Your message shows signs of mental or stress-related symptoms: {', '.join(mental)}. "
            "These sensations are common when your mind is overloaded or your body is tired. "
            "Try slow breathing, short breaks, and hydration. "
            "Staying off screens for a while and doing something calm helps a lot. "
            "Small lifestyle resets usually bring quick relief."
        )

    if hydro:
        return (
            f"You may be experiencing hydration-related signs: {', '.join(hydro)}. "
            "These symptoms show your body needs more fluids or electrolytes. "
            "Drink water slowly, add ORS if available, and avoid long gaps without drinking. "
            "Fruits like watermelon, oranges, and cucumber can help restore fluids. "
            "Rehydrate gradually and rest if you're feeling low energy."
        )

    return None
