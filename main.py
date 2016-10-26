from porc import Client
import utils, time
from agency import Agency

client = Client("293bdf31-c0f2-48a5-8d81-02b72c5a7de7")
agency = Agency("rutgers")

relevantTags = ['a','b','f','lx']

relevantRoutes = []
for relevantTag in relevantTags:
    route = agency.getRoute(relevantTag)
    if route != None:
        relevantRoutes.append(route)

while True:
    print("start")
    predictions = []
    for route in relevantRoutes:
        predictions = predictions + route.getPredictions()

    # asynchronously post items
    with client.async() as c:
        futures = [c.post('predictions', prediction) for prediction in predictions]
        responses = [future.result() for future in futures]
        [response.raise_for_status() for response in responses]
    print("end")
    time.sleep(10)
