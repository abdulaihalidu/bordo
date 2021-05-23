# https://ip-api.com/ servisinin sağladığı ücretsiz API’ı kullanarak kullanıcının girmiş olduğu ip
# adresinin latitude, longitude ve country bilgilerini ekranda gösteren bir program yazmqk

import requests


def get_info():
    user_ip_address = input("ip adresiniz giriniz: ")   # get user up address
    response = requests.get(f"http://ip-api.com/json/{user_ip_address}").json()     # append ip address to link
    lat = response['lat']
    lon = response['lon']
    country = response['country']
    print(f"\nip:\t\t\t{user_ip_address}"
          f"\nlatitude:\t{lat}"
          f"\nlongitude:\t{lon}"
          f"\ncountry:\t{country}")


#  driver program
if __name__ == "__main__":
    get_info()
