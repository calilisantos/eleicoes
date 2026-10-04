import pandas as pd

print(pd.read_parquet("src/infrastructure/storage/silver/consulta_cand/consulta_cand_2026.parquet").columns)
print(pd.read_parquet("src/infrastructure/storage/silver/consulta_cand/consulta_cand_2026.parquet").head(5).to_dict())