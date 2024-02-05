from art import tprint
from gtts import gTTS
from pathlib import Path
import pdfplumber


def pdf_to_mp3(file_path, language='en'):
    if not Path(file_path).is_file():
        raise FileNotFoundError('File does not exist')
    if not Path(file_path).suffix == '.pdf':
        raise ValueError('The file is not a PDF')

    print(f'\nConverting {Path(file_path).name} to mp3')
    print('File processing...')

    with pdfplumber.PDF(open(file_path, 'rb')) as pdf:
        pages = [page.extract_text() for page in pdf.pages]

    text = ''.join(pages)
    text = text.replace('\n', '')

    audio = gTTS(text=text, lang=language)
    file_name = Path(file_path).stem
    audio.save(f'mp3_files/{file_name}.mp3')

    return f'{file_name}.mp3 successfully saved in "mp3_files"'


def main():
    tprint('PDF TO MP3', font='bulbhead')
    file_path = input('\nEnter the path of the pdf file: ')
    language = input('Choose language, for example "en" or "ru": ')
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()