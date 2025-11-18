from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Демонстрация SHA-256</title>
</head>
<body>
  <h1>Демонстрация SHA-256 хеширования</h1>
  <p>Введите строку. Приложение посчитает её SHA-256 хеш.</p>
  <form method="post">
    <label>Строка для хеширования:</label>
    <input type="text" name="text" required>
    <button type="submit">Посчитать хеш</button>
  </form>

  {% if text is not none %}
    <h2>Результат</h2>
    <p><strong>Введённая строка:</strong> <code>{{ text }}</code></p>
    <p><strong>SHA-256 хеш:</strong></p>
    <p><code>{{ hash }}</code></p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    text = None
    hash_value = None
    if request.method == "POST":
        text = request.form["text"]
        hash_value = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return render_template_string(HTML, text=text, hash=hash_value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)