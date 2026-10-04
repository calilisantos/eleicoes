import re
from pathlib import Path

def parse_url_files(url: str) -> dict:
    """
    Analisa a URL e define o destino na camada 'landing'.
    Ex: landing/fotos/AC/foto_cand2026_AC_div.zip
    Ex: landing/bem_candidato/BR/bem_candidato_2026.zip
    """
    partes = url.split('/')
    nome_arquivo = partes[-1]
    
    # A categoria geralmente é o diretório pai na URL do TSE 
    # Ex: .../odsele/certidao_criminal/... -> 'certidao_criminal'
    categoria = partes[-2]
    
    # Busca a sigla do estado (UF) no final do arquivo (Ex: _AC.zip ou _SP_div.zip)
    # Se não encontrar, assume que é um arquivo nacional (BR)
    match_uf = re.search(r'_([A-Z]{2})(?:_div)?\.zip$', nome_arquivo)
    uf = match_uf.group(1) if match_uf else "BR"
    
    # Estrutura do Data Lake: landing / categoria / uf / arquivo.zip
    pasta_destino = Path(f"src/infrastructure/storage/landing/{categoria}/{uf}")
    
    return {
        "url": url,
        "nome_arquivo": nome_arquivo,
        "pasta_destino": pasta_destino,
        "caminho_completo": pasta_destino / nome_arquivo
    }
