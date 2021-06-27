import requests



#https://apihistorical.finlogix.com/v1/getMarketData/19?resolution=D1&size=3000&sid=1
#data = {"resolution=D1&size=3000&sid=1"}

#response = requests.get("https://apihistorical.finlogix.com/v1/getMarketData/19",data)
for i in range(1,100):
    response = requests.get("https://apihistorical.finlogix.com/v1/getMarketData/"+str(i)+"?resolution=D1&size=3000&sid=1")
    print(i)
    print(response.status_code)
    print(response.json())

# print(response.text)
#
# print(response.content)

