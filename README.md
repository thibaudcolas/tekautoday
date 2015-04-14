[Tekau Today](http://www.tekautoday.xyz/)
==========

> Ten Years Ago, Today

- [Production site](http://www.tekautoday.xyz/)
- [Trello board](https://trello.com/b/ytZCXTVM/tekau-today)

## Installation

These installation instructions should be executed inside the project root.

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
gem install scss-lint
# Then, install all project dependencies.
npm install
~~~

## Working on the project

> Everything mentioned in the installation process should already be done.

~~~sh
# Always start by activating Python's virtualenv.
source env/bin/activate
# Then start the server and the development tools.
npm run start
# Voilà!
# You can then go to http://localhost:3000/ to see the site running.
# When you feel like it, you can run the tests.
npm run test
~~~

## Deployment

The site is deployed on [Heroku](http://heroku.com/).

> To deploy the site, you'll need the Heroku Toolbelt: `brew install heroku-toolbelt`, an Heroku Account, and contributor access on the project.

You'll also need to do some configuration beforehand:

~~~sh
# First log in to Heroku.
heroku login
# Add the Heroku remote to the repository.
heroku git:remote -r heroku -a tekautoday
# Retrieve the deploy branch from GitHub.
git fetch --all
~~~

Then for each deploy:

~~~sh
# Switch to the deploy branch.
git checkout deploy
# Rebase it from master.
git rebase master
# Push it to GitHub.
git push origin deploy
# Then push the code to Heroku.
git push heroku deploy:master
~~~

### Other deployment configuration

Only when we set up the Heroku Dyno:

~~~sh
heroku config:add BUILDPACK_URL=git://github.com/heroku/heroku-buildpack-python.git
heroku ps:scale web=1
~~~
