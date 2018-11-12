import http.client, urllib.parse, json, time

# Represents the various elements used to create HTTP request URIs
# for QnA Maker operations.
# From Publish Page: HOST
# Example: https://YOUR-RESOURCE-NAME.azurewebsites.net/qnamaker
host = "https://YOUR-RESOURCE-NAME.azurewebsites.net/qnamaker";

# Authorization endpoint key
# From Publish Page
endpoint_key = "YOUR-ENDPOINT-KEY";

# Management APIs postpend the version to the route
# From Publish Page, value after POST
# Example: /knowledgebases/ZZZ15f8c-d01b-4698-a2de-85b0dbf3358c/generateAnswer
route = "/knowledgebases/YOUR-KNOWLEDGE-BASE-ID/generateAnswer";

# JSON format for passing question to service
question = "{'question': 'Is the QnA Maker Service free?','top': 3}";

# Convert the request to a string.
content = json.dumps(question)

headers = {
  'Authorization': 'EndpointKey ' + endpoint_key,
  'Content-Type': 'application/json',
  'Content-Length': len (content)
}

conn = http.client.HTTPSConnection(host)

conn.request ("POST", route, content, headers)

response = conn.getresponse ()

answer = response.read ()

json.dumps(json.loads(answer), indent=4)
