from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Адреса бэкендов
backend_sum_server = "http://backend-sum:5000"
backend_multiply_server = "http://backend-multiply:5000"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    backend_used = None

    if request.method == "POST":
        num1 = float(request.form.get("num1"))
        num2 = float(request.form.get("num2"))

        # Вызываем бэкенд для суммирования чисел
        sum_response = requests.post(f"{backend_sum_server}/sum", json={"num1": num1, "num2": num2})
        sum_result = sum_response.json()

        # Вызываем бэкенд для умножения чисел
        multiply_response = requests.post(f"{backend_multiply_server}/multiply", json={"num1": num1, "num2": num2})
        multiply_result = multiply_response.json()

        result = {
            "sum": sum_result["result"],
            "multiply": multiply_result["result"]
        }
        
        backend_used = {
            "sum": sum_result["used_backend"],
            "multiply": multiply_result["used_backend"]
        }

    return render_template("index.html", result=result, backend_used=backend_used)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
