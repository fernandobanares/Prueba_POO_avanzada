from campaña import Campaña
from anuncio import Video
from datetime import date
from error import SubTipoInvalidoException
try:
    C1 = Campaña("campaña1", date(2024,9,1), date(2024,12,1))
    anuncio_video = Video(url_archivo="video.mp4", url_clic="http://fernando.com", sub_tipo="instream", duracion=30)
    C1.agregar_anuncio(anuncio_video)

    print("Campaña original: \n")
    print(C1)

    nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: \n")
    C1.nombre = nuevo_nombre

    nuevo_sub_tipo = input("Ingrese un nuevo sub_tipo para la campaña: \n")
    C1.anuncios[0].sub_tipo = nuevo_sub_tipo

    print("\nCampaña actualizada:")
    print(C1)
    
except SubTipoInvalidoException as e:
    print(f"Error: {e}")
    with open("error.log", "a+") as error_log:
        error_log.write(f"{e}\n")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
    with open("error.log", "a+") as error_log:
        error_log.write(f"Error inesperado: {e}\n")

