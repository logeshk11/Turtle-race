import requests

pixel_endpoint="https://pixe.la/v1/users"
tok = "fcedh4hs3hs6"
usr_name ="logesh202"

user_prams = {
    "token": "fcedh4hs3hs6",
    "username": "logesh202",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#response= requests.post(url=pixel_endpoint, json=user_prams)

graph_endpoint=f"{pixel_endpoint}/{usr_name}/graphs"
graph_para={
    "id": "example1",
    "name":"cycling",
    "unit":"km",
    "type":"float",
    "color": "sora"
}

headers={
    "X-USER-TOKEN": tok
}
#res= requests.post(url=graph_endpoint, json=graph_para, headers= headers)
#res.raise_for_status()

pixel_endpoint = f"{graph_endpoint}/example1"
pixel_para={
    "date":"20230325",
    "quantity": 8
}
pixel= requests.post(url=pixel_endpoint, json=pixel_para, headers=headers)
