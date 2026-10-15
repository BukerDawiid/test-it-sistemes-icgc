# Visió general

Tria les eines que et siguin més còmodes per tal de solucionar aquests problemes. Les tasques estan dissenyades per testejar la teva habilitat de treballar amb dades i scripts, amb l’objectiu de mostrar les teves capacitats per entrar a l’equip tècnic de sistemes de l’ICGC.

# Exercici

La companyia proveïdora d'eines ACME Inc. realitza les seves operacions a través de tres fitxers CSV:

1. `customers.csv` conté la informació sobre els clients:
    * `id` número d'identificació del client
    * `firstname` el nom del client
    * `lastname` el cognom del client
2. `products.csv` conté la informació del producte:
    * `id` número d'identificació del producte
    * `name` nom del producte
    * `cost` cost del producte en euros
3. `orders.csv` conté la informació de les comandes:
    * `id` numero d'identificació de comanda
    * `customer` número d'identificació del client que ha fet la comanda
    * `products` llistat d'identificadors de producte separats per espais de la comanda

Gestionar manualment aquests fitxers és difícil i pot induir a errors humans. Ens han demanat si els podries ajudar a aportar una solució per facilitar-los la feina.

### Tasca 1

Actualment `orders.csv` no conté el total del cost de la comanda.

Necessitem utilitzar les dades d’aquests fitxers per generar el fitxer `order_prices.csv` amb les següents columnes:
* `id` número d'identificació de la comanda
* `euros` cost total en euros de la comanda

### Tasca 2

El departament de màrqueting vol saber quins clients tenen interès en cada producte. Ens han demanat el fitxer `product_customers.csv` que, per a cada producte, contingui un llistat dels clients que l’han comprat: 
* `id` número d'identificació del producte
* `customer_ids` llistat separat per espais amb els identificadors dels clients que han comprat el producte

### Tasca 3

Per tal d’avaluar els nostres clients, necessitem el fitxer `customer_ranking.csv`, que conté les següents columnes, ordenades de forma descendent pel camp `total_euros`:
* `id` número d'identificació del client
* `firstname` nom del client
* `lastname` cognom del client
* `total_euros` total en euros que aquest client ha gastat en productes

### Instruccions d'entrega

1. Fes un fork d'aquest repositori al teu compte de git (github, gitlab, o el que consideris).
2. Al teu fork, crea una branca nova a partir de `main` per implementar-hi la solució.
3. Quan hagis acabat, obre una pull request **dins del teu fork**, des de la branca amb la solució cap a `main`. Comprova que tant el repositori com les branques d'origen i de destinació siguin els del teu fork:

   ```mermaid
   flowchart LR
       subgraph Original["Repositori original"]
           OriginalMain["main"]
       end
       subgraph Fork["El teu fork"]
           ForkMain["main"]
           Solution["branca-amb-solucio<br/>La teva solució"]
       end
       OriginalMain -->|"Fork"| ForkMain
       ForkMain -->|"Crea una branca"| Solution
       Solution -->|"Pull request"| ForkMain
   ```

4. A la descripció de la pull request, explica breument la solució, les instruccions per executar-la i el raonament que has seguit.
5. Entregar l'enllaç de la pull request **dins del teu fork**.

Recordeu, aquest exercici es una carta de presentació per veure com treballeu. És important que puguem entendre i validar la solució.