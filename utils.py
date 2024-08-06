import pycountry


def translate_iso_639_1_to_639_3(iso_639_1_code) -> str | None:
    """
    Translates an ISO 639-1 code to an ISO 639-3 code.

    Args:
    iso_639_1_code (str): The ISO 639-1 language code.

    Returns:
    str: The corresponding ISO 639-3 language code, or None if not found.
    """
    try:
        language = pycountry.languages.get(alpha_2=iso_639_1_code)
        return language.alpha_3
    except AttributeError:
        return None


def translate_iso_639_3_to_full_name(iso_639_3_code) -> str | None:
    """
    Translates an ISO 639-3 code to the full language name.

    Args:
    iso_639_3_code (str): The ISO 639-3 language code.

    Returns:
    str: The full language name, or None if not found.
    """
    try:
        language = pycountry.languages.get(alpha_3=iso_639_3_code)
        return language.name
    except AttributeError:
        return None
