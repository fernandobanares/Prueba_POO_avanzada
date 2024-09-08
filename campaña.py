from datetime import date
from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoException, SubTipoInvalidoException


class Campaña():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, datos_anuncios: tuple = ()) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []
        
        for datos in datos_anuncios:
            anuncio = self._crear_anuncio(datos)
            self.__anuncios.append(anuncio)
            
    def _crear_anuncio(self, datos: dict) -> Anuncio:
        tipo = datos.get("tipo")
        if tipo == "Video":
            return Video(datos["titulo"], datos["duracion"])
        elif tipo == "Display":
            return Display(datos["titulo"], datos["imagen"])
        elif tipo == "Social":
            return Social(datos["titulo"], datos["red_social"])
        else:
             raise SubTipoInvalidoException(f"Subtipo de anuncio desconocido: {tipo}")
            
            
    def __str__(self) -> str:
        tipos_anuncios = {"Video": 0, "Display": 0, "Social": 0}

        for anuncio in self.__anuncios:
            if isinstance(anuncio, Video):
                tipos_anuncios["Video"] += 1
            elif isinstance(anuncio, Display):
                tipos_anuncios["Display"] += 1
            elif isinstance(anuncio, Social):
                tipos_anuncios["Social"] += 1

        return (f"Nombre de la campaña: {self.__nombre}\n"
                f"Anuncios: {tipos_anuncios['Video']} Video, "
                f"{tipos_anuncios['Display']} Display, "
                f"{tipos_anuncios['Social']} Social")
    
    def agregar_anuncio(self, anuncio: Anuncio):
        if not isinstance(anuncio, Anuncio):
            raise TypeError("Debe agregarse una instancia de la clase Anuncio o sus subclases.")
        self.__anuncios.append(anuncio)
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if len(self.__nombre) < 250:
            self.__nombre = nombre
        else:
            raise LargoExcedidoException("El nombre excede los 250 caracteres.")
        
    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str) -> None:
        self.__fecha_inicio = fecha_inicio
        
    @property
    def fecha_termino(self) -> date:
        return self.__fecha_termino
    @fecha_termino.setter
    def url_archivo(self, fecha_termino: str) -> None:
        self.__fecha_termino = fecha_termino
        
    @property
    def anuncios(self) -> list:
        return self.__anuncios
    
