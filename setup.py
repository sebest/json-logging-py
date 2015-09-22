from setuptools import setup

setup(
    name='json-logging-py',
    version='0.1',
    description='',
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
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
)
