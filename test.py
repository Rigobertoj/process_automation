import requests
URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43783/datos/oportuno?token=9692a09b038f044e2980f9895de684d4b6958787fe6ef49ee85d5257005866d1"
TOKEN = "9692a09b038f044e2980f9895de684d4b6958787fe6ef49ee85d5257005866d1"
def getTiie():
    response = requests.get(URL, {
        "headers": {

        }
    })
    print(response)

getTiie()
