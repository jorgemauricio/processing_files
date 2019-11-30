# libraries
import zipfile
from dbfread import DBF

def main():


with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)

for record in DBF('file.dbf'):
    print(record)


if __name__ == '__main__':
    main()
