# %%
import requests
from bs4 import BeautifulSoup

def get_content(url):
    headers = {
    'authority': 'www.residentevildatabase.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'SLG_G_WPT_TO=pt; _gid=GA1.2.1584669900.1712077885; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; _ga_DJLCSW50SC=GS1.1.1712077884.1.1.1712079659.60.0.0; _gat_gtag_UA_29446588_1=1; _ga_D6NF5QC4QT=GS1.1.1712077885.1.1.1712079660.59.0.0; _ga=GA1.1.1811783422.1712077885; FCNEC=%5B%5B%22AKsRol8oR35LxN6CEKSyXZgGzigqxWSOC87wXtDEzQnYv6LMc9ZnAqmB0Emb6jBhV661bRbEr-FwcyPJ9u6iHmoCpADPGO86Sydn9MKEsrfp_blMO1xqPIBlMhcmhtHF_FVxZs_5EkZYUXOEr34ntZGUaTmhbsJnfQ%3D%3D%22%5D%5D',
    'referer': 'https://www.residentevildatabase.com/personagens/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Opera GX";v="107", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
}
    resp = requests.get(url, headers=headers)
    return resp


def get_basic_infos(soup):
    div_page = soup.find("div", class_="td-page-content")
    paragrafo = div_page.find_all("p")[1]
    linhas = paragrafo.find_all("em")
    
    data = {}
    
    for i in linhas:
        chave, valor = i.text.split(":")
        chave = chave.strip(" ")
        data[chave] = valor.strip(" ")

    return data


def get_aparicoes(soup):
    lis = (soup.find("div", class_="td-page-content").
       find("h4").
       find_next().
       find_all('li'))
    
    aparicoes = [i.text for i in lis ]
    return aparicoes
# %%
url = "https://www.residentevildatabase.com/personagens/ada-wong/"
resp = get_content(url)
# %%
if resp.status_code != 200:
    print('Não foi possível realizar a requisição')
else:
    soup = BeautifulSoup(resp.text)
    get_basic_infos(soup)
# %%

