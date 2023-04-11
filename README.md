# PyComm

Este programa permite realizar el envío y recepción de mensajes de texto a través de una red, los mensajes están codificados/decodificados con un algoritmo propio.

## Preparación

> Esta sección es par aisntalar venv en el sistema y tener un entorno de ejecucion común. Si no lo necesita o no lo usará puede saltarse a la siguiente sección.

### Creación de Virtual Enviroment

Al instalar python3 en el sistema, este incluye la opción de crear venvs, que son entornos de ejecución de códigos aislados, por lo que no interfieren con todo el computador o servidor donde se hospedan.

Crearemos un entorno virtual llamado `venv`:

```shell
python3 -m venv venv
```

Ahora podemos ejecutarlo con el siguiente comando desde la carpeta raíz del programa:

```shell
source venv/bin/activate
```

### Instalación de requerimientos

Con el Virtual Enviroment activado, instalamos los paquetes requeridos dentro del `requirement.txt` con el siguiente comando:

```shell
pip install -r requirements.txt
```

Con esto tenemos todo listo para ejecutar el programa!

## Como ejecutar

1. Se deben abrir dos terminales para ejecutar el `Server.py` y `Client.py` en un mismo pc.
2. En ambas terminales ejecutar el ambiente con `source venv/bin/activate`
3. En la primera ejecutar `Server.py` con python utilizando el siguiente comando:

```shell
python3 server.py
```

4. En la segunda terminal ejecutar `Client.py` con python utilizando el siguiente comando:

```shell
python3 client.py
```

5. Ahora se puede mandar mensajes desde cliente a servidor y viceversa, pero siempre comienza el cliente!

## Consideraciones

1. La conversación y envío de mensajes siempre la comienza el cliente.
2. Siempre ejecutar primero el `server.py` y luego el `client.py` para no tener errores.
3. En caso de realizar la conexión entre dos pcs distintos, ambos deben estar en la misma red conectados y cambiar en ambos archivos la variable `HOST`a la ip donde se ejecutará el servidor.
4. En caso de tener un error por una carpeta `logs`, se debe crear de manera manual una carpeta vacía con dicho nombre en el directorio raíz del proyecto.

# Como contribuir

Para contribuir en el código se puede realizar un fork del git actual, y luego hacer un pull request que será revisado por los dueños del Git actual.

# Licencia

Para ver las licencia GNU-3 haga click [aqui](https://github.com/PyComm/PyComm/blob/main/LICENSE)
