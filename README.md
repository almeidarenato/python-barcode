# python-barcode
API to generate  Barcodes in Python using Flask framework. 


<img src="./post-create_tag.png" alt="drawing" width="100"/>

This endpoint is used to create a new tag (barcode). 

The **HTTP** **POST** request should be sent to [http://127.0.0.1:3000/create_tag](http://127.0.0.1:3000/create_tag) with a raw request body containing the product code.

### Request Body

- product_code (string, required): The code of the product for which the tag is being created.


```json
{
    "product_code": "1576-456-789"
}
```
    
### Response


```json
{
    "data": {
        "count": 1,
        "path": "1576-456-789.png",
        "type": "Tag Image"
    }
}
```


# Installation 

```bash
pip3 install -r requirements.txt
```

# Running 
In the local folder , execute the following command on the terminal:
```bash
python3 run.py
```
it will launch a development server on http://127.0.0.1:3000


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

# Pre-commit installation
- Install pre-commit lib
- Create config file .pylintrc
- Install the pre-commit with:
```bash
    pre-commit install
```


# BarCode Example

![BarCode](./example.png)

# Libs 
- Cerberus
- Flask 
- PyTest
- Virtual Env
