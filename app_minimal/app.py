from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.before_request
def before_request():
    print('before request')

@app.after_request
def after_request(response):
    print('after request')
    return response


@app.route('/')
def index():
    test_list = ['test1', 'test2', 'test3']
    data = {
        'title': 'Coca-Cola Reports',
        'message': 'testing',
        'test': test_list,
        'test_lenght': len(test_list),
    }
    return render_template('index.html', data=data)

@app.route('/contacto/<name>/<int:edad>')
def contacto(name, edad):
    data = {
        'title': 'Contacto',
        'name': name,
        'edad': edad or 0,
    }
    return render_template('contact.html', data = data )

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "ok"

def page_not_found(error):
    # return redirect(url_for('index'))
    return render_template('404.html'), 404


if __name__=='__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5000)