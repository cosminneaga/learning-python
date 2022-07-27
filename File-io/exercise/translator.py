from translate import Translator

translator = Translator(to_lang="ja")

try:

    with open('File-io\\sample.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        with open('File-io\\sample-ja.txt', mode="w", encoding="utf-8") as file:
            file.write(translation)

except FileNotFoundError as e:
    print(e)
