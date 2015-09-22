from setuptools import setup


with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='json-logging-py',
    version='0.2',
    description='JSON / Logstash formatters for Python logging',
    long_description=readme,
    keywords=['json', 'logging', 'logstash'],
    author='Sebastien Estienne',
    author_email='rs@dailymotion.com',
    url='https://github.com/sebest/json-logging-py',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    py_modules=['jsonlogging'],
)
