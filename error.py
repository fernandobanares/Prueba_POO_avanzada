class Error(Exception):
    pass

class LargoExcedidoError(Error):
    def __str__(self):
        return "El largo excede el límite permitido."

class SubTipoInvalidoException(Error):
    def __str__(self):
        return "El subtipo del anuncio es inválido."

class LargoExcedidoException(Error):
    def __str__(self):
        return "El largo del campo excede lo permitido."
