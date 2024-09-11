
# app.py
from app import create_app
import unittest
app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    app.run(debug=True)
