# rastreio_koala
Site para fazer os rastreios de todos os cliente da empresa koala consutando nas transportadoras usando o API delas.

API 
Sera usado 5 API das reespectivas transportadoras:
Translovato
Mandaê
Braspress
Loggi
Expresso São Miguel

baixar as bibliotecas
pip install -r requirements.txt

mandaê
200 → resposta recebida
401 → token inválido/ausente
403 → acesso não autorizado
404 → rastreio não encontrado
422 → problema nos dados enviados
500 → problema no servidor da API

testa a API Linux
curl -i -H "Authorization: SEU_TOKEN" "https://api.mandae.com.br/v2/trackings/SEU_CODIGO"

Testa a API Windonws
curl.exe -i -H "Authorization: SEU_TOKEN" "https://api.mandae.com.br/v2/trackings/SEU_CODIGO"