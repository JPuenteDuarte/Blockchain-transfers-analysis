#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

def transaction_values_dict(file_trans):
    """ Esta función toma como argumento un archivo de transacciones y devuelve un diccionario
        con estructura {"txid" : value} compuesto por strings y floats respectivamente."""
    txid_list = []
    values_list = []
    with open('%s' % file_trans, 'r') as f:
        for line in f:
            txid = json.loads(line)["txid"]
            txid_list.append(txid)
            vout = json.loads(line)["vout"]
            values = [v["value"] for v in vout]
            values_list.append(sum(values))
    txid_vals = dict(zip(txid_list, values_list))
    return(txid_vals)

