from translate import Translator

# Create a Translator instance
translator = Translator(to_lang="zh-TW")

try:
    with open('./untranslated_words.txt', mode='r') as my_file:
        with open('./translated-zh-tw.txt', mode='w') as my_file2:
            while True:
                # Read a chunk of text (up to 500 characters) from the file
                chunk = my_file.read(500)
                if not chunk:
                    # End of file reached
                    break

                # Translate the chunk
                translation = translator.translate(chunk)

                # Write the translated text in lines of 50 characters each
                for i in range(0, len(translation), 50):
                    line = translation[i:i + 50]
                    my_file2.write(line + '\n')

except FileNotFoundError as err:
    print('File does not exist')
    raise err
