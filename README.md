# PyComm

Este programa permite realizar el envío y recepción de mensajes de texto a través de una red, los mensajes están codificados/decodificados con un algoritmo propio.

## Antes de usar, se debe instalar la siguiente librería utilizando.
```
pip install unidecode
```
O
```
pip3 install unidecode
````

## Como usar

> Se recomienda utilizar virtual envs para su ejecución, por lo que esta guía los incluirá

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
