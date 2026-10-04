## Development:

[uv tutorial](https://flocode.substack.com/p/044-python-environments-again-uv)
1. Starting local env:
```shell
uv venv
```

2. (Optional) Running ingestion:
```shell
uv run src/data_proccess/ingestion/main.py
```

```
Logs:
uv run src/data_proccess/ingestion/main.py
🔍 Raspando os links diretamente da página do TSE...

✅ Sucesso! Encontrados 92 links de arquivos comprimidos (.zip):
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_AC_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_AL_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_AM_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_AP_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_BA_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_BR_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_CE_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_DF_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_ES_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_GO_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_MA_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_MG_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_MS_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_MT_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_PA_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_PB_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_PE_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_PI_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_PR_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_RJ_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_RN_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_RO_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_RR_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_RS_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_SC_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_SE_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_SP_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/eleicoes/eleicoes2026/fotos/foto_cand2026_TO_div.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/bem_candidato/bem_candidato_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_AC.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_AL.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_AM.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_AP.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_BA.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_BR.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_CE.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_DF.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_ES.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_GO.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_MA.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_MG.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_MS.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_MT.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_PA.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_PB.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_PE.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_PI.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_PR.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_RJ.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_RN.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_RO.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_RR.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_RS.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_SC.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_SE.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_SP.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/certidao_criminal/certidao_criminal_2026_TO.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/rede_social_candidato_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand_complementar/consulta_cand_complementar_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_coligacao/consulta_coligacao_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_vagas/consulta_vagas_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/historico_candidatura/historico_candidatura_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/motivo_cassacao/motivo_cassacao_2026.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_AC.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_AL.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_AM.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_AP.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_BA.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_BR.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_CE.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_DF.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_ES.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_GO.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_MA.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_MG.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_MS.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_MT.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_PA.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_PB.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_PE.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_PI.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_PR.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_RJ.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_RN.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_RO.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_RR.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_RS.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_SC.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_SE.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_SP.zip
🔹 https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2026_TO.zip
🔗 Processando 92 arquivos...
✅ Sucesso: foto_cand2026_AM_div.zip -> src/infrastructure/storage/landing/fotos/AM/
✅ Sucesso: foto_cand2026_BR_div.zip -> src/infrastructure/storage/landing/fotos/BR/
✅ Sucesso: foto_cand2026_AL_div.zip -> src/infrastructure/storage/landing/fotos/AL/
✅ Sucesso: foto_cand2026_CE_div.zip -> src/infrastructure/storage/landing/fotos/CE/
✅ Sucesso: foto_cand2026_AP_div.zip -> src/infrastructure/storage/landing/fotos/AP/
✅ Sucesso: foto_cand2026_AC_div.zip -> src/infrastructure/storage/landing/fotos/AC/
✅ Sucesso: foto_cand2026_ES_div.zip -> src/infrastructure/storage/landing/fotos/ES/
✅ Sucesso: foto_cand2026_DF_div.zip -> src/infrastructure/storage/landing/fotos/DF/
✅ Sucesso: foto_cand2026_BA_div.zip -> src/infrastructure/storage/landing/fotos/BA/
✅ Sucesso: foto_cand2026_MS_div.zip -> src/infrastructure/storage/landing/fotos/MS/
✅ Sucesso: foto_cand2026_MA_div.zip -> src/infrastructure/storage/landing/fotos/MA/
✅ Sucesso: foto_cand2026_MG_div.zip -> src/infrastructure/storage/landing/fotos/MG/
✅ Sucesso: foto_cand2026_MT_div.zip -> src/infrastructure/storage/landing/fotos/MT/
✅ Sucesso: foto_cand2026_GO_div.zip -> src/infrastructure/storage/landing/fotos/GO/
✅ Sucesso: foto_cand2026_PI_div.zip -> src/infrastructure/storage/landing/fotos/PI/
✅ Sucesso: foto_cand2026_PE_div.zip -> src/infrastructure/storage/landing/fotos/PE/
✅ Sucesso: foto_cand2026_PB_div.zip -> src/infrastructure/storage/landing/fotos/PB/
✅ Sucesso: foto_cand2026_PA_div.zip -> src/infrastructure/storage/landing/fotos/PA/
✅ Sucesso: foto_cand2026_RN_div.zip -> src/infrastructure/storage/landing/fotos/RN/
✅ Sucesso: foto_cand2026_RR_div.zip -> src/infrastructure/storage/landing/fotos/RR/
✅ Sucesso: foto_cand2026_RO_div.zip -> src/infrastructure/storage/landing/fotos/RO/
✅ Sucesso: foto_cand2026_PR_div.zip -> src/infrastructure/storage/landing/fotos/PR/
✅ Sucesso: foto_cand2026_RS_div.zip -> src/infrastructure/storage/landing/fotos/RS/
✅ Sucesso: foto_cand2026_RJ_div.zip -> src/infrastructure/storage/landing/fotos/RJ/
✅ Sucesso: foto_cand2026_SE_div.zip -> src/infrastructure/storage/landing/fotos/SE/
✅ Sucesso: foto_cand2026_SC_div.zip -> src/infrastructure/storage/landing/fotos/SC/
✅ Sucesso: foto_cand2026_TO_div.zip -> src/infrastructure/storage/landing/fotos/TO/
✅ Sucesso: bem_candidato_2026.zip -> src/infrastructure/storage/landing/bem_candidato/BR/
✅ Sucesso: foto_cand2026_SP_div.zip -> src/infrastructure/storage/landing/fotos/SP/
✅ Sucesso: certidao_criminal_2026_AL.zip -> src/infrastructure/storage/landing/certidao_criminal/AL/
✅ Sucesso: certidao_criminal_2026_AP.zip -> src/infrastructure/storage/landing/certidao_criminal/AP/
✅ Sucesso: certidao_criminal_2026_AC.zip -> src/infrastructure/storage/landing/certidao_criminal/AC/
✅ Sucesso: certidao_criminal_2026_BR.zip -> src/infrastructure/storage/landing/certidao_criminal/BR/
✅ Sucesso: certidao_criminal_2026_AM.zip -> src/infrastructure/storage/landing/certidao_criminal/AM/
✅ Sucesso: certidao_criminal_2026_DF.zip -> src/infrastructure/storage/landing/certidao_criminal/DF/
✅ Sucesso: certidao_criminal_2026_CE.zip -> src/infrastructure/storage/landing/certidao_criminal/CE/
✅ Sucesso: certidao_criminal_2026_ES.zip -> src/infrastructure/storage/landing/certidao_criminal/ES/
✅ Sucesso: certidao_criminal_2026_GO.zip -> src/infrastructure/storage/landing/certidao_criminal/GO/
✅ Sucesso: certidao_criminal_2026_BA.zip -> src/infrastructure/storage/landing/certidao_criminal/BA/
✅ Sucesso: certidao_criminal_2026_MA.zip -> src/infrastructure/storage/landing/certidao_criminal/MA/
✅ Sucesso: certidao_criminal_2026_MS.zip -> src/infrastructure/storage/landing/certidao_criminal/MS/
✅ Sucesso: certidao_criminal_2026_PB.zip -> src/infrastructure/storage/landing/certidao_criminal/PB/
✅ Sucesso: certidao_criminal_2026_MT.zip -> src/infrastructure/storage/landing/certidao_criminal/MT/
✅ Sucesso: certidao_criminal_2026_PA.zip -> src/infrastructure/storage/landing/certidao_criminal/PA/
✅ Sucesso: certidao_criminal_2026_PE.zip -> src/infrastructure/storage/landing/certidao_criminal/PE/
✅ Sucesso: certidao_criminal_2026_MG.zip -> src/infrastructure/storage/landing/certidao_criminal/MG/
✅ Sucesso: certidao_criminal_2026_PI.zip -> src/infrastructure/storage/landing/certidao_criminal/PI/
✅ Sucesso: certidao_criminal_2026_RN.zip -> src/infrastructure/storage/landing/certidao_criminal/RN/
✅ Sucesso: certidao_criminal_2026_RR.zip -> src/infrastructure/storage/landing/certidao_criminal/RR/
✅ Sucesso: certidao_criminal_2026_RO.zip -> src/infrastructure/storage/landing/certidao_criminal/RO/
✅ Sucesso: certidao_criminal_2026_SE.zip -> src/infrastructure/storage/landing/certidao_criminal/SE/
✅ Sucesso: certidao_criminal_2026_PR.zip -> src/infrastructure/storage/landing/certidao_criminal/PR/
✅ Sucesso: certidao_criminal_2026_TO.zip -> src/infrastructure/storage/landing/certidao_criminal/TO/
✅ Sucesso: consulta_cand_2026.zip -> src/infrastructure/storage/landing/consulta_cand/BR/
✅ Sucesso: rede_social_candidato_2026.zip -> src/infrastructure/storage/landing/consulta_cand/BR/
✅ Sucesso: consulta_cand_complementar_2026.zip -> src/infrastructure/storage/landing/consulta_cand_complementar/BR/
✅ Sucesso: consulta_coligacao_2026.zip -> src/infrastructure/storage/landing/consulta_coligacao/BR/
✅ Sucesso: consulta_vagas_2026.zip -> src/infrastructure/storage/landing/consulta_vagas/BR/
✅ Sucesso: historico_candidatura_2026.zip -> src/infrastructure/storage/landing/historico_candidatura/BR/
✅ Sucesso: motivo_cassacao_2026.zip -> src/infrastructure/storage/landing/motivo_cassacao/BR/
✅ Sucesso: proposta_governo_2026_AC.zip -> src/infrastructure/storage/landing/proposta_governo/AC/
✅ Sucesso: proposta_governo_2026_AL.zip -> src/infrastructure/storage/landing/proposta_governo/AL/
✅ Sucesso: certidao_criminal_2026_RS.zip -> src/infrastructure/storage/landing/certidao_criminal/RS/
✅ Sucesso: proposta_governo_2026_AP.zip -> src/infrastructure/storage/landing/proposta_governo/AP/
✅ Sucesso: proposta_governo_2026_BA.zip -> src/infrastructure/storage/landing/proposta_governo/BA/
✅ Sucesso: proposta_governo_2026_BR.zip -> src/infrastructure/storage/landing/proposta_governo/BR/
✅ Sucesso: proposta_governo_2026_CE.zip -> src/infrastructure/storage/landing/proposta_governo/CE/
✅ Sucesso: proposta_governo_2026_DF.zip -> src/infrastructure/storage/landing/proposta_governo/DF/
✅ Sucesso: proposta_governo_2026_AM.zip -> src/infrastructure/storage/landing/proposta_governo/AM/
✅ Sucesso: proposta_governo_2026_GO.zip -> src/infrastructure/storage/landing/proposta_governo/GO/
✅ Sucesso: proposta_governo_2026_ES.zip -> src/infrastructure/storage/landing/proposta_governo/ES/
✅ Sucesso: proposta_governo_2026_MA.zip -> src/infrastructure/storage/landing/proposta_governo/MA/
✅ Sucesso: proposta_governo_2026_MS.zip -> src/infrastructure/storage/landing/proposta_governo/MS/
✅ Sucesso: proposta_governo_2026_MT.zip -> src/infrastructure/storage/landing/proposta_governo/MT/
✅ Sucesso: proposta_governo_2026_MG.zip -> src/infrastructure/storage/landing/proposta_governo/MG/
✅ Sucesso: proposta_governo_2026_PB.zip -> src/infrastructure/storage/landing/proposta_governo/PB/
✅ Sucesso: proposta_governo_2026_PA.zip -> src/infrastructure/storage/landing/proposta_governo/PA/
✅ Sucesso: proposta_governo_2026_PI.zip -> src/infrastructure/storage/landing/proposta_governo/PI/
✅ Sucesso: proposta_governo_2026_PE.zip -> src/infrastructure/storage/landing/proposta_governo/PE/
✅ Sucesso: proposta_governo_2026_PR.zip -> src/infrastructure/storage/landing/proposta_governo/PR/
✅ Sucesso: proposta_governo_2026_RJ.zip -> src/infrastructure/storage/landing/proposta_governo/RJ/
✅ Sucesso: proposta_governo_2026_RN.zip -> src/infrastructure/storage/landing/proposta_governo/RN/
✅ Sucesso: proposta_governo_2026_RR.zip -> src/infrastructure/storage/landing/proposta_governo/RR/
✅ Sucesso: proposta_governo_2026_RO.zip -> src/infrastructure/storage/landing/proposta_governo/RO/
✅ Sucesso: proposta_governo_2026_SC.zip -> src/infrastructure/storage/landing/proposta_governo/SC/
✅ Sucesso: proposta_governo_2026_RS.zip -> src/infrastructure/storage/landing/proposta_governo/RS/
✅ Sucesso: proposta_governo_2026_SE.zip -> src/infrastructure/storage/landing/proposta_governo/SE/
✅ Sucesso: proposta_governo_2026_SP.zip -> src/infrastructure/storage/landing/proposta_governo/SP/
✅ Sucesso: proposta_governo_2026_TO.zip -> src/infrastructure/storage/landing/proposta_governo/TO/
✅ Sucesso: certidao_criminal_2026_SC.zip -> src/infrastructure/storage/landing/certidao_criminal/SC/
✅ Sucesso: certidao_criminal_2026_SP.zip -> src/infrastructure/storage/landing/certidao_criminal/SP/
✅ Sucesso: certidao_criminal_2026_RJ.zip -> src/infrastructure/storage/landing/certidao_criminal/RJ/

🎉 Pipeline finalizado em 637.27 segundos!
```