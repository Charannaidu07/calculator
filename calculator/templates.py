from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'charan'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        def get_value(field_name):
            value = request.form.get(field_name, '')
            return value if value else 0
        exp = get_value("Expression")
        result = eval(exp)
        print("Result:", result)
        return render_template('result.html', result=result)
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
