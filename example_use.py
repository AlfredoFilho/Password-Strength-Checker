import json
import requests

url = "http://localhost:8000/graphql"
 
body = """
query {
    verify(password: "TestStrengthPassword!12&", rules: [
        {rule: "minSize", value: 10},
        {rule: "minUppercase", value: 5},
        {rule: "minLowercase", value: 3},
        {rule: "minDigit", value: 3},
        {rule: "minSpecialChars", value: 2},
        {rule: "noRepeted", value: 0},
    ]) {
        verify
        noMatch
    }
}
"""

print(body)
response = requests.post(url=url, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    parsed = json.loads(response.content)
    print("response : ", json.dumps(parsed, indent=4))

# response status code:  200
# response :  {
#     "data": {
#         "verify": {
#             "verify": false,
#             "noMatch": [
#                 "minUppercase",
#                 "minDigit",
#                 "noRepeted"
#             ]
#         }
#     }
# }
