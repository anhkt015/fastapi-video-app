import imagehash
from PIL import Image
from services.ocr_engine import ocr_image
import difflib

def normalize_text(text):
    return (
        text.lower()
        .replace(" ", "")
        .replace("\n", "")
        .replace(".", "")
        .replace(",", "")
        .replace(":", "")
        .replace(";", "")
    )

def is_similar(text1, text2, threshold=0.9):
    return difflib.SequenceMatcher(None, text1, text2).ratio() > threshold

def filter_unique_images(image_paths, hash_threshold=8, text_similarity=0.9):
    hashes = []
    texts = []
    unique = []

    for path in image_paths:
        img = Image.open(path)
        raw_text = ocr_image(path)
        norm_text = normalize_text(raw_text)

        phash = imagehash.phash(img)
        dhash = imagehash.dhash(img)

        is_hash_duplicate = any(
            abs(phash - h[0]) < hash_threshold and abs(dhash - h[1]) < hash_threshold
            for h in hashes
        )

        is_text_duplicate = any(is_similar(norm_text, t, text_similarity) for t in texts)

        if not is_hash_duplicate and not is_text_duplicate:
            hashes.append((phash, dhash))
            texts.append(norm_text)
            unique.append((path, raw_text))

    return unique
