import argparse

#Récupère les entrées passé en argument.
def parse_arguments():

    parser = argparse.ArgumentParser(prog='analyzLog', description='Analyse de log')

    parser.add_argument('log_file', help='chemin du fichier log à analyser')

    args = parser.parse_args()

    return args