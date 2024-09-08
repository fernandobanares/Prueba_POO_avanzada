from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self._ancho = ancho if ancho > 0 else 1
        self._alto = alto if alto > 0 else 1
        self._url_archivo = url_archivo
        self._url_clic = url_clic
        self._sub_tipo = sub_tipo
        
    @property
    def ancho(self) -> int:
        return self._ancho
    @ancho.setter
    def ancho(self, ancho: int) -> None:
        if ancho > 0:
            self._ancho = ancho
        else:
            self._ancho = 1
            
    @property
    def alto(self) -> int:
        return self._alto
    @alto.setter
    def alto(self, alto: int) -> None:
        if alto > 0:
            self._alto = alto
        else:
            self._alto = 1
    
    @property
    def url_archivo(self) -> str:
        return self._url_archivo
    @url_archivo.setter
    def url_archivo(self, url_archivo: str) -> None:
        self._url_archivo = url_archivo
            
    @property
    def url_clic(self) -> str:
        return self._url_clic
    @url_clic.setter
    def url_clic(self, url_clic: str) -> None:
        self._url_clic = url_clic
    
    @property
    def sub_tipo(self) -> str:
        return self._sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str):
        if sub_tipo in self.SUB_TIPOS:
            self._sub_tipo = sub_tipo
        else:
            raise SubTipoInvalidoException(f"El subtipo {sub_tipo} no es válido para {self.__class__.__name__}.")

    @staticmethod        
    def mostrar_formatos():
        for subtipo in Anuncio.SUB_TIPOS:
            print(f"- {subtipo}")
    @abstractmethod
    def comprimir_anuncio() -> None:
        pass
    @abstractmethod
    def redimensionar_anuncio() -> None:
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    
    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(ancho=1, alto=1, url_archivo=url_archivo, url_clic=url_clic, sub_tipo=sub_tipo)
        self._duracion = duracion if duracion > 0 else 5
    @property
    def ancho(self) -> int:
        return 1
    @ancho.setter
    def ancho(self, ancho: int) -> None:
        pass

    @property
    def alto(self) -> int:
        return 1
    @alto.setter
    def alto(self, alto: int) -> None:
        pass 
      
    @property
    def duracion(self):
        return self.duracion
    @duracion.setter
    def duracion(self, duracion):
        if self.duracion > 0:
            self._duracion = duracion
        else:
            self._duracion = 5
            
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")
    
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

