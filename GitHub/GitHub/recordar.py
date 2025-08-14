import time
from plyer import notification # type: ignore
from datetime import datetime

def programar_recordatorio(mensaje, hora_str, titulo="Recordatorio"):
    """
    Programa un recordatorio que se mostrará como una notificación.

    Args:
        mensaje (str): El texto del recordatorio.
        hora_str (str): La hora en formato "HH:MM" (ej. "14:30").
        titulo (str): El título de la notificación (opcional, por defecto "Recordatorio").
    """
    try:
        # Parsear la hora deseada
        hora_deseada = datetime.strptime(hora_str, "%H:%M").time()
        print(f"Recordatorio '{mensaje}' programado para las {hora_str}.")

        while True:
            ahora = datetime.now().time()
            # Si la hora actual es mayor o igual a la hora deseada, envía la notificación
            # y se asegura de que sea solo una vez por día (si el script sigue corriendo)
            if ahora.hour == hora_deseada.hour and ahora.minute == hora_deseada.minute:
                notification.notify(
                    title=titulo,
                    message=mensaje,
                    app_name="Mi Recordatorio Python",
                    timeout=10 # La notificación estará visible por 10 segundos
                )
                print(f"Notificación enviada: '{mensaje}' a las {datetime.now().strftime('%H:%M')}")
                # Espera un minuto para evitar enviar múltiples notificaciones en el mismo minuto
                time.sleep(60)
            
            # Duerme un rato para no consumir muchos recursos, y chequea cada 30 segundos
            time.sleep(30)

    except ValueError:
        print("Error: Formato de hora incorrecto. Usa HH:MM (ej. 14:30).")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    print("Iniciando el programa de recordatorios.")
    print("Para detenerlo, presioná Ctrl+C en la terminal.")
    mensaje = input("¿Cuál es el mensaje del recordatorio? ")
    hora = input("¿A qué hora? (formato HH:MM) ")
    programar_recordatorio(mensaje, hora)

