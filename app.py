from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, RatesNotAvailableError

app = Flask(__name__)
c = CurrencyRates()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    try:
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()
        result = c.convert(from_currency, to_currency, amount)
        return f"<h1>{amount} {from_currency} = {result:.2f} {to_currency}</h1>"
    except RatesNotAvailableError:
        return "<h1>Error: Currency rates not available.</h1>"
    except Exception as e:
        return f"<h1>Error: {e}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
