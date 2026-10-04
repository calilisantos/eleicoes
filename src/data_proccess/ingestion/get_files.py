import asyncio
import aiohttp
import aiofiles
import time
from pathlib import Path

# IMPORTAÇÃO CORRIGIDA AQUI
from parse_url_files import parse_url_files 

LIMITE_CONEXOES = 5

async def _download_file(session: aiohttp.ClientSession, semaphore: asyncio.Semaphore, metadados: dict):
    async with semaphore:
        url = metadados["url"]
        caminho_completo = metadados["caminho_completo"]
        pasta = metadados["pasta_destino"]
        
        pasta.mkdir(parents=True, exist_ok=True)
        
        if caminho_completo.exists() and caminho_completo.stat().st_size > 0:
            print(f"⏩ Já existe: {metadados['nome_arquivo']}")
            return

        try:
            async with session.get(url) as resposta:
                resposta.raise_for_status()
                
                async with aiofiles.open(caminho_completo, "wb") as f:
                    async for bloco in resposta.content.iter_chunked(1024 * 64):
                        await f.write(bloco)
                        
                print(f"✅ Sucesso: {metadados['nome_arquivo']} -> {pasta}/")
        except Exception as e:
            print(f"❌ Erro em {metadados['nome_arquivo']}: {e}")
            if caminho_completo.exists():
                caminho_completo.unlink()

async def get_files(urls: list):
    if not urls:
        print("⚠️ Nenhuma URL fornecida.")
        return

    print(f"🔗 Processando {len(urls)} arquivos...")
    
    # NOME DA FUNÇÃO CORRIGIDO AQUI
    tarefas_download = [parse_url_files(url) for url in urls]
    
    tempo_inicial = time.time()
    semaphore = asyncio.Semaphore(LIMITE_CONEXOES)
    timeout = aiohttp.ClientTimeout(total=None, sock_connect=30, sock_read=60)
    
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tarefas = [_download_file(session, semaphore, meta) for meta in tarefas_download]
        await asyncio.gather(*tarefas)
        
    tempo_total = time.time() - tempo_inicial
    print(f"\n🎉 Pipeline finalizado em {tempo_total:.2f} segundos!")
