# Task From Stepik

### Condition:
1. The test in the repository can be run with the command pytest --language = es, the test passes successfully.
2. Checking the functionality of the code for different languages. Add the command time.sleep (30) to the test file immediately after opening the link. Run the test with the --language = fr parameter and visually check that the phrase on the add to cart button looks like this: "Ajouter au panier".
3. The browser must be declared in the browser fixture and passed to the test as a parameter.
4. The test checks for the presence of the add to cart button. The button selector is unique to the page being checked. There is assert.
5. The name of the test method inside the test_items.py file corresponds to the task. The name test_something does not meet the requirements.

#### Executable commands:
```bash
pytest --language=fr test_items.py
```
```bash
pytest --language=eu test_items.py
```
```bash
pytest --language=ru test_items.py
```

#### Stack:
* Python 3.8+
* Selenium 3.14
* Pytest 5.1

#### Python requirements:
`requirements.txt`

Installation of requirements:
```bash
pip3 install -r requirements.txt
```

#### Developers:
Shkvalik
`valikko2004@gmail.com`
