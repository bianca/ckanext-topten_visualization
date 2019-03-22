.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/bianca/ckanext-topten_visualization.svg?branch=master
    :target: https://travis-ci.org/bianca/ckanext-topten_visualization

.. image:: https://coveralls.io/repos/bianca/ckanext-topten_visualization/badge.svg
  :target: https://coveralls.io/r/bianca/ckanext-topten_visualization

.. image:: https://pypip.in/download/ckanext-topten_visualization/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-topten_visualization/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-topten_visualization/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-topten_visualization/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-topten_visualization/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-topten_visualization/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-topten_visualization/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-topten_visualization/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-topten_visualization/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-topten_visualization/
    :alt: License

=============
ckanext-topten_visualization
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

This works with CKAN 2.7-2.8


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-topten_visualization:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-topten_visualization Python package into your virtual environment::

     pip install ckanext-topten_visualization

3. Add ``topten_visualization`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload

------------------------
Development Installation
------------------------

To install ckanext-topten_visualization for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/bianca/ckanext-topten_visualization.git
    cd ckanext-topten_visualization
    python setup.py develop
    pip install -r dev-requirements.txt
