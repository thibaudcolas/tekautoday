[Tekau Today](http://www.tekautoday.xyz/) [![Travis](https://img.shields.io/travis/judsonsam/tekautoday.svg?style=flat-square)](https://travis-ci.org/judsonsam/tekautoday)
==========

> Ten Years Ago, Today
>
> Tekau Today is an experiment built on top of the [DigitalNZ API](http://digitalnz.org/developers).

- [Production site](http://www.tekautoday.xyz/)
- [Trello board](https://trello.com/b/ytZCXTVM/tekau-today)

Here are examples from the site:

- [07 May 2005](http://www.tekautoday.xyz/record/ddafdd0330ffb48b082d132a348648d2)
- [25 July 2005](http://www.tekautoday.xyz/record/8090b73800d9bb93beaf4a36f2a1f42a)
- [27 January 2005](http://www.tekautoday.xyz/record/bf117d33a0631e1beafa38c5b8ac5d35)

## Installation

> You first need to clone the project on your computer.

From the command-line:

```sh
cd ~/Development/sites/
git clone git@github.com:judsonsam/tekautoday.git
cd tekautoday
```

Our main dependencies are:

- [Python 3](https://www.python.org/) programming language.
- [Flask](http://flask.pocoo.org/) web framework.
- [virtualenv](https://virtualenv.pypa.io/en/latest/) and [pip](https://pypi.python.org/pypi/pip).
- [Node.js](nodejs.org) JavaScript runtime and the [npm](https://www.npmjs.com/) ecosystem.

> If you don't already have those installed, use `brew install python node`.

To install our dependencies, run:

```sh
pip install flake8 virtualenv
gem install scss_lint
# Create a Python 3 virtual environment with virtualenv.
virtualenv -p python3 env
# Then let's start it.
source env/bin/activate
# And install all our python dependencies.
pip install -r requirements.txt
# Then, install all npm dependencies.
npm install
# If that's your thing, install the git hooks:
./.githooks/deploy
```

## Working on the project

> Everything mentioned in the installation process should already be done.

~~~sh
# Always start by activating Python's virtualenv.
source env/bin/activate
# Export your DNZ API Key
export DNZ_KEY=<YOUR API KEY>
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
# Merge it with master.
git merge master
# Rebuild the project.
npm run build
# Commit the new build.
git add . && git commit -m 'Deploy latest version'
# Push it to GitHub, and Travis will pick it up.
git push origin deploy
# Alternatively, manual deploy
git push heroku deploy:master
~~~

### Other deployment configuration

Only when we set up the Heroku Dyno:

~~~sh
heroku config:add ENV=production
heroku config:add DNZ_KEY=<Production DNZ API KEY>
heroku config:add BUILDPACK_URL=git://github.com/heroku/heroku-buildpack-python.git
heroku config:add TZ="Pacific/Auckland"
heroku ps:scale web=1
~~~

To configure deployment from Travis:

~~~sh
travis setup heroku
~~~

## Scripts

Our `scripts/` rely on [pyDNZ](https://github.com/fogonwater/pydnz) to access the DNZ API. An [API key](http://www.digitalnz.org/developers) is also necessary.

```sh
export DNZ_KEY=<YOUR API KEY>
python scripts/fetch.py
```
