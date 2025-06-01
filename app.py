from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/battery', methods=['GET', 'POST'])
def battery():
    result = None
    if request.method == 'POST':
        x폭행1 = request.form.get('x폭행1') == 'True'
        x폭행2 = request.form.get('x폭행2') == 'True'
        x폭행3 = request.form.get('x폭행3') == 'True'
        result = x폭행1 and x폭행2 and not x폭행3
    return render_template('battery.html', result=result)

@app.route('/fraud', methods=['GET', 'POST'])
def fraud():
    result = None
    if request.method == 'POST':
        x사기1 = request.form.get('x사기1') == 'True'
        x사기2 = request.form.get('x사기2') == 'True'
        x사기3 = request.form.get('x사기3') == 'True'
        result = x사기1 and x사기2 and not x사기3
    return render_template('fraud.html', result=result)

@app.route('/molestation', methods=['GET', 'POST'])
def molestation():
    result = None
    if request.method == 'POST':
        x추행1 = request.form.get('x추행1') == 'True'
        x추행2 = request.form.get('x추행2') == 'True'
        x추행3 = request.form.get('x추행3') == 'True'
        result = x추행1 and x추행2 and not x추행3
    return render_template('molestation.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
