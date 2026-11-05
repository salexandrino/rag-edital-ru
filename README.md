# RAG para o Edital do Restaurante Universitário da UFPB

Projeto de estudo para fazer perguntas, em português, sobre um edital em PDF e conferir respostas nas páginas e nos trechos originais.

## Etapa atual: leitura e conferência do PDF

O programa lê o texto página por página e mostra uma amostra de cada página, com a numeração do arquivo PDF começando em 1. Ele não faz OCR, embeddings, indexação, busca ou geração de respostas nesta etapa.

O edital usado nesta etapa está em `data/edital/Edital-20-2026-RU-integral-todos-os-campi.pdf`. Não coloque documentos pessoais neste projeto.

## Preparação no Windows 10

Abra o terminal PowerShell do VS Code na pasta do projeto e execute:

```powershell
py -0p
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`py -0p` lista as instalações que o launcher do Windows encontra. O comando acima usa Python 3.14; se escolher outra versão compatível que apareça na lista, troque `-3.14` pela versão correspondente, por exemplo `-3.13`. Use uma instalação padrão do Python para Windows (CPython), não o Python do MSYS2. Neste ambiente, `python` aponta para o MSYS2, e `py -0p` não encontra uma instalação CPython. Se `py` não estiver disponível, instale o Python para Windows e reabra o VS Code. No VS Code, use **Python: Select Interpreter** e selecione `.venv\Scripts\python.exe`; feche e abra novamente o terminal integrado para atualizar o ambiente. Se a ativação for bloqueada pelo PowerShell, consulte a política de execução do seu Windows ou invoque os comandos diretamente com `.\.venv\Scripts\python.exe`.

Confirme que o ambiente virtual está ativo:

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

Nesta etapa, `requirements.txt` instala somente PyMuPDF. Chroma será considerado quando a etapa de indexação começar.

## Executar a extração

Passe o caminho do PDF como argumento. Coloque o caminho entre aspas se ele tiver espaços:

```powershell
python -m src.rag_edital.cli ".\data\edital\Edital-20-2026-RU-integral-todos-os-campi.pdf"
```

O programa informa o nome do arquivo, o total de páginas, quantas têm texto extraível e quantas não têm, e uma amostra de até 500 caracteres por página. Para mostrar amostras maiores:

```powershell
python -m src.rag_edital.cli ".\data\edital\Edital-20-2026-RU-integral-todos-os-campi.pdf" --sample-chars 1200
```

O número mostrado é a posição da página dentro do PDF, começando em 1. Ele pode diferir do número impresso na própria página; identificar essa numeração impressa será tratado em uma etapa posterior.

Uma página sem texto extraível pode ser uma imagem digitalizada e exigir OCR. O programa avisa, mas não executa OCR automaticamente. Se nenhuma página tiver texto extraível, a execução termina com uma mensagem de erro explicativa.

## Conferência manual

1. Compare a amostra de cada página com a mesma página aberta em um leitor de PDF.
2. Confira títulos, nomes, datas, acentos e números, que são elementos importantes para uma futura consulta.
3. Confirme que a amostra exibida sob “Página do PDF N” realmente aparece na folha N do arquivo. A numeração impressa pode ser diferente.
4. Se houver páginas sem texto, abra-as no leitor de PDF para verificar se são imagens digitalizadas. Esta etapa não extrai texto de imagens.

## Segurança e dados locais

O `.gitignore` exclui o ambiente virtual, arquivos temporários, segredos e o PDF/índice locais. O arquivo `.env.example` não contém chaves. Não envie PDFs para serviços externos nesta etapa.

## Próximas etapas planejadas

Depois de conferir a extração, o fluxo previsto é dividir o texto preservando origem e página, criar/reutilizar um índice e comparar métodos de busca. Geração de respostas e escolha de modelos locais ou APIs virão depois. Respostas, prazos e requisitos deverão ser conferidos na fonte oficial, especialmente se o edital tiver atualizações ou retificações.
