import re

#Fonction pour trouver les récurrences dans les logs ERROR et WARNING
def recurrence(dic):

    pattern = r'[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?'

    rec = {}
    for ligne in dic['ERROR'] + dic['WARNING']:
        new_ligne = re.sub(pattern, '', ligne)
        rec[new_ligne] = rec.get(new_ligne, 0) + 1

    result = {}
    for ligne in rec:
        if rec[ligne] > 1:
            result[ligne] = rec[ligne]
    
    return result

#Détermine si le statut du rapport est 'OK', ou 'ATTENTION' si des erreurs ou warnings sont présents.
def analyse_statut(dic):

    if len(dic['ERROR']) > 0 or len(dic['WARNING']) > 0 or len(dic['INVALID']) > 0:
        return 'ATTENTION'
    else:
        return 'OK'
