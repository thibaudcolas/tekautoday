# tekautoday
Ten Years Ago, Today

## Installation

Those installation instructions should be executed inside the project root.

### Back-end setup

We use:

- [Python 3](https://www.python.org/) programming language.
- [Flask](http://flask.pocoo.org/) web framework.
- [virtualenv](https://virtualenv.pypa.io/en/latest/) and [pip](https://pypi.python.org/pypi/pip).

> If you don't already have Python 3 and virtualenv, you can install them with `brew install python3` and `pip install virtualenv`.

~~~sh
# First, create a Python 3 virtual environment with virtualenv.
virtualenv -p python3 env
# Then let's start it.
source env/bin/activate
# And install all our python dependencies.
pip install -r requirements.txt
~~~

### Front-end setup

We use:

- [Node.js](nodejs.org) JavaScript runtime and the [npm](https://www.npmjs.com/) ecosystem.
- [Browserify](http://browserify.org/) dependency builder and the [Babel](https://babeljs.io/) ES6/ES2015 transpiler.
- [React](https://facebook.github.io/react/) UI library, [jQuery](http://jquery.com/) and the [lodash](https://lodash.com/) utility library.

> If you don't already have Node and npm installed, you can get them with `brew install node`.

~~~sh
# First, install all front-end development global dependencies.
npm install --global gulp browserify eslint jscs browser-sync
# Then, install all project dependencies.
npm install
~~~


## Working on the project

