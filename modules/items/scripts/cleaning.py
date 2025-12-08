import re

def normalisasi(teks: str | None) -> str:
    if not teks:
        return ""

    teks = teks.lower()
    teks = re.sub(r"http\S+|www\.\S+", " ", teks)
    teks = re.sub(r"@\w+", " ", teks)
    teks = re.sub(r"#(\w+)", r"\1", teks)
    teks = teks.replace("&amp;", " and ")

    teks = re.sub(r"[^a-z0-9.,!?()' ]+", " ", teks)

    teks = re.sub(r"\s*:\s*", ":", teks)
    teks = re.sub(r"\'s", " 's", teks)
    teks = re.sub(r"\'ve", " 've", teks)
    teks = re.sub(r"n\'t", " n't", teks)
    teks = re.sub(r"\'re", " 're", teks)
    teks = re.sub(r"\'d", " 'd", teks)
    teks = re.sub(r"\'ll", " 'll", teks)

    teks = re.sub(r",", " , ", teks)
    teks = re.sub(r"!", " ! ", teks)
    teks = re.sub(r"\(", " ( ", teks)
    teks = re.sub(r"\)", " ) ", teks)
    teks = re.sub(r"\?", " ? ", teks)
    teks = re.sub(r"\.", " . ", teks)

    teks = re.sub(r"(.)\1{2,}", r"\1\1", teks)

    teks = re.sub(r"\s+", " ", teks)
    teks = teks.strip()

    return teks
