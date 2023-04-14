import os
import xml.sax as sax


class TitleHandler(sax.ContentHandler):
    def __init__(self, output_file):
        super().__init__()
        self.is_title = False
        self.title = ""
        self.output_file = output_file

    def startElement(self, name, attrs):
        self.is_title = (name == "TITLE")

    def endElement(self, name):
        if name == "TITLE":
            local_title = " ".join(self.title.split()).strip() + "\n"
            self.output_file.write(local_title)
            self.is_title = False
            self.title = ""

    def characters(self, content):
        if self.is_title:
            self.title += content.strip() + " "


if __name__ == "__main__":
    data_dir = r".\data"
    output_file = r".\output\titulo.xml"

    with open(output_file, "w") as f:
        for file_name in os.listdir(data_dir):
            if file_name.endswith(".xml"):
                xml_path = os.path.join(data_dir, file_name)
                handler = TitleHandler(f)
                sax.parse(xml_path, handler)
