from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        fa = float(request.form.get("fa"))
        va = float(request.form.get("va"))
        ca = float(request.form.get("ca"))
        rs = float(request.form.get("rs"))
        ch = float(request.form.get("ch"))
        fsd = float(request.form.get("fsd"))
        tsd = float(request.form.get("tsd"))
        density = float(request.form.get("density"))
        sulphates = float(request.form.get("sulphates"))
        alcohol = float(request.form.get("alcohol"))
        quality = float(request.form.get("quality"))
        model = pickle.load(open('svc_clf.pkl', 'rb'))
        prediction = model.predict([[fa, va, ca, rs, ch, fsd, tsd, density, sulphates, alcohol, quality]])[0]
        return redirect(url_for('res', prediction=prediction))
    return render_template('index.html')
@app.route('/results')
def res():
    prediction = request.args.get('prediction', default="Try again", type=float)
    return render_template('results.html', prediction=prediction)
if __name__ == '__main__':
    app.run(debug=True)
