import base64
import requests

# #印刷识别

# with open('words.jpg', 'rb') as r:
#     b64=base64.b64encode(r.read())
#     print(type(b64))
#     b64 = str(b64).split("'")[1]
# print(b64)
#
# data = {
# 'key':'9e8c3357db13860ec51e8127e9596203',
# 'ImageBase64' : b64
# }
#
# res = requests.post(url='http://v.juhe.cn/generalaccurateOcr/index.php' ,data=data )
# print(res.text)




#机票
with open('flight.jpg','rb') as r:
    b64=base64.b64encode(r.read())

    b64 = str(b64).split("'")[1]

data = {
    'key':'8c9fcd4c9f0c2717b178b50f96f242bd',
    'ImageBase64': b64
}

res = requests.post(url='http://v.juhe.cn/flightinvoiceOcr/index',data=data )
print(res.text)
exit(0)
import shelve
shelve.open





