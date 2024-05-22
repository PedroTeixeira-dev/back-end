from logging.config import dictConfig
import logging
import os
from config.default import Config


log_path = "log/"
# Verifica se o diretorio para armexanar os logs não existe
if not os.path.exists(log_path):
   # então cria o diretorio
   os.makedirs(log_path)


dictConfig(Config.LOGGING)


logger = logging.getLogger(__name__)
