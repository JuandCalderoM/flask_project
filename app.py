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

if __name__ == '__main__':
    app.run()



