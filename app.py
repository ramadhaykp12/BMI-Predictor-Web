from flask import Flask, render_template, request, jsonify
import sklearn
import pickle

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def bmi_calculation(height,weight):
    global bmi
    height = height/100
    bmi = weight/height**2
    return bmi

@app.route('/predict', methods=['POST'])
def predict():
    gender_feature = float(request.form['gender'])
    height_feature = float(request.form['height'])
    weight_feature = float(request.form['weight'])

    # Load the model using pickle
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    predictions = model.predict([[gender_feature, height_feature, weight_feature]])

    if predictions == 0:
        predictions = 'Extremely weak'
    elif predictions == 1:
        predictions = 'Weak'
    elif predictions == 2:
        predictions = 'Normal'
    elif predictions == 3:
        predictions = 'Overweight'
    elif predictions == 4:
        predictions = 'Obesity'
    else:
        predictions = 'Extremely Obesity'

    bmi_calculation(height_feature,weight_feature)
    
    return render_template('result.html', predictions=predictions, bmi_calc=bmi)

if __name__ == '__main__':
    app.run(debug=True)