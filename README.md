# md2docx

A library to convert Markdown files to DOCX format.

## Installation

pip install md2docx

## Usage

from md2docx import convert_markdown_to_docx

markdown_text = """
# Heading 1
## Heading 2

This is a paragraph.
"""

convert_markdown_to_docx(markdown_text, "output.docx")
