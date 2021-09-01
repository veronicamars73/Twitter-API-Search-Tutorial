from decouple import config
import requests
import json

bearer_token = config('BEARERTOKEN')

def set_autenticacao(objeto_para_auth):
    """
    Método que acrescenta no objeto da busca um cabeçalho correspondente a autenticação do request.
    """

    objeto_para_auth.headers["Authorization"] = f"Bearer {bearer_token}"
    return objeto_para_auth


def realiza_request(url_endpoint, params):
    """
    Método que realiza a solicitação HTTP get com informações relacionadas a
    parâmetros de busca, endpoint e autenticação.
    """

    response = requests.get(url_endpoint, auth=set_autenticacao, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main(perfil, chave_busca, lingua, limite_tweets):
    search_url = "https://api.twitter.com/2/tweets/search/recent"

    str_aux = f'to:{perfil} {chave_busca} lang:{lingua}'
    query_params = {'query': str_aux,
                    'tweet.fields': 'attachments,author_id,created_at,lang,public_metrics,source',
                    'max_results':limite_tweets}
                    
    r = realiza_request(search_url, query_params)

    print(json.dumps(r, indent=4, sort_keys=True))


if __name__ == '__main__':
    main("PSG_English","Mbappe",'en',100)