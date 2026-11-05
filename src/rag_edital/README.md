# Módulos da aplicação

O código será separado por responsabilidade, mantendo o fluxo explícito:

- `pdf_reader.py`: extração do texto e número de página do PDF.
- `chunker.py`: divisão em trechos e inclusão dos metadados de origem.
- `index_store.py`: criação, persistência e atualização do índice.
- `retriever.py`: busca por palavras-chave e/ou vetores.
- `answerer.py`: resposta baseada apenas nas evidências recuperadas.
- `cli.py`: interface de terminal.

Esses módulos serão criados junto com suas respectivas etapas, para que cada parte possa ser conferida antes da próxima. A escolha do provedor e dos modelos ainda está pendente.
