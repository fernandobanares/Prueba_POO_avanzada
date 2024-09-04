from datetime import date
from anuncio import Anuncio
from error import LargoExcedidoException


class Campaña():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date) -> None:
        self._nombre = nombre
        self._fecha_inicio = fecha_inicio
        self._fecha_termino = fecha_termino
        self.anuncios = []
        
    def __str__(self) -> str:
        return (f"Campaña: {self._nombre}\n"
                f"Fecha de inicio: {self.fecha_inicio}\n"
                f"Fecha de término: {self.fecha_termino}\n"
                f"Anuncios: {len(self.anuncios)}")
    
    def agregar_anuncio(self, anuncio: Anuncio):
        if not isinstance(anuncio, Anuncio):
            raise TypeError("Debe agregarse una instancia de la clase Anuncio o sus subclases.")
        self.anuncios.append(anuncio)
    
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if len(self._nombre) < 250:
            self._nombre = nombre
        else:
            raise LargoExcedidoException
        
    @property
    def fecha_inicio(self) -> date:
        return self._fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str) -> None:
        self._fecha_inicio = fecha_inicio
        
    @property
    def fecha_termino(self) -> str:
        return self._fecha_termino
    @fecha_termino.setter
    def url_archivo(self, fecha_termino: str) -> None:
        self._fecha_termino = fecha_termino
