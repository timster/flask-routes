from setuptools import setup
from codecs import open
from os import path

from flask_routes import __version__

root_dir = path.abspath(path.dirname(__file__))

with open(path.join(root_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='flask-routes',
    version=__version__,

    description='Command line extension to list all routes in a Flask project',
    long_description=long_description,

    url='https://github.com/timster/flask-routes',

    author='Tim Shaffer',
    author_email='timshaffer@me.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Database :: Front-Ends',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points={
        'flask.commands': [
            'routes = flask_routes:command',
        ],
    },

    keywords='flask routes routing api documentation',

    py_modules=['flask_routes'],
)