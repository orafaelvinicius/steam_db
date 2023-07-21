# SCRIPT

Diretório responsável por armazenar todos os arquivos necessários para rodar a aplicação

## Arquitetura

```
├── script
   ├── attempts
   │   ├── api_steam.py
   │   ├── force_antiCAPTCHA.py
   │   ├── lib_steam.py
   │   └── req_sales.py
   ├── main.py
   ├── procedures
   │   ├── screaping.py
   │   ├── send_to_big_query.py
   │   └── send_to_sheets.py
   └── token.json
```

### Descrição dos diretórios

- attempts: Diretório responsável por armazenar todas as tentativas de realizar a tarefa
- procedures: Diretório responsável por armazenar todos os executores do main.py

### Descrição dos arquivos

- main.py: Responsável pela execução de todos os scripts utilizados para realizar a tarefa.
- screaping.py: Responsável pela raspagem e tratamento de dados
- send_to_big_query.py: Responsável pelo envio de dados para o Big Query
- send_to_sheets.py: Responsável pelo envio de dados para o planilhas do Google

  - api_steam.py: Arquivo utilizado para realizar o acesso às informações da Steam via API
  - force_antiCAPTCHA.py: Arquivo utilizado para realizar a quebra do CAPTCHA do steamdb
  - lib_steam.py: Arquivo utilizado para realizar a coleta dos dados através da biblioteca
  - req_sales.py: Arquivo utilizado para realizar a raspagem do steamdb com bs4
