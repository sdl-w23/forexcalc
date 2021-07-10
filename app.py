from flask import Flask, render_template, request, redirect, url_for
from forex_python.converter import CurrencyRates, convert, CurrencyCodes
from validity import errors, results


app = Flask(__name__)

codes = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        confrom = request.form["con-from"]
        conto = request.form["con-to"]
        amount = request.form["amount"]
        mistakes = errors(confrom, conto, amount)
        if not mistakes:
            message = results(confrom, conto, amount)
            return render_template('result.html', message=message)
        else:
            return render_template('error.html', mistakes=mistakes)
    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
