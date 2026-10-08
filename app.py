import request

response = requests.get(url)
data = response.json()

print(data)

temperature = data["current"]["temperature_2m"]


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", city="", message="")


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city", "").strip()
    message = f"Je zoekt het weer voor {city}." if city else "Vul een plaats in om te zoeken."
    return render_template("index.html", city=city, message=message)


if __name__ == "__main__":
    app.run(debug=True)
