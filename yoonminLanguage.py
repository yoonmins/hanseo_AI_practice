from methodLanguage import Language

class FranchLanguage(Language):
    default_language="프랑스어"
class JapaneseLanguage(Language):
    default_language="일본어"
class KoreaLanguage(Language):
    default_language="한국어"
a=KoreaLanguage.class_my_language()
b=JapaneseLanguage.static_my_language()
c=FranchLanguage.static_my_language()
a.print_language()
b.print_language()
c.print_language()