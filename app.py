from flask import Flask,request, make_response,redirect, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/anuncios')
def anuncios():
    return render_template('anuncios.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.errorhandler(404)
def not_found(error):
    context = {
        'code': 404,
        'message_for_error' : 'Not Found',
        'error' : error
    }
    return render_template('error.html', **context)

@app.errorhandler(500)
def internal_server_error(error):
    context = {
        'code': 500,
        'message_for_error' : 'Internal Server Error',
        'error' : error
    }
    return render_template('error.html', **context)

if __name__ == '__main__':
    app.run()



