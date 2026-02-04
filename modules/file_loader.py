import logging, os

#Fonction qui lit et retourne une liste de toutes les lignes.
def read_file(fi):

    try:
        with open(fi, "r") as f:
            if os.path.splitext(fi)[1] == '.log':
                logs = f.readlines()
                result = []
                for ligne in logs:
                    result.append(ligne.replace('\n', ''))

                #vérifier que le fichier contient des données
                if len(logs) > 0 and len(logs[0]) > 0 :
                    return result
                else:
                    logging.info('Empty file')
                    return None
            else:
                logging.error('File not .log')
    except FileNotFoundError:
        logging.error('File not found')
    except PermissionError:
        logging.error('Permission denied')