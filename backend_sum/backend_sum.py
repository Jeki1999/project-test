from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2

    response = {
        'result': result,
        'used_backend': 'Sum Backend'
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
