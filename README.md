[![Python](https://img.shields.io/pypi/pyversions/relevantpackage)](https://img.shields.io/pypi/pyversions/relevantpackage)
[![Pypi](https://img.shields.io/pypi/v/relevantpackage)](https://pypi.org/project/relevantpackage/)
[![LOC](https://sloc.xyz/github/erdogant/relevantpackage/?category=code)](https://github.com/erdogant/relevantpackage/)
[![Downloads](https://static.pepy.tech/personalized-badge/relevantpackage?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/relevantpackage)
[![Downloads](https://static.pepy.tech/personalized-badge/relevantpackage?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/relevantpackage)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/relevantpackage/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/relevantpackage.svg)](https://github.com/erdogant/relevantpackage/network)
[![Issues](https://img.shields.io/github/issues/erdogant/relevantpackage.svg)](https://github.com/erdogant/relevantpackage/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)

---------

### Install relevantpackagefrom PyPi.
bash
pip validator_and_token_generator

# Import library
from validator_and_token_generator import validator_and_token_generator
# Initialize
initialize = validator_and_token_generator(message='Validator and Token Generator is running')
# Run the model
intialize.show()

# validator_and_token_generator is a package created for a class project to validate certain strings such as credit/debit card numbers, and generate alphanumeric tokens.

Example
-------
>>> # Import library
>>> import validator_and_token_generator
>>> # Generate token
>>> _token = validator_and_token_generator.token_generator(length=10)
