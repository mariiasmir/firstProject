"""""

"""""
str1 = 'the_stealth_warrior'
str2 = 'The-Stealth-Warrior'
str3 = 'A-B-C'
str4 = ''
str5 = 'to_camel_case(''the_stealth_warrior'')'


def to_camel_case(text):
    if not text:
        return "An empty string was provided but not returned"
    elif text.find('_') and text.find('-'):
        text = text.replace("_", " ").replace("-", " ")
        if text[0].islower() is True:
            text = text.title()
            text = text[0].lower() + text[1:]
            text = text.replace(" ", "")
        else:
            text = text.title()
            text = text.replace(" ", "")
        return text
    else:
        print(text + "did not return correct value")
        return


print(to_camel_case(str4))
