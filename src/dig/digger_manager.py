"""Modulo che gestisce lo 'scavatore' delle cartelle."""

# Standard Import
import os
from hashlib import md5
from dataclasses import dataclass as dc, field
# Site-package Import

# Project Import
from util import config_manager as cm
from util import logger_manager as lm
from util import option_manager as om
from util import path_manager as pm
from meta import metadata_manager as mm
from index import indexer_manager as im



class DiggerManager():
    """Recupera i file nelle cartelle e manda i dati al DB.

    Apre i file nelle cartelle selezionate, quando rileva un nuovo
    file o una modifica, recupera i  nuovi metadata usnado metadata_manager
    e manda al database con index_manager.



    Il percorso della cartella viene passato nelle configurazioni,
    in fase di sviluppo si prenderà una costante."""

    def __init__(self,
                 path: pm.PathManager, 
                 option: om.OptionManager,
                 config: cm.ConfigManager,
                 log: lm.LoggerManager,
                 index: im.IndexerManager,
                 meta: mm.MetadataManager):
        
        """

        Args:
            path: percorsi delle risorse dell'applicazione(per ora ignorato)
            option: opzioni definite dall'utente(per ora ignorato)
            config: indicazione del percorso da monitorare
            log: raccoglie errori ed eventi in fase runtime
            index: collegamento e funzioni per il database
            meta: recupera i metadati dei files passati 
        """

        self.__path = path
        self.__option = option
        self.__config = config
        self.__log = log
        self.__index = index
        self.__meta = meta
        self.__dirPath = self.__config["path"]["source_folder"]


    def scan(self, path=None) -> None:
        """scansiona il percorso passato come parametro o quello nel config"""
        if(path == None):
            path = self.__dirPath
            
        with os.scandir(path) as el:
            for i in el:
                if (i.is_file()):
                    self.__log.info(f'File esaminato {i.path}')
                    
                    #calcolo dell'hash 
                    h = self.__resolve_checksum(i.path)
                    #aggiorna o inserisce in index
                    self.__update_index(i.path, h)

                #chiamata ricorsiva per le cartelle
                elif(i.is_dir()):
                    self.scan(path=i.path)


    def __resolve_checksum(self, path, type='md5') -> bytes:
        """calcola il checksum del file al percorso indicato
        
        da implementare la possibilità di usare altro algoritmo di hashing
        Return:
            binario che rappresenta il checksum (MD5)
        """
        try:
            with open(path, 'rb') as file:
                file_hash = md5(file.read())
                self.__log.info(f'updated md5 {file_hash.digest()}')
                return file_hash.digest()
        except Exception as err:
            self.__log.error(err)


############################### Test ##########################################

if __name__ == "__main__":
    pass

###############################################################################