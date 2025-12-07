from langdetect import detect
import re
import nltk
from nltk.corpus import words

# Download word list jika belum ada
nltk.download('words')

english_vocab = set(words.words())

def validate_english_text_strict(text: str):
    """
    STRICT VALIDATION:
    - Must be English language (langdetect)
    - Only English ASCII characters
    - Every word must be in English dictionary
    """

    # --- 1. CEK PANJANG ---
    if len(text.strip()) < 3:
        return False, "Text is too short."

    # --- 2. DETEKSI BAHASA ---
    try:
        lang = detect(text)
    except:
        return False, "Unable to detect language."

    if lang != "en":
        return False, "Only English sentences are allowed."

    # --- 3. CEK KARAKTER NON-ENGLISH ---
    if not re.fullmatch(r"[A-Za-z0-9\s.,!?':;\"()\-]+", text):
        return False, "Text contains unsupported characters."

    # --- 4. CEK KAMUS ENGLISH ---
    words_in_text = re.findall(r"[A-Za-z]+", text.lower())

    for w in words_in_text:
        if w not in english_vocab:
            return False, f"Word '{w}' is not recognized as English."

    return True, ""
