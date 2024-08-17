def latindan_crill(text):
    replacements = {
        "a": "а", "b": "б", "v": "в", "g": "г", "d": "д",
        "e": "е", "yo": "ё", "j": "ж", "z": "з", "i": "и",
        "y": "й", "k": "к", "l": "л", "m": "м", "n": "н",
        "o": "о", "p": "п", "r": "р", "s": "с", "t": "т",
        "u": "у", "f": "ф", "x": "х", "ts": "ц", "ch": "ч",
        "sh": "ш", "sch": "щ", "yu": "ю", "ya": "я",
        "A": "А", "B": "Б", "V": "В", "G": "Г", "D": "Д",
        "E": "Е", "Yo": "Ё", "J": "Ж", "Z": "З", "I": "И",
        "Y": "Й", "K": "К", "L": "Л", "M": "М", "N": "Н",
        "O": "О", "P": "П", "R": "Р", "S": "С", "T": "Т",
        "U": "У", "F": "Ф", "X": "Х", "Ts": "Ц", "Ch": "Ч",
        "Sh": "Ш", "Sch": "Щ", "Yu": "Ю", "Ya": "Я",
        # Add 'h' to 'ҳ' mapping if needed
        "h": "ҳ", "H": "Ҳ"
    }
    # To ensure 'h' is replaced correctly, process in a specific order if necessary
    for latin, crill in replacements.items():
        text = text.replace(latin, crill)
    return text

def latindan_arab(text):
    replacements = {
        "a": "ا", "b": "ب", "v": "ڤ", "g": "غ", "d": "د",
        "e": "ﻩ", "j": "ج", "z": "ز", "i": "ى", "y": "ي",
        "k": "ك", "l": "ل", "m": "م", "n": "ن", "o": "و",
        "p": "پ", "r": "ر", "s": "س", "t": "ت", "u": "و",
        "f": "ف", "x": "خ", "ch": "چ", "sh": "ش", "q": "ق",
        "h": "ه",  # Add mapping for 'h'
    }
    for latin, arab in replacements.items():
        text = text.replace(latin, arab)
    return text

def latindan_kores(text):
    replacements = {
        "a": "아", "b": "ㅂ", "v": "ㅍ", "g": "ㄱ", "d": "ㄷ",
        "e": "에", "j": "ㅈ", "z": "ㅈ", "i": "이", "y": "ㅣ",
        "k": "ㅋ", "l": "ㄹ", "m": "ㅁ", "n": "ㄴ", "o": "오",
        "p": "ㅍ", "r": "ㄹ", "s": "ㅅ", "t": "ㅌ", "u": "우",
        "f": "ㅍ", "x": "ㅅ", "ch": "ㅊ", "sh": "ㅅ",  # Replace 'sh' with 'ㅅ' for Korean
        "h": "ㅎ"  # Add mapping for 'h'
    }
    for latin, kores in replacements.items():
        text = text.replace(latin, kores)
    return text

