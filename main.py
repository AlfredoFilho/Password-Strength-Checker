import strawberry
from typing import List
from fastapi import FastAPI
from strawberry.asgi import GraphQL
# Local import
from rules_password import *

@strawberry.type
class Response:
    verify: bool
    noMatch: List[str]

@strawberry.input
class Rules:
    rule: str
    value: int

@strawberry.type
class Query:
    @strawberry.field
    def verify(self, password: str,  rules: List[Rules]) -> Response:
        
        # Relates the rules available in GraphQL with the name of the functions in rules_password.py
        dictFunctions = {
            "minSize": min_size,
            "minUppercase": min_upper_case,
            "minLowercase": min_lower_case,
            "minDigit": min_digit,
            "minSpecialChars": min_special_chars,
            "noRepeted": no_repeted,
        }
        
        # For each rule input in GraphQL, call the function and relate the name of the rule with the return to its function
        dictResponse = {}
        for ruleInput in rules:
            dictResponse[ruleInput.rule] = dictFunctions[ruleInput.rule](password, ruleInput.value)
            # Example: dictResponse["minSize"] = False (False it's return of min_size(string, value))
        
        if all(list(dictResponse.values())):
            # Returns empty "noMatch" attribute if all values in dictResponse are True
            return Response(verify=True, noMatch=[""])
        else:
            # Return the rules that did not pass in the "noMatch" attribute
            wrongChecks = [response for response in dictResponse if dictResponse[response] == False]
            return Response(verify=False, noMatch=wrongChecks)

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)