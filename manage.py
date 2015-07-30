import os
from __init__ import create_app
from flask_script import Manager
from flask_script import Server

app = create_app()
app.config['DEBUG'] = True
manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=9004))


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()