JSON logging for Python |PyPi version|
======================================

This library provides Python logging formatters to output JSON, 2
formatters are specific for Logstash message format version 0 or 1.

Installation
============

Using pip:

::

    pip install json-logging-py

From source:

::

    python setup.py install

Usage
=====

The name of the library is ``jsonlogging``, it provides 3 formatters:

JSONFormatter
-------------

::

    {
        "tags": [
            "env=prod",
            "role=www"
        ],
        "timestamp": "2015-09-22T22:40:56.178715Z",
        "level": "ERROR",
        "host": "server-01.example.com",
        "path": "example.py",
        "message": "hello world!",
        "logger": "root"
    }

LogstashFormatterV0
-------------------

::

    {
        "@source": "JSON://server-01.example.com/example.py",
        "@source_host": "server-01.example.com",
        "@message": "hello world!",
        "@tags": [
            "env=prod",
            "role=www"
        ],
        "@fields": {
            "logger": "root",
            "levelname": "ERROR"
        },
        "@timestamp": "2015-09-22T22:42:02.094525Z",
        "@source_path": "example.py",
        "@type": "JSON"
    }

LogstashFormatterV1
-------------------

::

    {
        "host": "server-01.example.com",
        "logger": "root",
        "type": "JSON",
        "tags": [
            "env=prod",
            "role=www"
        ],
        "path": "example.py",
        "@timestamp": "2015-09-22T22:43:11.966558Z",
        "@version": 1,
        "message": "hello world!",
        "levelname": "ERROR"
    }

Python example
--------------

::

    import logging
    import jsonlogging


    logger = logging.getLogger()

    logHandler = logging.StreamHandler()

    # You can also use LogstashFormatterV0 or LogstashFormatterV1
    formatter = jsonlogging.JSONFormatter(
        hostname="server-01.example.com"
        tags=["env=prod", "role=www"],
        indent=4)
    logHandler.setFormatter(formatter)

    logger.addHandler(logHandler)

    # You can pass additional tags
    logger.error('hello world!', extra={"tags": ["hello=world"]})

.. |PyPi version| image:: https://img.shields.io/pypi/v/json-logging-py.svg
   :target: https://pypi.python.org/pypi/json-logging-py/
