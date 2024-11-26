#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def read_file(file):
    """Esta función toma como argumento la ruta a un archivo json y lo transforma 
        devolviendo una lista de diccionarios"""
    with open('%s' % file, 'r') as f:
        table = [json.loads(line) for line in f]
        return table

