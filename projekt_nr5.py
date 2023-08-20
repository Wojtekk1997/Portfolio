import click
from lxml import html
import requests


def extract(page_content, xpath):
    """Accepts page_content as a string and xpath as a string and returns matching elements as a list of strigs."""

    tree = html.fromstring(page_content)
    elements = tree.xpath(xpath)
    elements = [e.text_content() for e in elements]
    stripped = [e.strip().replace('\n', ' ') for e in elements]
    return stripped


@click.command()
@click.argument('url')
@click.argument('xpath')
def main(url, xpath):
    page = requests.get(url)
    content = page.text
    elements = extract(content, xpath)
    for element in elements:
        print(element)


if __name__ == '__main__':
    main()
