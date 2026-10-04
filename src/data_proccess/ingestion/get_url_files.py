import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url_pagina = "https://dadosabertos.tse.jus.br/dataset/candidatos-2026"

# Cabeçalho essencial para o servidor do governo não bloquear sua requisição
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"🔍 Raspando os links diretamente da página do TSE...")

def get_url_files():
    resposta = requests.get(url_pagina, headers=headers)
    resposta.raise_for_status()
    
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    links_zip = set() # Usando set para evitar links duplicados
    
    # Busca todas as tags de link (<a>) na página
    for tag_a in soup.find_all('a', href=True):
        href = tag_a['href']
        
        # Resolve o link caso ele seja relativo (/dataset/...)
        link_completo = urljoin(url_pagina, href)
        
        # Filtra apenas os links que apontam para arquivos .zip
        if ".zip" in link_completo:
            links_zip.add(link_completo)
            
    # Separando para exibição limpa
    lista_links = sorted(list(links_zip))
    
    print(f"\n✅ Sucesso! Encontrados {len(lista_links)} links de arquivos comprimidos (.zip):")
    for link in lista_links:
        # Exemplo filtrando apenas os metadados principais (bens, candidatos, vagas)
        # if "eleicoes2026/fotos" not in link and "proposta_governo" not in link:
        print(f"🔹 {link}")
    
    return lista_links
