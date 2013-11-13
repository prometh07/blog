#encoding=utf-8


pl_chars = u"ąćęłńóśżźĄĆĘŁŃÓŚŻŹ"
en_chars = u"acelnoszzACELNOSZZ"
pl_to_en = dict((ord(a), b) for a, b in zip(pl_chars, en_chars))
