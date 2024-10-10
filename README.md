# Docker MySQL & PostgreSQL

Desplegament bàsic de MySQL i PostgreSQL amb [AdminerEvo](https://docs.adminerevo.org/).

**Important!** Tant PostgreSQL com MySQL estan configurats per defectet per a que siguin accessibles fora de docker, amb la IP configurada. Revisa el fitxer [docker-compose.yml](./docker-compose.yml) si no vols aquest comportament.

## Flask

A la carpeta [./data/flask/flask_app_to_deploy/](./data/flask/flask_app_to_deploy/) hi ha l'aplicació flask de prova que es desplega. L'aplicació flask de prova que hi ha també necessita un fitxer `.env` propi de configuració.

## Configuració

Crea un fitxer `.env` amb els paràmetres de configuració. Pots fer servir el fitxer [.env.exemple](./.env.exemple). A continuació executa:

    docker compose up -d
