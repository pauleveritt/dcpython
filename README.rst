dcpython
========

Pyramid tutorial sources for my DCPython presentation Feb 2013

This tutorial walkthrough is targeted at Python 3.3. The steps I used
to get my virtualenv setup::

  $ pyvenv-3.3 env33
  $ env33/bin/python3.3 distribute_setup.py
  $ env33/bin/easy_install-3.3 pip
  $ env33/bin/pip-3.3 install pyramid
  ....chuggalugga...
  $ source env33/bin/activate
  $ python3.3 01-helloworld/helloworld.py

Each of the directories in this repo (except the first one,
01-helloworld) is a Python package. To successfully run each step::

  $ cd 02-hellopackage
  $ python3.3 ./setup.py develop

...and repeat for each step you would like to work on.

Notes
=====

- 04-hellotests requires::

  $ pip install nose WebTest

- 08-helloforms requires::

  $ pip install