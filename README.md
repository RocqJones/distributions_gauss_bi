[![CircleCI](https://circleci.com/gh/google/pybadges.svg?style=svg)](https://circleci.com/gh/google/pybadges)
![pypi](https://img.shields.io/pypi/v/pybadges.svg)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
![pip installation](tests/golden-images/build-passing.svg)

# distributions_gauss_bi

**distributions_gauss_bi** is a Python module/package for [Machine Learning](https://expertsystem.com/machine-learning-definition/) and [Data Science](https://en.wikipedia.org/wiki/Data_science) built for Gaussian and Binomial distributions. This package is distributed under the [MIT License](https://opensource.org/licenses/MIT).

* The project was started on 27-05-2020 by [Jones Mbindyo](https://jonesmbindyo.herokuapp.com/).

## Installation.
To install simply run(Commandline);
```
pip install distributions-gauss-bi
```
or 
```
conda install distributions-gauss-bi
```

PyPI link: https://pypi.org/project/distributions-gauss-bi/

## Testing.
For this test version of the package I would recommend running it on a [Virtual Environment](https://docs.python-guide.org/dev/virtualenvs/)
```
pip install -i https://test.pypi.org/simple/ distributions-gauss-bi
```

TestPyPI link: https://test.pypi.org/project/distributions-gauss-bi/

### Sample python test code.
On your commandline or favorite editor run below python code after installation.
```
>>> from distributions_gauss_bi import Gaussian, Binomial
>>> Gaussian(38,17)
>>> Binomial(0.4, 35)
```

## Development.
* I welcome new contributors of all experience levels. The goals of this package is to be helpful, welcoming, and effective.
* You'll note that I'm using [Unit Testing](https://docs.python.org/3/library/unittest.html) in each phase(1 to 4) of development to track bugs. To contribute follow programming code testing best practices.

## Contibution.
There are many ways to contribute to distributions_gauss_bi, with the most common ones being contribution of code or documentation to the project. Improving the documentation is no less important than improving the module itself. If you find a typo in the documentation or have made improvements on pseudocode or source code, do not hesitate to submit a GitHub pull request.
* **NOTE** Before reviewing the code I would encourage you go through the [pseudocode](https://github.com/RocqJones/distributions_gauss_bi/pseudocode.txt)

## Important links.
* **Pseudocode:** https://github.com/RocqJones/distributions_gauss_bi/pseudocode.txt
* **PyPI:** https://pypi.org/project/distributions-gauss-bi/
* **Test-PyPI:** https://test.pypi.org/project/distributions-gauss-bi/

## Gaussian and Binomial distribution overview
### 1. Gaussian distribution (also known as Normal distribution) 
- In probability theory, a normal distribution is a type of continuous probability distribution for a real-valued random variable. The general form of its probability density function is The parameter is the mean or expectation of the distribution; and is its standard deviation.
- The general form of its probability density function is:
<a href="url"><img src="https://github.com/RocqJones/distributions_gauss_bi/blob/master/imgs/gaussian1.png" height="50" width="90%" ></a>
<a href="url"><img src="https://github.com/RocqJones/distributions_gauss_bi/blob/master/imgs/gaussian2.png" height="50" width="90%" ></a>

#### Further Resources.
If you would like to review the Gaussian (normal) distribution and binomial distribution, here are a few resources:
* [Gaussian Distributions Wikipedia](https://en.wikipedia.org/wiki/Normal_distribution)
<a href="url"><img src="https://github.com/RocqJones/distributions_gauss_bi/blob/master/imgs/Normal_Distribution.png" height="50" width="50%" ></a>
* [](https://en.wikipedia.org/wiki/Binomial_distribution)
<a href="url"><img src="https://github.com/RocqJones/distributions_gauss_bi/blob/master/imgs/Binomial_distribution.png" height="50" width="50%" ></a>

#### Dunder or magic methods in Python. 
Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator overloading. eg ``__init__``

For instance if you want to add two Gaussian distributions to create another object of a third Gaussian distribution; 
* This is what I mean: ```gauss_a + gauss_b = gauss_c```
<a href="url"><img src="https://github.com/RocqJones/distributions_gauss_bi/blob/master/imgs/gauss_distribution.png" height="150" width="100%" ></a>

### 2. Binomial distribution.
- In probability theory and statistics, the binomial distribution with parameters n and p is the discrete probability distribution of the number of successes in a sequence of n independent experiments, each asking a yes–no question, and each with its own boolean-valued outcome: success/yes/true/one (with probability p) or failure/no/false/zero (with probability q = 1 − p).
<a href="url"><img src="https://github.com/RocqJones/distributions_gauss_bi/blob/master/imgs/Binomial_distribution_1.png" height="150" width="100%" ></a>
<a href="url"><img src="https://github.com/RocqJones/distributions_gauss_bi/blob/master/imgs/Binomial_distribution_2.png" height="150" width="100%" ></a>
