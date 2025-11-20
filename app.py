from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from symptom_engine import analyze_symptoms

# ----------------------------
# FLASK APP
# ----------------------------
app = Flask(__name__)

# ----------------------------
# GEMINI API CONFIG
# ----------------------------
genai.configure(api_key="AIzaSyAOMvYnY9smKriC8UjBcLKJCjmaGAMvA0I")
model = genai.GenerativeModel("gemini-2.5-flash")


# ----------------------------
# HYBRID AI SYSTEM
# ----------------------------
def hybrid_ai(user_text):
    """
    1. Try Gemini AI
    2. If fail -> Symptom Engine
    3. If no match -> generic wellness advice
    """

    # ----- 1. Try Gemini AI -----
    try:
        prompt = f"""
        You are a friendly health & wellness AI assistant.
        Respond clearly, medium-length (4-6 lines), helpful and non-scary.

        User message: {user_text}
        """

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text.strip()

    except Exception:
        pass  # If Gemini fails → fallback


    # ----- 2. Use Symptom Engine -----
    symptom_reply = analyze_symptoms(user_text)
    if symptom_reply:
        return symptom_reply

    # ----- 3. Final fallback -----
    return (
        "Here are some general wellness tips: stay hydrated, get enough sleep, "
        "eat whole foods, move your body daily, and keep stress low."
    )


# ----------------------------
# ROUTES
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_msg = data.get("msg", "")
    bot_reply = hybrid_ai(user_msg)
    return jsonify({"reply": bot_reply})


# ----------------------------
# RUN APP
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
