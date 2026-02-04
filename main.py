import logging, datetime
from modules.arguments import parse_arguments
from modules.file_loader import read_file
from modules.log_interpret import interpret
from modules.report_generator import report_gen
from modules.analyser import analyse_statut, recurrence

#Script Principal
def main():
    
    #récupération des données passés en arguments
    args = parse_arguments()
    fi = args.log_file

    #lecture du fichier et retourne les données
    logs = read_file(fi)

    if logs:
        #création du dictionnaire avec les données organisés
        dic = interpret(logs)

        #statut pour le rapport et recrrence des logs
        etat = analyse_statut(dic)
        rec = recurrence(dic)

        #structure du rapport
        report = report_gen(etat, fi, dic, rec)

        #récupération de la date et de l'heure
        now = datetime.datetime.now()
        dt = now.strftime("%Y-%m-%d-%H-%M-%S")

        #création + écriture du fichier rapport
        fichier = open(f'./reports/{dt}.txt', '+a')
        fichier.write(report)
        logging.info('Rapport généré avec succes. Voir repertoir ./reports')
    else:
        logging.info('Rapport non généré')


if __name__ == '__main__':

    #Config basic logging
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    #Appel script principal
    main()