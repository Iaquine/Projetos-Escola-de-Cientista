from imp import load_module
from pyexpat import model
import time
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd
import pickle as pck

class shows():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_model()

    def load_model(self):
        """"
        Carrega o modelo de classificacão de shows a ser usado
        """
        filename = '/code/arvore_model2.pkl'
        self.model = pck.load(open(filename, 'rb'))
        logger.debug(mensagens.FIM_LOAD_MODEL)


    def executar_rest(self, band_scores):
        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_predicts = self.buscar_predicao(band_scores['textoMensagem'])

        logger.debug(mensagens.FIM_PREDICT)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")
        
        df_response = pd.DataFrame(band_scores, columns=['textoMensagem'])
        df_response['predict'] = response_predicts

        df_response = df_response.drop(columns=['textoMensagem'])
        df_response = df_response.head(1)

        response = {
                     "Classificação": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    def buscar_predicao(self, band_scores):
        """
        Pega o modelo carregado e aplica em texts
        """
        logger.debug('Iniciando o predict...')

        self.load_model()
        #model.compile()
        predicted = self.model.predict([band_scores])

        if predicted == 0:
            print(predicted)
            return 'No! You should not go to this concert'
        else:
            print(predicted)
            return 'YES! You should go to this concert'

        