# Docker MySQL, PhpMyadmin i Flask

Desplegament bàsic de MySQL amb PHPMyAdmin i Flask.

**Important!** MySQL per defecte s'ha configurat per a que sigui accessible fora de docker, amb la IP configurada. Comenta la línia del [docker-composen.yml](./docker-compose.yml) si no vols aquest comportament:

    - ${IP}:${MYSQL_PORT}:3306

## Configuració

Crea un fitxer `.env` amb els paràmetres de configuració. Pots fer servir el fitxer [.env.exemple](./.env.exemple).

## Flask

A la carpeta [./data/flask/flask-app/](./data/flask/flask-app/) hi ha l'aplicació flask de prova que es desplega.
