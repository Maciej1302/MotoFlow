# Uruchamianie projektu MotoFlow

## Wymagania wstępne

### Zainstalowane narzędzia
Przed rozpoczęciem upewnij się, że masz zainstalowane:
- **Docker** w wersji co najmniej `20.10`. [Pobierz Docker](https://docs.docker.com/get-docker/).

### Utwórz plik `.env`
W katalogu głównym projektu utwórz plik `.env` i dodaj do niego następujące zmienne środowiskowe:

SECRET_KEY=your_secret_key_here  
POSTGRES_USER=your_postgres_user  
POSTGRES_PASSWORD=your_postgres_password  
POSTGRES_DB=your_postgres_db_name  
DEBUG=True # To ma tak zostać  

## Uruchamianie projektu na różnych systemach operacyjnych

### Na systemie Linux (przy użyciu Makefile)

1. W katalogu głównym projektu uruchom następujące polecenie, aby zbudować obrazy i uruchomić kontenery dla backendu, frontendu oraz bazy danych:  
`make build`

2. Następnie uruchom kontenery za pomocą polecenia:  
`make up`

> **Uwaga:** Jeżeli kontenery zostały wcześniej zbudowane i nie wprowadzono żadnych zmian w instalowanych bibliotekach, możesz pominąć krok `make build` i uruchomić od razu `make up`.

### Na systemie Windows (przy użyciu Docker Compose)

1. W katalogu głównym projektu uruchom następujące polecenie, aby zbudować obrazy i uruchomić kontenery:  
`docker compose build`

2. Po zbudowaniu kontenerów możesz je uruchomić za pomocą polecenia:  
`docker compose up`

> **Uwaga:** Jeżeli kontenery zostały wcześniej zbudowane i nie wprowadzono żadnych zmian w instalowanych bibliotekach, możesz pominąć krok `docker compose --build` i uruchomić od razu `docker compose up`.

### Na systemie Windows (przy użyciu Docker Compose) i Linux (Kiedys zrobie do tego komende w makefilu ale narazie mi sie nie chce)

3. W katalogu głównym projektu uruchom następujące polecenie (ale w oddzielnym terminalu), aby wykonac migracje bazy danych:  
`docker exec -it MotoFlow_backend python manage.py migrate`

### Jeżeli koniguracja zostanie poprawnie przeprowadzona w przeglądarce pod linkami:
`http://localhost:8000/myapp/` Pojawi się wiadomość "Hello from my new testapp its django here!" wyświetlana przez backend
`http://localhost:3000/` Pojawi się wiadomość "Hello from my new testapp its django here!" wysłana z backendu i wyświetlona przez frontend


