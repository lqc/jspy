jspy - JavaScript interpreter in Python
=========================================

*jspy* is a toy JavaScript interpreter in Python created by Marek Stepniowski. Its implementation is directly based on [ECMA-262 standard (PDF)](http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf).


Installing
------------

You'll need setuptools or distribute for installation. Then you can just run:

    $ python setup.py install

You may need to have root rights, depending on your system configuration. 


Usage
-------

After the installation, `jspy` script should be on your path. You can then just run the script with the JavaScript file as a single argument:

    $ jspy file.js


Test suite
----------

To run the test suite, you either need Python 2.7 or the [unittest2](http://pypi.python.org/pypi/unittest2) package installed. 
Thankfully, setuptools will handle it for you, so you can just run:

    $ python setup.py test

Source code
-----------

You can find the newest source code of *jspy* on [GitHub](https://github.com/zuber/jspy).


Implemented features
--------------------

  * Expressions (excluding `delete`, `typeof`, `instanceof` and `in` operators)
  * Statements (excluding `for` and `for in` loops, `with`, `switch`, labels and exception handling)
  * Functions (with nested execution scopes allowing for closures)
  * Basic object support (`Object` and `Array` literals, item assignment)
  * `console.log`, same as in [Node.js](http://nodejs.org/) and [Firebug](http://getfirebug.com/)


Todo (in order of priorities)
-----------------------------

  * `for` and `for in` loops
  * `switch` statement
  * Full object support (including an `Array` implementation)
  * `delete`, `typeof`, `instanceof` and `in` operators
  * Function statements
  * Sane error messages
  * Prototypal inheritance
  * Exception handling
  * Strict mode (should we run in strict mode by default?)
  * Proper value behaviour (right now the behaviour of `Number` and `String` objects is Python-like and can sometimes be different than in JavaScript)
  * Automatic semicolon insertion (as defined in section 7.9 of ECMA-262)
  * Labels for `break` and `continue` statements
  * `with` statement (it's [evil](http://yuiblog.com/blog/2006/04/11/with-statement-considered-harmful/)!)

