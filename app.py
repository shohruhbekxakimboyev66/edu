from flask import Flask, render_template, jsonify, request
import time


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/submit', methods=['POST'])
def submit():
    time.sleep(0.3)  # Realistik kechikish (loading effekti uchun)
    data = request.get_json()
    name = data.get('name', '').strip()

    if not name:
        return jsonify({"error": "Ismni kiriting!"}), 400

    return jsonify({
        "message": f"Assalomu alaykum, {name}! Sizning so'rovingiz qabul qilindi ✨",
        "timestamp": time.strftime("%H:%M:%S")
    })


@app.route('/api/quote')
def random_quote():
    quotes = [
        "Dunyodagi eng yaxshi narsalar bepul: quyosh, oy va yulduzlar 🌞",
        "Har kunning o'z go'zalligi bor. Uni ko'ra olmoqdigan ko'z kerak 👁️",
        "Chiroy tabiatda emas, uni ko'ra oladigan qobiliyatda yashirin 🌸",
        "Yuragingizni ochiq qoldiring — go'zallik uni topadi ❤️"
    ]
    import random
    return jsonify({"quote": random.choice(quotes)})


if __name__ == '__main__':
    app.run(debug=True)