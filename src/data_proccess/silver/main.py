import pandas as pd
import re
from pathlib import Path

STORAGE_DIR = Path("src/infrastructure/storage")
BRONZE_DIR = STORAGE_DIR / "bronze"
SILVER_DIR = STORAGE_DIR / "silver"

def silver_pipeline():
    print("⏳ Iniciando o processamento Bronze -> Silver...\n")
    
    # Vamos varrer todas as pastas da Bronze (consulta_cand, bem_candidato, etc)
    pastas_categorias = [p for p in BRONZE_DIR.iterdir() if p.is_dir()]
    
    for pasta_categoria in pastas_categorias:
        # Acessa a subpasta (ex: consulta_cand/BR/)
        pasta_arquivos = pasta_categoria / "BR"
        if not pasta_arquivos.exists():
            continue
            
        arquivos_parquet = list(pasta_arquivos.glob("*.parquet"))
        
        # Dicionário para separar por assunto (Ex: "consulta_cand_2026": [arq_SP, arq_RJ...])
        entidades = {}
        
        for arq in arquivos_parquet:
            nome = arq.stem # Nome sem a extensão
            
            # Usamos Regex para separar o Assunto da UF
            # Ex: "rede_social_candidato_2026_SP" -> base: "rede_social_candidato_2026", uf: "SP"
            match = re.match(r"(.+)_([A-Z]{2}|BRASIL)$", nome)
            
            if match:
                base = match.group(1)
                uf = match.group(2)
                
                # Ignoramos o _BRASIL para evitar duplicação (vamos construir nosso próprio dataset nacional)
                if uf == "BRASIL":
                    continue
                    
                if base not in entidades:
                    entidades[base] = []
                entidades[base].append(arq)

        # Agora concatenamos e limpamos cada assunto separadamente
        for entidade, lista_arquivos in entidades.items():
            print(f"🔄 Consolidando: {entidade} ({len(lista_arquivos)} arquivos)")
            
            # Lê todos os arquivos Parquet dessa entidade
            lista_dfs = [pd.read_parquet(f) for f in lista_arquivos]
            
            # Concatena todos num único DataFrame Nacional
            df_final = pd.concat(lista_dfs, ignore_index=True)
            
            # ==========================================
            # 🧹 LIMPEZA PADRÃO CAMADA SILVER
            # ==========================================
           # 1. Padronizar nomes das colunas (tudo minúsculo, sem espaços)
            df_final.columns = [c.lower().strip() for c in df_final.columns]
            
            # 2. Limpar Lixo do TSE (Expansão de variações)
            valores_lixo = [
                "#NULO#", "#NULO", 
                "#NE#", "#NE", 
                "-1", "-3", "-4",
                "NÃO DIVULGÁVEL"
            ]
            
            # O Pandas vai procurar qualquer string exata dessa lista e trocar pelo nulo nativo
            df_final.replace(valores_lixo, pd.NA, inplace=True)
            
            # 3. Remover duplicatas (Sempre bom garantir)
            linhas_antes = len(df_final)
            df_final.drop_duplicates(inplace=True)
            linhas_depois = len(df_final)
            if linhas_antes != linhas_depois:
                print(f"   ⚠️ Removidas {linhas_antes - linhas_depois} linhas duplicadas!")

            # ==========================================
            # 💾 SALVAR NA SILVER
            # ==========================================
            pasta_destino = SILVER_DIR / pasta_categoria.name
            pasta_destino.mkdir(parents=True, exist_ok=True)
            
            # Salvaremos um ÚNICO arquivo Parquet consolidado (muito melhor para analisar depois)
            caminho_salvar = pasta_destino / f"{entidade}.parquet"
            df_final.to_parquet(caminho_salvar, engine="pyarrow", index=False)
            
            print(f"✅ Salvo: {caminho_salvar} | Linhas: {len(df_final)}\n")

if __name__ == "__main__":
    silver_pipeline()
