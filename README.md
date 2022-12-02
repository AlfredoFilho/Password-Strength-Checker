# Password Strength Checker
A FastAPI with GraphQL (Strawberry) to check strength of passwords
## Example
##### Query input
```graphql
query {
    verify(password: "TestStrengthPassword!123&", rules: [
        {rule: "minSize", value: 10},
        {rule: "minUppercase", value: 5},
        {rule: "minLowercase", value: 3},
        {rule: "minDigit", value: 2},
        {rule: "minSpecialChars", value: 2},
        {rule: "noRepeted", value: 0},
    ]) {
        verify
        noMatch
    }
}
```
##### Output
```json
{
  "data": {
    "verify": {
      "verify": false,
      "noMatch": [
        "minUppercase",
        "minDigit",
        "noRepeted"
      ]
    }
  }
}
```
## Dependencies
- Python 3

##How to use:
#####Install requirements
```bash
pip install -r requirements.txt
```
##### Run API
```bash
uvicorn main:app --reload --port 8000
```
##### Run Tests
```bash
python -m unittest test_rules_password.py
```
- Go to http://localhost:8000/graphql in a browser you will be able to insert queries and execute them

or

- Make a POST request with the desired Query to http://localhost:8000/graphql
###### In the [example_use.py](/example_use.py) file there is an example of a POST request in python
```bash
python example_use.py
```