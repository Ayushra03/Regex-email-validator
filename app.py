from flask import Flask,render_template,request
import re


app=Flask(__name__)


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/regex_page')
def regexvalidate():
    return render_template('regex_page.html')

@app.route('/email_page')
def emailvalidate():
    return render_template('email_page.html')


@app.route('/regex_result', methods=['POST'])
def regex_result():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    match_result = re.findall(regex_pattern, test_string)
    return render_template('regex_result.html', match_result=match_result)

@app.route('/validate_email',methods=['POST'])
def email_result():
    email = request.form['email']
    if(validate_email(email)):
        return "<h1>Valid Email</h1>"
    
    return "<h1>Invalid Email</h1>"



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")