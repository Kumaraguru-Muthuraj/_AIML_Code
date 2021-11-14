from flask import Flask, jsonify,  request, render_template
import joblib
import numpy as np

app = Flask(__name__)
#model_load = joblib.load("./models/rf_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if (request.method == 'POST'):
        int_features = [x for x in request.form.values()]
        final_features = [np.array(int_features)]
        #output = model_load.predict(final_features).tolist()
        return render_template('index.html', prediction_text='Top 5 items recommended are {}'.format(['Item 1', 'Item23']))
    else:
        return render_template('index.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)
    app.debug=True
    app.run()
