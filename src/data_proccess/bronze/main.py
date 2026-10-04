import zipfile
import pandas as pd
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

STORAGE_DIR = Path("src/infrastructure/storage")
LANDING_DIR = STORAGE_DIR / "landing"
BRONZE_DIR = STORAGE_DIR / "bronze" # Mudamos para Bronze!
ASSETS_DIR = STORAGE_DIR / "assets"

def zip_reader(caminho_zip: Path):
    uf = caminho_zip.parent.name
    categoria = caminho_zip.parent.parent.name

    # Definimos quais categorias são "Arquivos/Documentos" (Assets)
    categorias_assets = ["fotos", "certidao_criminal", "proposta_governo"]

    try:
        with zipfile.ZipFile(caminho_zip, 'r') as zf:
            lista_arquivos = zf.namelist()

            # 1. PROCESSAMENTO DE DOCUMENTOS/MÍDIA (ASSETS)
            if categoria in categorias_assets:
                pasta_assets = ASSETS_DIR / categoria / uf
                pasta_assets.mkdir(parents=True, exist_ok=True)
                
                arquivos_extraidos = 0
                for arquivo_interno in lista_arquivos:
                    # Opcional: ignorar o arquivo de instruções do TSE
                    if "leiame" in arquivo_interno.lower():
                        continue
                    
                    # Agora aceitamos também .pdf!
                    if arquivo_interno.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf')):
                        zf.extract(arquivo_interno, path=pasta_assets)
                        arquivos_extraidos += 1
                        
                return f"📁 [ASSETS] {arquivos_extraidos} arquivos extraídos de {caminho_zip.name} para {categoria}."

            # 2. PROCESSAMENTO DE DADOS TABULARES (LANDING -> BRONZE)
            else:
                pasta_bronze = BRONZE_DIR / categoria / uf
                pasta_bronze.mkdir(parents=True, exist_ok=True)

                arquivos_dados = [f for f in lista_arquivos if f.lower().endswith(('.csv', '.txt'))]

                for arquivo_dados in arquivos_dados:
                    with zf.open(arquivo_dados) as f:
                        df = pd.read_csv(
                            f, 
                            sep=';', 
                            encoding='latin1', 
                            dtype=str, 
                            low_memory=False
                        )
                        
                        nome_parquet = f"{Path(arquivo_dados).stem}.parquet"
                        caminho_parquet = pasta_bronze / nome_parquet
                        
                        df.to_parquet(caminho_parquet, engine='pyarrow', index=False)
                        
                return f"📊 [DADOS] {caminho_zip.name} -> Bronze convertida com sucesso."
                        
    except Exception as e:
        return f"❌ Erro em {caminho_zip.name}: {e}"

def bronze_pipeline(zip_files):  
    if not zip_files:
        print("⚠️ Nenhum arquivo encontrado.")
        return

    print(f"⏳ Processando {len(zip_files)} arquivos usando Multiprocessing...")

    # CUIDADO: Limite os workers baseado na sua RAM. 
    # Ler múltiplos CSVs grandes simultaneamente devora a RAM da máquina.
    # Um bom número inicial é o número de núcleos da sua CPU menos 1 (ou 2, se tiver pouca RAM).
    MAX_WORKERS = 5

    # ProcessPoolExecutor cria processos filhos separados na CPU
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Envia as tarefas para o pool
        futuros = {executor.submit(zip_reader, caminho): caminho for caminho in zip_files}
        
        # Conforme forem acabando, pega o resultado
        for futuro in as_completed(futuros):
            resultado = futuro.result()
            print(resultado)

    print("\n🎉 Pipeline Landing -> Bronze finalizado!")

if __name__ == "__main__":
    zip_files = list(LANDING_DIR.rglob('*.zip'))
    bronze_pipeline(zip_files=zip_files)
