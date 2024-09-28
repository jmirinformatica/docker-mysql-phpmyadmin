# Docker MySQL PhpMyadmin

Desplegament bàsic de MySQL amb PHPMyAdmin.

**Important!** MySQL per defecte s'ha configurat per a que sigui accessible fora de docker, amb la IP configurada. Comenta la línia del [docker-composen.yml](./docker-compose.yml) si no vols aquest comportament:

    - ${IP}:${MYSQL_PORT}:3306

## Configuració

Crea un fitxer `.env` amb els paràmetres de configuració. Pots fer servir el fitxer [.env.exemple](./.env.exemple).
