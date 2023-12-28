try:
    import requests
except ImportError:
    subprocess.check_call(['pip', 'install', 'requests'])
try:
    import colorama
except ImportError:
    subprocess.check_call(['pip', 'install', 'colorama'])

#inicia colorama
colorama.init()

GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET
def print_green(msg):
    print(f"{GREEN}{msg}{RESET}")

print_green ("       /$$$$$$$ /$$$$$$$  /$$$$$$ /$$   /$$/$$     /$$          ")
print_green ("      | $$__  $| $$__  $$/$$__  $| $$  / $|  $$   /$$/          ")
print_green ("      | $$__  $| $$__  $$/$$__  $| $$  / $|  $$   /$$/          ")
print_green ("      | $$  \ $| $$  \ $| $$  \ $|  $$/ $$/\  $$ /$$/           ")
print_green ("      | $$$$$$$| $$$$$$$| $$  | $$\  $$$$/  \  $$$$/            ")
print_green ("      | $$____/| $$__  $| $$  | $$ >$$  $$   \  $$/             ")
print_green ("      | $$     | $$  \ $| $$  | $$/$$/\  $$   | $$              ")
print_green ("      | $$     | $$  | $|  $$$$$$| $$  \ $$   | $$              ")
print_green ("      |__/     |__/  |__/\______/|__/  |__/   |__/              ")
print_green ("  /$$$$$$ /$$   /$$/$$$$$$$$ /$$$$$$ /$$   /$$/$$$$$$$$/$$$$$$$ ")
print_green (" /$$__  $| $$  | $| $$_____//$$__  $| $$  /$$| $$_____| $$__  $$")
print_green ("| $$  \__| $$  | $| $$     | $$  \__| $$ /$$/| $$     | $$  \ $$")
print_green ("| $$     | $$$$$$$| $$$$$  | $$     | $$$$$/ | $$$$$  | $$$$$$$/")
print_green ("| $$     | $$__  $| $$__/  | $$     | $$  $$ | $$__/  | $$__  $$")
print_green ("| $$    $| $$  | $| $$     | $$    $| $$\  $$| $$     | $$  \ $$")
print_green ("|  $$$$$$| $$  | $| $$$$$$$|  $$$$$$| $$ \  $| $$$$$$$| $$  | $$")
print_green (" \______/|__/  |__|________/\______/|__/  \__|________|__/  |__/")
print_green ("                                                                ")
print_green ("  _                 _                    ")
print_green (" | |               | |                   ")
print_green (" | |__  _   _    __| | ___ _ __ ___  ____")
print_green (" | '_ \| | | |  / _` |/ _ | '_ ` _ \|_  /")
print_green (" | |_) | |_| | | (_| |  __| | | | | |/ / ")
print_green (" |_.__/ \__, |  \__,_|\___|_| |_| |_/___|")
print_green ("         __/ |                           ")
print_green ("        |___/                            ")
print_green ("                                                                ")
print_green ("                                                                ")

try:
    while True:
        while True:  # Bucle infinito para continuar solicitando direcciones IP
            
            # Revisa el archivo api.txt buscando la apikey y la guarda en una variable
            with open('api.txt', 'r') as api:
                apikey = api.read()
            # Pide la IP por consola
            ip = input("\nIP: ")

            # URL de la API
            url = 'https://api.whatismyip.com/proxy.php'

            # Agrega la IP para chequear
            urlcheck = f'{url}?key={apikey}&input={ip}&output=json' 

            # Realiza una solicitud GET a la API
            response = requests.get(urlcheck)

            # Verifica si la solicitud fue exitosa (código de estado 200)
            if response.status_code == 200:
                # La respuesta de la API se encuentra en response.text o response.json() si es JSON
                data = response.json()  # Si la respuesta es JSON
                if data == 1 :
                    print ("Not a valid API key")
                    print (f'Error code: {data}')
                elif data == 3 :
                    print ("Too many lookups today")
                    print (f'Error code: {data}')
                else :
                    print (data)
            else:
                print(f'Error al hacer la solicitud: Codigo de estado {response.status_code}')

    pass
except KeyboardInterrupt:
    print("\n\nGoodbye")