import os
import xml.dom.minidom as minidom


class XmlDomParser:
    def __init__(self):
        self.authors = []

    def get_authors_from_file(self, input_path):
        document = minidom.parse(input_path)
        self.authors = self.authors + [author.firstChild.data for author in document.getElementsByTagName('AUTHOR')]

    def write_authors_to_file(self, output_path):
        local_authors = list(set(self.authors))
        local_authors.sort()
        with open(output_path, 'w') as file:
            for author in local_authors:
                file.write(f"{author}\n")
        print(f"Authors saved to file {output_path}")


path = r'.\data'
dom_parser = XmlDomParser()
for file_name in os.listdir(path):
    if file_name.endswith('.xml'):
        xml_path = os.path.join(path, file_name)
        dom_parser.get_authors_from_file(xml_path)

authors_file = r'.output\autores.xml'
with open(authors_file, 'w') as f:
    dom_parser.write_authors_to_file(authors_file)
