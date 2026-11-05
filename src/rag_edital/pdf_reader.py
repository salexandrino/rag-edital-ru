"""Leitura de texto por página de um arquivo PDF."""

from dataclasses import dataclass
from pathlib import Path

try:
    import pymupdf
except ModuleNotFoundError as error:
    if error.name != "pymupdf":
        raise
    pymupdf = None


class PdfReadError(Exception):
    """Erro compreensível ao validar ou ler o PDF de entrada."""


@dataclass
class ExtractedPage:
    """Texto extraído e posição da página no arquivo PDF."""

    number: int
    text: str

    @property
    def has_text(self) -> bool:
        return bool(self.text.strip())


@dataclass
class PdfExtraction:
    """Resultado da extração, preservando a ordem e os números das páginas."""

    file_name: str
    pages: list[ExtractedPage]

    @property
    def total_pages(self) -> int:
        return len(self.pages)

    @property
    def pages_with_text(self) -> int:
        return sum(page.has_text for page in self.pages)

    @property
    def pages_without_text(self) -> int:
        return self.total_pages - self.pages_with_text


def extract_pdf(pdf_path: str | Path) -> PdfExtraction:
    """Extrai o texto de cada página; os números começam em 1."""

    if pymupdf is None:
        raise PdfReadError(
            "PyMuPDF não está instalado no Python ativo. Ative o ambiente "
            "virtual do projeto e execute: pip install -r requirements.txt"
        )

    path = Path(pdf_path).expanduser()
    if not path.exists():
        raise PdfReadError(f"Arquivo não encontrado: {path}")
    if not path.is_file():
        raise PdfReadError(f"O caminho informado não é um arquivo: {path}")
    if path.suffix.lower() != ".pdf":
        raise PdfReadError(f"O arquivo não tem extensão .pdf: {path.name}")

    try:
        with pymupdf.open(path) as document:
            if document.needs_pass:
                raise PdfReadError(
                    "O PDF está protegido por senha. Esta versão não solicita "
                    "nem tenta descobrir a senha."
                )

            # A página impressa pode ter outra numeração; aqui guardamos a
            # posição real da folha no arquivo, começando em 1.
            pages = [
                ExtractedPage(number=page_index + 1, text=page.get_text("text"))
                for page_index, page in enumerate(document)
            ]
    except PdfReadError:
        raise
    except Exception as error:
        raise PdfReadError(
            "Não foi possível abrir o PDF. Verifique se o arquivo é um PDF "
            "válido, não está danificado e pode ser lido. "
            f"Detalhe técnico: {error}"
        ) from error

    return PdfExtraction(file_name=path.name, pages=pages)
