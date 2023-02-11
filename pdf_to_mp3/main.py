from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path


def get_mp3(file_path, language='en'):

    if Path(file_path).is_file:  # and Path(file_path).suffix == '.pdf':

        tprint('...its working...', font='random-small')
        # for pdf
        with pdfplumber.PDF(open(file=file_path, mode='rb'))as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        # with open('txt_from_pdf.txt', 'w') as file:
        #    file.write(text)

        # for txt
        # with open(file=file_path, mode='r', encoding='utf-8') as txt:
        #    text = txt.read()

        my_audio = gTTS(text=text, lang=language,  slow=False)
        audio_name = Path(file_path).stem
        my_audio.save(f'{audio_name}.mp3')

    else:
        return 'bad file path'


def main():
    tprint('PDF >> To >> MP3', font='bulbhead')
    file_path = input('\nEnter a file path: ')
    language = input('\nChoose language, exemple en or ru : ')
    print(get_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
