from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def start_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = add(a, b)
    return str(answer)

@app.route('/sub')
def start_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = sub(a, b)
    return str(answer)

@app.route('/mult')
def start_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = mult(a, b)
    return str(answer)

@app.route('/div')
def start_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = div(a, b)
    return str(answer)

# copied below from solution

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)


