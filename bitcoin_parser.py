import json
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


def read_file(file):
    """
    Takes as an argument the json path and
    transforms it by returning a list of dicts
    """
    with open('%s' % file, 'r') as f:
        table = [json.loads(line) for line in f]
        return (table)


def count_transacions(file_blocks):
    """
    Takes a blocks file and counts the number of transactions per block
    and represents them graphically. The function read_file() is required.
    """
    table = read_file(file_blocks)
    s = []
    for i in range(len(table)):
        s.append(len(table[i]["tx"]))
    plot = plt.bar([i for i in range(len(s))], s, color = "darkblue")
    
    plt.ylabel('Number of transactions')
    plt.xlabel('Block number')
    plt.title('Transactions per block')
    return(plot)


def transaction_values_dict(file_trans):
    """
    Takes as an argument a transactions file and returns a dictionary with
    a structure like {"txid" : value} containng strings and floats respectively.
    """
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
    
    
def value_block(file_blocks, file_trans):
    """
    Takes a blocks file and a transactions file. Groups in a list the transactions
    of each block and from each one calculates the total value of the transactions
    per each block and returns the result in a plot. The functions read_file() y 
    transaction_values_dict() are required.
    """
    table = read_file(file_blocks)
    bloques_transacciones = []
    for i in table:
        a = [transaccion for transaccion in i["tx"]]
        bloques_transacciones.append(a)
    diccionario_transacciones = transaction_values_dict(file_trans)
    lista_valores = []
    for b in bloques_transacciones:
        b_valor = 0
        for t in b:
            b_valor = b_valor + diccionario_transacciones.get(t)
        lista_valores.append(b_valor)
    plot = plt.bar([i for i in range(len(lista_valores))], lista_valores, color='darkgreen')
    plt.ylabel('Transactions value')
    plt.xlabel('Block number')
    plt.title('Value of the transactions on each block')
    return(plot)


def dates_blocks(file_blocks):
    """
    Takes a blocks file and returns a list with each block's date
    """
    bloques = read_file(file_blocks)
    lista_fechas = []
    for b in bloques:
        bloque_fecha = datetime.fromtimestamp(int(b["time"]))
        lista_fechas.append(bloque_fecha)
    return(lista_fechas)


def timedelta_bloques(file_blocks):
    """
    Takes a blocks file and returns a plot with the time difference between
    the blocks. The function dates_blocks() is required.
    """
    lista_fechas = dates_blocks(file_blocks)
    lista_deltas=[]
    for i in range(len(lista_fechas)-1):
        a = lista_fechas[i] - lista_fechas[i+1]
        lista_deltas.append(a.seconds)
    plt.xlabel('Block number')
    plt.ylabel('seconds')
    plt.title('Time intervals between blocks')
    plot = plt.bar([i for i in range(len(lista_deltas))], lista_deltas, color='firebrick')
    return(plot)


def avg_size_block(file_blocks):
    """
    Takes a blocks file and returns the average of the blocks size per hour. The
    function read_file() is required.
    """
    table = read_file(file_blocks)
    timestamps_days = []
    timestamps_hours = []
    sizes = []
    for i in range(len(table)):
        timestamp = table[i]["time"]
        timestamps_days.append(datetime.fromtimestamp(int(table[i]["time"])).day)
        timestamps_hours.append(datetime.fromtimestamp(int(table[i]["time"])).hour)
        size = table[i]["size"]
        sizes.append(size)
    hours_studied = []
    for i in range(len(timestamps_days)):
        hour_studied = ("day:"+str(timestamps_days[i])+" "+"hour:"+str(timestamps_hours[i]))
        hours_studied.append(hour_studied)
    import pandas as pd
    df=pd.DataFrame(sizes,columns=["tamaño"],index=hours_studied)
    df_agrupado = df.groupby(df.index).mean()
    plt.xticks(rotation=90)
    plt.xlabel('Hour')
    plt.ylabel('Size')
    plt.title('Average block size per hour')
    plot = plt.bar(df_agrupado.index, df_agrupado["tamaño"],  color='red')
    return(plot)


def count_tr_block(file_blocks):
    """
    Takes a blocks file and returns a plot with the number of transactions
    per hour.
    """
    table = read_file(file_blocks)
    timestamps_days = []
    timestamps_hours = []
    sizes = []
    for i in range(len(table)):
        timestamp = table[i]["time"]
        timestamps_days.append(datetime.fromtimestamp(int(table[i]["time"])).day)
        timestamps_hours.append(datetime.fromtimestamp(int(table[i]["time"])).hour)
        size = len(table[i]["tx"])
        sizes.append(size)
    hours_studied = []
    for i in range(len(timestamps_days)):
        hour_studied = ("day:"+str(timestamps_days[i])+" "+"hour:"+str(timestamps_hours[i]))
        hours_studied.append(hour_studied)
    import pandas as pd
    df=pd.DataFrame(sizes,columns=["tamaño"],index=hours_studied)
    df_agrupado = df.groupby(df.index).sum()
    plt.xticks(rotation=90)
    plt.xlabel('Hour')
    plt.ylabel('Transactions')
    plt.title('Number of transactions per hour')
    plot = plt.bar(df_agrupado.index, df_agrupado["tamaño"],   color='navy')
    return(plot)