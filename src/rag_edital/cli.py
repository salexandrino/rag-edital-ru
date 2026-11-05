"""Interface de terminal para conferir a extração de um PDF."""

import argparse
import sys

from .pdf_reader import PdfReadError, extract_pdf


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extrai e mostra uma amostra do texto de cada página de um PDF."
    )
    parser.add_argument("pdf", help="Caminho do arquivo PDF a conferir")
    parser.add_argument(
        "--sample-chars",
        type=int,
        default=500,
        help="Quantidade máxima de caracteres exibida por página (padrão: 500)",
    )
    arguments = parser.parse_args()

    if arguments.sample_chars < 1:
        parser.error("--sample-chars precisa ser maior que zero")

    try:
        result = extract_pdf(arguments.pdf)
    except PdfReadError as error:
        print(f"Erro: {error}", file=sys.stderr)
        return 2

    print(f"Arquivo: {result.file_name}")
    print(f"Total de páginas: {result.total_pages}")
    print(f"Páginas com texto extraível: {result.pages_with_text}")
    print(f"Páginas sem texto extraível: {result.pages_without_text}")

    for page in result.pages:
        print(f"\n--- Página do PDF {page.number} ---")
        if not page.has_text:
            print("[Sem texto extraível. Esta página pode exigir OCR.]")
            continue

        sample = page.text.strip()[: arguments.sample_chars]
        if len(page.text.strip()) > arguments.sample_chars:
            sample += "…"
        print(sample)

    if result.total_pages == 0 or result.pages_with_text == 0:
        print(
            "\nErro: o documento não contém texto extraível. "
            "Se as páginas forem imagens digitalizadas, será necessário OCR; "
            "esta etapa não executa OCR automaticamente.",
            file=sys.stderr,
        )
        return 2

    if result.pages_without_text:
        print(
            "\nAviso: há páginas sem texto extraível. Elas podem ser imagens "
            "e exigir OCR; esta etapa não executa OCR automaticamente."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
