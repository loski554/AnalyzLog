import logging, datetime

#Fonction qui genere le texte du résumé
def resume_report(dic, statut, file_name, dt):

    nb_line = len(dic['INFO']) + len(dic['ERROR']) + len(dic['WARNING']) + len(dic['INVALID'])
    
    txt = [
        f'\n\nFichier analysé : {file_name}\nDate d\'analyse : {dt}\nNombre de ligne : {nb_line}\n\n', '-'*50, '\nRÉSUMÉ GLOBAL\n', '-'*50,
        f'\nLignes valides : {len(dic['INFO']) + len(dic['WARNING']) + len(dic['ERROR'])}\nLignes invalides : {len(dic['INVALID'])}\n',
        f'\nNiveaux détectés :\n- INFO :  {len(dic['INFO'])}\n- ERROR : {len(dic['ERROR'])}\n- WARNING : {len(dic['WARNING'])}\n\nStatut global: {statut}\n\n'
        ]

    result = ''.join(txt)

    return result

#Fonction qui genere le texte du detail
def detail_report(dic):

    txt = ['-'*50, '\nDÉTAIL PAR NIVEAU\n', '-'*50, '\n\n[WARNING]\n']

    if len(dic['WARNING']) > 0:
        for ligne in dic['WARNING']:
            txt.append(f'- {ligne}\n')
    else:
        txt.append('x\n')
    
    txt.append('\n[ERROR]\n')

    if len(dic['ERROR']) > 0:
        for ligne in dic['ERROR']:
            txt.append(f'- {ligne}\n')
    else:
        txt.append('x\n')
    

    result = ''.join(txt)

    return result

#Fonction qui genere le texte des anomalies
def anomalies_report(dic, rec):
    
    txt = ['\n', '-'*50, '\nANOMALIES DÉTECTÉES\n', '-'*50]

    if len(rec) > 0:
        txt.append('\nMessages répété :\n')
        for ligne in rec:
            txt.append(f'- {rec[ligne]} fois : {ligne}\n')

    if len(dic['INVALID']) > 0:
        txt.append('\nPrésence de lignes invalides\n')
        for ligne in dic['INVALID']:
            txt.append(f'- \'{ligne}\'\n')
    else:
        txt.append('\nR.A.S\n')

    result = ''.join(txt)
    
    return result

#Fonction qui genere le texte de la conclusion
def conclusion_report(dic, statut):

    txt = ['\n', '-'*50, '\nCONCLUSION\n', '-'*50]

    if statut == 'ATTENTION':
        txt.append('\nMessage signalant le besoin d\'intervention suite a des erreurs et warning détectés .\n\n')
    else:
        txt.append('\nAucune erreur ou problème n\'est à signaler.\n\n')

    result = ''.join(txt)

    return result

#Fonction qui genere le rapport final
def report_gen(statut, file_name, dic, rec):

    dt = datetime.datetime.now().replace(microsecond=0)
    date = dt.date()

    #MSG DEBUT RAPPORT
    txt = ['='*50 + '\nRAPPORT D\'ANALYSE DES LOGS\n' + '='*50]

    #SECTION RESUME
    txt.append(resume_report(dic, statut, file_name, dt))
    #SECTION DETAILS
    txt.append(detail_report(dic))
    #SECTION ANOMALIES
    txt.append(anomalies_report(dic, rec))
    #SECTION CONCLUSION
    txt.append(conclusion_report(dic, statut))

    #MSG FIN DE RAPPORT
    txt.append('='*50 + '\nFIN DU RAPPORT\n' + '='*50)

    result = ''.join(txt)

    return result