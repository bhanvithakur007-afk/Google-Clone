
from flask import Flask, render_template_string, request
from duckduckgo_search import DDGS

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Google Clone</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #fff;
    text-align: center;
    margin: 0;
    padding: 0;
}

.container {
    margin-top: 150px;
}

.logo {
    font-size: 75px;
    font-weight: bold;
    margin-bottom: 30px;
}

.blue { color: #4285F4; }
.red { color: #EA4335; }
.yellow { color: #FBBC05; }
.green { color: #34A853; }

input {
    width: 500px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 30px;
    font-size: 16px;
    outline: none;
}

button {
    padding: 12px 25px;
    margin: 20px 5px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    background: #f2f2f2;
}

button:hover {
    background: #e5e5e5;
}

.results {
    text-align: left;
    max-width: 650px;
    margin: 40px auto;
}

.result {
    margin-bottom: 25px;
}

.result a {
    color: #1a0dab;
    font-size: 20px;
    text-decoration: none;
}

.result p {
    color: #444;
}
</style>
</head>

<body>
<div class="container">
    <div class="logo">
        <span class="blue">G</span><span class="red">o</span><span class="yellow">o</span><span class="blue">g</span><span class="green">l</span><span class="red">e</span>
    </div>

    <form method="POST">
        <input type="text" name="query"
        placeholder="Search anything..." required>
        <br>
        <button type="submit">Google Search</button>
    </form>
</div>

<div class="results">
{% for result in results %}
    <div class="result">
        <a href="{{ result.href }}" target="_blank">
            {{ result.title }}
        </a>
        <p>{{ result.body }}</p>
        <small>{{ result.href }}</small>
    </div>
{% endfor %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            try:
                with DDGS() as ddgs:
                    results = list(
                        ddgs.text(query, max_results=10)
                    )
            except Exception:
                results = []

    return render_template_string(
        HTML, results=results
    )

if __name__ == "__main__":
    app.run(debug=True)
