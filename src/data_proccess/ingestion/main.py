import asyncio
from get_files import get_files
from get_url_files import get_url_files

if __name__ == "__main__":
    try:
        # Pega a lista de strings (URLs)
        url_files = get_url_files()
        
        # Inicia o pipeline de download
        asyncio.run(get_files(url_files))
        
    except Exception as e:
        print(f"❌ Erro fatal no fluxo principal: {e}")
