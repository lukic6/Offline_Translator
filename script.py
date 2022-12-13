from translate import Translator

translator = Translator(to_lang="sl")

try:
    with open("test.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open("./test-sl.txt", mode="w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("FileNotFoundError; Changing file path should resolve this issue :D")
