from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def test():
    input=request.args.getlist('i')
    print(len(input))
    return '12'
def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()