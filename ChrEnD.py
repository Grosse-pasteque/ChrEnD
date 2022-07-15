from typing import Optional, Union, Tuple, List

CONV = {
    "%c": "d", # -> actual char
    "%w": "e", # -> all the text passed
    "%l": "f"  # -> last char
}
OPERATORS = {
    "+": "-",
    "-": "+",
    "*": "/",
    "/": "*",
    "**": "** (1 / %n)",
    "<<": ">>",
    ">>": "<<",
    "~": "~",
    "^": "^"
    # "%", "//", "&", "|" -> ignored
}

ModifiersType = Optional[List[Tuple[str, Union[int, str]]]]


def seed(
    turns:     Optional[int] = 0,
    modifiers: ModifiersType = []
):
    s = str(turns)
    for op, n in modifiers:
        n = n if isinstance(n, int) else CONV[n]
        s += f"a{n}b{list(OPERATORS).index(op)}"
    return "0x" + s


def unseed(s: Union[str, int]):
    if not isinstance(s, str):
        s = hex(int(s))
    if "a" in s:
        parts = s[2:].split("a")
        turns = int(parts.pop(0))
        modifiers = []
        for p in parts:
            n, op = p.split("b")
            modifiers.append(
                (list(OPERATORS)[int(op)], int(n) if isinstance(n, int) else n)
            )
        return turns, modifiers
    return int(s[2:]), []


def invert(modifiers: list):
    return [
        (OPERATORS[op], n)
        for op, n in modifiers
        if op in OPERATORS
    ][::-1]


def apply_mod(
    chro:      int,
    modifiers: ModifiersType = [],
    word_len:  Optional[int] = 0,
    last_chro: Optional[int] = 0
):
    conv = {"d": chro, "e": word_len, "f": last_chro}
    for op, n in modifiers:
        if n in conv:
            n = conv[n]
        if "%n" not in op:
            op += "%n"
        chro = eval(f"{chro}{op.replace('%n', str(n))}")
    return chro


def transform(text: str):
    return "".join(
        chr(int(chro))
        for chro in text.split(".")
    )


def untransform(text: str):
    return ".".join(
        str(ord(char))
        for char in text
    )


def encrypt(
    text:       str, 
    turns:      Optional[int] = 0,
    modifiers:  ModifiersType = [],
    get_layers: Optional[bool] = False,
    seed:       Optional[Union[str, int]] = None
):
    if seed:
        turns, modifiers = unseed(seed)

    org_text = text
    encrypted = text
    text = list(text)
    layers = [org_text, text, []]

    for i in range(turns):
        layer = []
        last = 0
        
        for char in text:
            chro = ord(char)
            layer.append(str(apply_mod(
                chro,
                modifiers,
                word_len=len(org_text),
                last_chro=last
            )))
            last = chro
        
        encrypted = ".".join(layer)
        layers[2].append(encrypted)
        text = list(encrypted)

    if get_layers:
        return encrypted, layers
    return encrypted


def decrypt(
    text:       str,
    turns:      Optional[int] = 0,
    modifiers:  ModifiersType = [],
    get_layers: Optional[bool] = False,
    seed:       Optional[Union[str, int]] = None
):
    if seed:
        turns, modifiers = unseed(seed)
        modifiers = invert(modifiers)

    org_text = text
    decrypted = text
    text = text.split(".")
    layers = [org_text, text, []]

    for i in range(turns):
        decrypted = ""
        last = 0

        for chro in text:
            char = int(apply_mod(
                int(chro),
                modifiers,
                word_len=len(org_text),
                last_chro=last
            ))
            decrypted += chr(char)
            last = char

        layers[2].append(decrypted)
        text = decrypted.split(".")

    if get_layers:
        return decrypted, layers
    return decrypted


def combinations(
    turns:         Optional[int] = 1,
    nmodifiers:    Optional[int] = 0,
    encoding_size: Optional[int] = 128
):
    return (((encoding_size + 3) * len(OPERATORS))) ** nmodifiers * turns
