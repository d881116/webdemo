from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    description = data.get("description", "")
    model_name = data.get("model", "model1")

    if model_name == "model1":
        tags = model1_predict(description)
    elif model_name == "model2":
        tags = model2_predict(description)
    elif model_name == "model3":
        tags = model3_predict(description)
    else:
        tags = ["未知模型"]

    return jsonify({"tags": tags})

def model1_predict(text):
    return [f"model1 return: {text}"]

def model2_predict(text):
    return [f"model2 return: {text}"]

def model3_predict(text):
    return [f"model3 return: {text}"]

'''if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)'''


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
