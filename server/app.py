#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers=[str(n) for n in range(0,parameter)]
    return '\n'.join(numbers)+('\n')
    
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        return str(num1+num2)
    if operation =="-":
        return str(num1-num2)
    if operation == '*':
        return str(num1*num2)
    if operation == 'div':
        return str(num1/num2)
    if operation == '%':
        return str(num1%num2)
        