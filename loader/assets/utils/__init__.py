import os

from lxml import etree  # ty: ignore[unresolved-import]


def create_xml_parser() -> etree.XMLParser:
    return etree.XMLParser(recover=True, encoding=os.environ.get("FORCE_PARSER_ENCODING"), remove_comments=True)
