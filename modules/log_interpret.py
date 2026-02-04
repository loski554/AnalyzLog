import re, logging

#Fonction
def interpret(logs):
        
    dic = {'INFO' : [], 'ERROR' : [], 'WARNING': [], 'INVALID' : []}
    pattern = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?\s(TRACE|DEBUG|INFO|NOTICE|WARN|WARNING|ERROR|SEVERE|FATAL)\s')
    try:
        for ligne in logs:
            result = pattern.match(ligne)
            if result and 'INFO' in ligne:
                dic['INFO'].append(ligne)
            elif result and 'ERROR' in ligne:
                dic['ERROR'].append(ligne)
            elif result and 'WARNING' in ligne:
                dic['WARNING'].append(ligne)
            else:
                dic['INVALID'].append(ligne)
        return dic
    except TypeError:
        logging.error('Fichier vide')
