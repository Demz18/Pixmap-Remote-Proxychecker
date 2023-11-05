import requests

# Revisa el archivo api.txt buscando la apikey y la guarda en una variable
with open('api.txt', 'r') as api:
    apikey = api.read()
try:
    while True:
        while True:  # Bucle infinito para continuar solicitando direcciones IP
            # Pide la IP por consola
            ip = input("IP: ")

            # URL de la API que deseas llamar
            url = 'https://api.whatismyip.com/proxy.php'

            # Agrega la IP para chequear
            urlcheck = f'{url}?key={apikey}&input={ip}&output=json' 

            # Realiza una solicitud GET a la API
            response = requests.get(urlcheck)

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # La respuesta de la API se encuentra en response.text o response.json() si es JSON
                data = response.json()  # Si la respuesta es JSON
                print(data)
            else:
                print(f'Error al hacer la solicitud: Codigo de estado {response.status_code}')

        #    continuar = input("Do you want to continue checking ips? (Yes/No): ")
        #    if continuar == 'no' or 'n':
        #       break  # Sale del bucle si la respuesta no es "si" (puedes personalizar según tus necesidades)
    pass
except KeyboardInterrupt:
    print("\n\nGoodbye")