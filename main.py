
# app.py
from flask import render_template
from app import create_app
import unittest
app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', code=404, message_for_error='Not Found', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', code=500, message_for_error='Internal Server Error', error=error)
if __name__ == '__main__':
    app.run(debug=True)
