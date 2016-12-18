import httplib
import json
from Consistenthashing import ConsistentHashRing
Ch_obj = ConsistentHashRing()



Ch_obj.__setitem__("server1","5001")
Ch_obj.__setitem__("server2","5002")
Ch_obj.__setitem__("server3","5003")

for i in xrange(1,11):
    port = Ch_obj.__getitem__(str(i))
    url = "localhost:" + str(port)
    print url
    connection = httplib.HTTPConnection(url)

    headers = {'Content-type': 'application/json'}

    foo = {
    "id": i,
    "category": "training",
    "description": "iPhone for training",
    "email": "foo1@bar.com",
    "estimated_costs": "6760",
    "link": "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "name": "Foo Bar",
    "submit_date": "09-08-2016"
    }
    json_foo = json.dumps(foo)
    url2 = "/v1/expenses"
    print url2
    connection.request('POST', url2, json_foo, headers)
    response = connection.getresponse()
    print(response.read().decode())

for i in xrange(0,10):
    port = Ch_obj.__getitem__(str(i))
    url = "localhost:" + str(port)
    print url
    connection = httplib.HTTPConnection(url)

    url2 = "/v1/expenses/" + str(i) 
    print url2
    connection.request('GET', url2)
    response = connection.getresponse()
    print(response.read().decode())