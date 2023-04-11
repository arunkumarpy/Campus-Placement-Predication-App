from flask import *
import pickle 
import joblib
from tensorflow.keras.models import load_model
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("D:\\Pyenv\\ArunKumar\\Campus_Placement\\templates"))


app = Flask(__name__)

model = pickle.load(open("placement.pkl", "rb"))


@app.route('/')
def index():
    template = env.get_template('index.html')
    return render_template(template)

@app.route('/details')
def details():
    template = env.get_template('home.html')
    return render_template(template)


@app.route("/predict", methods = ["POST","GET"])
def predict():
    values_list = list(request.form.values()) 
    fname = values_list[0]
    req_values = values_list[1:8]

    x_test = [[int(x) for x in req_values]]

    predication = model.predict(x_test)
    predict = predication[0]
    print(predict)

    if predict == 1:
        template = env.get_template('chance.html')
        return render_template(template, predict="You Got Selected.")
    else:
        template = env.get_template('nochance.html')
        return render_template(template, predict="You Are Not Selected.")
        

if __name__ == "__main__":
    app.run(debug=True)