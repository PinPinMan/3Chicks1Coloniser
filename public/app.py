from openai import OpenAI
from flask import Flask, render_template, request, url_for, redirect, send_from_directory
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
client = OpenAI(api_key=API_KEY)
app = Flask(__name__)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('../public/download/', filename)

@app.route('/safe/<prediction>', methods=['GET', 'POST'])
def safe(prediction):
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('safe.html', prediction=prediction)

@app.route('/suspicious/<prediction>', methods=['GET', 'POST'])
def suspicious(prediction):
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('suspicious.html', prediction=prediction)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST' and request.form['textarea'] != "":
        # Process the submitted data to determine prediction
        prediction = predict_scam(request.form['textarea'])
        print(prediction)

    if prediction == 'Error':
        return render_template('index.html', prediction='Error')
    elif prediction == None:
        return render_template('index.html')
    elif int(prediction.split('%')[0][prediction.find('Yes-(')+5:] or prediction.split('%')[0][prediction.find('No-(')+4:]) > 50:
        return redirect(url_for('suspicious', prediction=prediction))
    else:
        return redirect(url_for('safe', prediction=prediction))



def predict_scam(text):
    try:
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{text}, does this sound like a Financial Scam? output format'Yes-(Percentage), No-(Percentage)' (include both percentages)"}],
        )
        response = stream.choices[0].message.content
        return response
    except:
        return 'Error'


if __name__ == '__main__':
    app.run(port=3000, debug=True)
