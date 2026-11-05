# RAG para o Edital do Restaurante Universitário da UFPB

Projeto de estudo para fazer perguntas, em português, sobre um edital em PDF e conferir as respostas nas páginas e nos trechos originais.

## Estado atual

Etapa 1: estrutura inicial e instruções de preparação. Ainda não há extração, indexação ou consulta implementadas. O PDF do edital será fornecido depois; não coloque documentos pessoais neste projeto.

## Preparação no Windows 10

Abra o PowerShell nesta pasta e execute:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se o PowerShell bloquear a ativação do ambiente, consulte a política de execução configurada no seu Windows ou use o interpretador diretamente em `.venv\Scripts\python.exe`. Não é preciso mudar uma configuração global do sistema para este projeto.

Para confirmar qual Python está ativo:

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

O ambiente virtual e as dependências ainda não foram criados/instalados nesta etapa.

## Estrutura

- `src/rag_edital/`: código da aplicação, organizado por etapa do fluxo.
- `data/edital/`: local para o PDF do edital fornecido pela pessoa usuária.
- `data/index/`: índice local, gerado a partir do PDF e reconstruível quando necessário.
- `.env.example`: exemplo sem segredos; será ampliado se a opção por APIs for escolhida.
- `.env`: configuração local e segredos; não deve ser versionado.

O índice deverá guardar metadados de origem, versão e página do PDF. A página impressa, se identificável, ficará separada. Uma alteração no hash do PDF ou na configuração/modelo de embeddings exigirá reconstruir o índice; perguntas não deverão reprocessar o PDF.

## Próximas etapas

1. Extrair o texto do PDF por página e conferir a extração.
2. Dividir o texto em trechos mantendo fonte, versão e páginas.
3. Criar e reutilizar o índice; comparar busca por palavras-chave e vetores.
4. Consultar os trechos e, depois de escolher geração local ou API, produzir respostas com citações.
5. Avaliar evidências, citações, atualização/possíveis retificações, tempo e custos.

Respostas, prazos e requisitos devem ser conferidos na fonte oficial. O programa não pode assumir que um edital sem retificação identificada continua atualizado.
