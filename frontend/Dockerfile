# Użycie obrazu Node.js jako bazowego
FROM node:18
ENV PATH /app/node_modules/.bin:$PATH
# Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# Skopiowanie plików package.json i package-lock.json
COPY package*.json .

# Instalacja zależności
RUN npm install
RUN npm install --save-dev @babel/plugin-proposal-private-property-in-object

# Skopiowanie całej aplikacji do katalogu roboczego
COPY . /app


# Eksponowanie portu 3000 (domyślny port dla serwera deweloperskiego Reacta)
EXPOSE 3000

