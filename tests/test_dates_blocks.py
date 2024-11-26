#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
from datetime import datetime

def dates_blocks(file_blocks):
    """ Esta función toma como argumento un archivo de bloques y devuelve un listado con las fechas
        de cada bloque."""
    bloques = read_file(file_blocks)
    lista_fechas = []
    for b in bloques:
        bloque_fecha = datetime.fromtimestamp(int(b["time"]))
        lista_fechas.append(bloque_fecha)
    return(lista_fechas)

