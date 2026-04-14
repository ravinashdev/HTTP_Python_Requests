PIXELA_CREATE_USER={
    "url":"https://pixe.la/v1/users",
    "params":{},
    "payload":{
        "token": "qwertyuiop[]",
        "username": "ravinash",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"},
    "headers":{}
}

PIXELA_CREATE_GRAPH={
    "url":"https://pixe.la/v1/users/ravinash/graphs",
    "params":{},
    "payload":{
        "id": "first-graph",
        "name": "First_Graph",
        "unit": "hits",
        "type": "int",
        "color": "momiji"
    },
    "headers":{
        "X-USER-TOKEN":"qwertyuiop[]"
    }
}

PIXELA_MARK_GRAPH={
    "url":"https://pixe.la/v1/users/ravinash/graphs/first-graph",
    "params":{},
    "payload":{
        "date": "20260413",
        "quantity": "5"
    },
    "headers": {
        "X-USER-TOKEN": "qwertyuiop[]"
    }
}