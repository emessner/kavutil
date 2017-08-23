import collections
import pandas as pd
import numpy as np
# import spss, spssdata wird erst relevanter Funktion importiert, da dieses Paket nur unter python 3.4 funktioniert.
# Es würde zu einer Fehlermeldung kommen, wenn man in das vorliegende Programm unter python 3.6 verwendet und diese Pakete zu nächst einlädt.

def freq(df, var, nomiss = False):
    """ Erzeugt Häufigkeitstabelle ähnlich der in Stata"""
    n = df.groupby([var]).size()
    N = n.sum()
    p = n/N *100
    P = p.sum()
    mis = pd.isnull(df[var]).sum()
    all = N + mis
    c = p.cumsum().map("{0:.2f}".format)
    if mis == 0 or nomiss==True:
        p = p.map("{0:.2f}".format)
        n = n.map("{0:.0f}".format)
        f = pd.DataFrame(collections.OrderedDict(Freq = n, Perc = p, Cum = c))
        t = pd.Series(collections.OrderedDict(Freq = "", Perc = "", Cum = ""), name="")
        f = f.append(t)
        t = pd.Series(collections.OrderedDict(Freq = N, Perc = P, Cum = 100), name="Total")
        f = f.append(t)
    else:
        p_all = n/(all)*100
        p_mis = mis/all*100
        p_o_mis = 100 - p_mis
        p = p.map("{0:.2f}".format)
        n = n.map("{0:.0f}".format)
        p_all = p_all.map("{0:.2f}".format)
        p_mis = "{0:.2f}".format(p_mis)
        p_o_mis = "{0:.2f}".format(p_o_mis)
        f = pd.DataFrame(collections.OrderedDict(Freq = n, Perc = p_all, Valid = p,  Cum = c))
        t = pd.Series(collections.OrderedDict(Freq = "", Perc = "", Valid = "", Cum = ""), name="")
        f = f.append(t)
        t = pd.Series(collections.OrderedDict(Freq = N, Perc = p_o_mis, Valid = P, Cum = ""), name="Total")
        f = f.append(t)
        t = pd.Series(collections.OrderedDict(Freq = mis, Perc = p_mis, Valid = "", Cum = ""), name="Missing")
        f = f.append(t)
        t = pd.Series(collections.OrderedDict(Freq = all, Perc = 100, Valid = "", Cum = ""), name="All")
        f = f.append(t)

    return f

def load_spssvars(var):
    """ Folgende Pakete werden für diese Funktion benötigt: spss, spssdata, pandas.    
    Überträgt ausgewählte Variablen aus einem SPSS Datensatz in einen pandas DataFrame. 
    Die gewünschten Variablen müssen als strings in einer Liste als Parameter in die Funktion eingegegen werden.
    Bsp: var = ["var1", "var2", ect.] """
    
    import spss, spssdata

    data = spssdata.Spssdata(var).fetchall()
        
    content = []        
    for i in range(len(data)):
        content.append(list(data[i]))
        
    labels = []
    for name in var:
        labels.append(name)        
    df = pd.DataFrame(content, columns = labels)            
        
    return(df)

def count_words(liste):
    """ Benötigte Pakete: collections, pandas
    Gibt die Häufigkeiten von Wörtern in einer Liste zurück. 
    Achtung: Die Liste muss eine einfache Liste mit strings sein. Eine Liste mit Listen von strings wird nicht erkannt."""
    
    if any(isinstance(el, list) for el in liste) == False:
        cnt_words = collections.Counter(liste).most_common()
        df = pd.DataFrame(cnt_words)
        df.columns = ["Words", "Counts"]
        df['Percent'] = df['Counts'] / len(liste)
    
        return df
    
    else:
        print('Your list contains several list. Use a single list with strings as input to the function')
    
