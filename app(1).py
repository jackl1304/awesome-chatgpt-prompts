from flask import Flask, render_template_string
import csv

app = Flask(__name__)

@app.route("/")
def index():
    prompts = []
    with open("prompts.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            prompts.append(row)
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Awesome ChatGPT Prompts</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .prompt { margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
            .prompt h3 { margin: 0 0 10px 0; }
        </style>
    </head>
    <body>
        <h1>Awesome ChatGPT Prompts</h1>
        {% for prompt in prompts %}
            <div class="prompt">
                <h3>{{ prompt['act'] }}</h3>
                <p>{{ prompt['prompt'] }}</p>
            </div>
        {% endfor %}
    </body>
    </html>
    """, prompts=prompts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
