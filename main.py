import PyPDF2
import pyttsx3

pdfreader = PyPDF2.PdfReader('book.pdf')

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

    # Zapisuje każdą stronę do oddzielnego pliku .mp3
    engine = pyttsx3.init()
    engine.save_to_file(clean_text, "story_page_{}.mp3".format(page_num))
    engine.runAndWait()
    engine.stop()
