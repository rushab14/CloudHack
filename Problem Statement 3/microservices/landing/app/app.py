from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


# def add(n1, n2):
#     return n1+n2

# def minus(n1, n2):
#     return n1-n2

# def multiply(n1, n2):
#     return n1*n2

# def divide(n1, n2):
#     return n1/n2

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    if(number_1 is not None and number_2 is not None):

        if operation == 'add':
            res = (requests.get("http://addition:5051/"+number_1+'/'+number_2)).json()

        elif operation == 'minus':
            res = (requests.get("http://subtraction:5052/"+number_1+'/'+number_2)).json()

        elif operation == 'multiply':
            res = (requests.get("http://multiplication:5053/"+number_1+'/'+number_2)).json()

        elif operation == 'divide':
            res = (requests.get("http://division:5054/"+number_1+'/'+number_2)).json()

        elif operation == 'modulus':
            res = (requests.get("http://modulus:5055/"+number_1+'/'+number_2)).json()

        elif operation == 'gcd':
            res = (requests.get("http://gcd:5056/"+number_1+'/'+number_2)).json()

        elif operation == 'lcm':
            res = (requests.get("http://lcm:5057/"+number_1+'/'+number_2)).json()

        elif operation == 'exponent':
            res = (requests.get("http://exponent:5058/"+number_1+'/'+number_2)).json()

        elif operation == 'greater_than':
            res = (requests.get("http://gt:5059/"+number_1+'/'+number_2)).json()

        elif operation == 'less_than':
            res = (requests.get("http://lt:5060/"+number_1+'/'+number_2)).json()

        elif operation == 'equals':
            res = (requests.get("http://eq:5061/"+number_1+'/'+number_2)).json()

        if(res["error"]):
            flash(res["errMsg"])
        else:
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {res["result"]}')
    else:
        flash(f'Do math')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )