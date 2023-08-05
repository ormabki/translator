from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    api_key = "YOUR_GOOGLE_CLOUD_API_KEY"  # Replace with your actual API key
    text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'es' for Spanish, 'fr' for French): ")

    try:
        translated_text = translate_text(text, target_language)
        print(f"Translated text: {translated_text}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
