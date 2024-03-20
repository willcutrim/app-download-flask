import unittest
import requests

class TestApi(unittest.TestCase):

    def setUp(self):
        self.host = 'http://127.0.0.1:5000'
        self.sufixo = '/api/download'
        self.url = 'https://www.youtube.com/watch?v=FyPGFkmGCvE'

    def test_get_video_info_status_code_ok(self):
        """
        Teste se o código de status está OK ao obter informações de vídeo.
        """
        response = requests.get(f'{self.host}{self.sufixo}?video_url={self.url}')
        self.assertEqual(response.status_code, 200)

    def test_get_video_info_content_type_json(self):
        """
        Test o endpoint da API 'get_video_info' para garantir que ele retorne uma resposta JSON.

        Este teste envia uma solicitação GET ao endpoint da API com um parâmetro de URL de vídeo e verifica se a resposta
        tem um cabeçalho 'Content-Type' com um valor de 'application/json'.

        Parâmetros:
            self (TestClass): A instância da classe de teste.
        
        Retorna:
            None
        """
        response = requests.get(f'{self.host}{self.sufixo}?video_url={self.url}')
        self.assertEqual(response.headers['Content-Type'], 'application/json')


    










if __name__ == '__main__':
    unittest.main()