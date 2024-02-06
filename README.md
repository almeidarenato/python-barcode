# python-barcode
Barcode create and manager with python and flask


# Installation 

pip3 install -r requirements.txt

# Using Virtual Env

Windows:
```bash
.venv/Script/activate
```
Mac/ Unix
```bash
. .venv/bin/activate
```
- Transfer libs from venv to requirements.txt
```bash
.venv/bin/pip3 freeze > requirements.txt
```


# Installing pylint
- Install Pylint lib
- Install the pylint extension
 https://marketplace.visualstudio.com/items?itemName=ms-python.pylint
 - Run the command:

```bash
pylint --generate-rcfile > .pylintrc
```

# Pre-commit instalattion
- Install pre-commit lib
- Create config file .pylintrc
- Install the pre-commit with:
```bash
    pre-commit install
```


# BarCode Example

![BarCode](./example.png)