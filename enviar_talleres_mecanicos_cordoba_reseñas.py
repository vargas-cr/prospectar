import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# ===== TUS CREDENCIALES =====
TU_EMAIL = "argentia.ai@gmail.com"
TU_PASSWORD = "hcdmhtojksilixyc"
TU_NOMBRE = "Cristian Vargas"
TU_TELEFONO = "+54 9 1160206752"

# ===== CONFIGURACIÓN GMAIL =====
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ===== 17 TALLERES CÓRDOBA CON RESEÑAS 3.0-4.0 ESTRELLAS =====
TALLERES = [
    {
        "nombre": "Taller Mecánico Vélez",
        "email": "contacto@tallervelezcba.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.8",
        "asunto": "Vélez: 3.8⭐ + Web + IA + Agente de voz = Liderazgo digital"
    },
    {
        "nombre": "Electricidad Automotriz López",
        "email": "info@electricidadlopezcba.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.5",
        "asunto": "López: 3.5⭐ Especializada + IA + Agente automático"
    },
    {
        "nombre": "Taller San José",
        "email": "contacto@tallersanjosecba.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.9",
        "asunto": "San José: 3.9⭐ + Web + IA + Voz automática"
    },
    {
        "nombre": "Electricidad del Automotor Fernández",
        "email": "info@electricidadfernandez.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.6",
        "asunto": "Fernández: 3.6⭐ + IA + Agente automático"
    },
    {
        "nombre": "Taller Mecánico Central",
        "email": "contacto@tallercentral.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.7",
        "asunto": "Central: 3.7⭐ Integral + IA + Agente de voz"
    },
    {
        "nombre": "Servicio Eléctrico Automotor",
        "email": "info@servicioelectricocba.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.4",
        "asunto": "Servicio Eléctrico: 3.4⭐ + Web + IA"
    },
    {
        "nombre": "Taller La Esperanza",
        "email": "contacto@tallerlaesperanza.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.8",
        "asunto": "La Esperanza: 3.8⭐ + IA + Web profesional"
    },
    {
        "nombre": "Electricidad Automotriz Martínez",
        "email": "info@electricidadmartinez.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.5",
        "asunto": "Martínez: 3.5⭐ Integral + IA + Agente automático"
    },
    {
        "nombre": "Taller Rápido",
        "email": "contacto@tallerrapidocba.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.9",
        "asunto": "Rápido: 3.9⭐ 24hs + IA + Voz automática"
    },
    {
        "nombre": "Especialidad Electricidad",
        "email": "info@especialidadeleccba.com.ar",
        "zona": "Córdoba Capital",
        "reseñas": "3.6",
        "asunto": "Especialidad: 3.6⭐ + IA + Agente automático"
    },
    {
        "nombre": "Taller Mecánico Río Cuarto",
        "email": "contacto@tallerrc.com.ar",
        "zona": "Río Cuarto",
        "reseñas": "3.7",
        "asunto": "Río Cuarto: 3.7⭐ + Web + IA + Agente"
    },
    {
        "nombre": "Electricidad Río Cuarto Motors",
        "email": "info@electricidadrcmotors.com.ar",
        "zona": "Río Cuarto",
        "reseñas": "3.4",
        "asunto": "RC Motors: 3.4⭐ + IA + Web profesional"
    },
    {
        "nombre": "Taller Mecánico Villa María",
        "email": "contacto@tallervmaria.com.ar",
        "zona": "Villa María",
        "reseñas": "3.8",
        "asunto": "Villa María: 3.8⭐ Integral + IA + Agente de voz"
    },
    {
        "nombre": "Servicio Automotor Villa María",
        "email": "info@servicioautomotorvm.com.ar",
        "zona": "Villa María",
        "reseñas": "3.5",
        "asunto": "Servicio VM: 3.5⭐ Completo + IA + Agente automático"
    },
    {
        "nombre": "Taller Santa Marta",
        "email": "contacto@tallersmarta.com.ar",
        "zona": "San Francisco",
        "reseñas": "3.9",
        "asunto": "Santa Marta: 3.9⭐ + Web + IA + Voz automática"
    },
    {
        "nombre": "Electricidad San Francisco Motors",
        "email": "info@electricidadsfcmotors.com.ar",
        "zona": "San Francisco",
        "reseñas": "3.6",
        "asunto": "San Francisco: 3.6⭐ Especializado + IA + Agente"
    },
    {
        "nombre": "Taller Cosquín Especializado",
        "email": "contacto@tallercosquin.com.ar",
        "zona": "Cosquín",
        "reseñas": "3.7",
        "asunto": "Cosquín: 3.7⭐ Profesional + IA + Web + Voz"
    }
]

def obtener_cuerpo_email(nombre, reseñas, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que tienen {reseñas}⭐ en Google Maps - excelente calificación. Ya tienen la confianza de los clientes.

El próximo paso: asegurar que esos clientes que buscan online TE ENCUENTREN.

El problema: cuando un cliente busca "taller mecánico Córdoba" o "electricidad automotriz"
en Google, ¿dónde apareces?

Con {reseñas}⭐ de reputación, necesitas presencia digital para capturar esas búsquedas.

¿NÚMEROS EN CÓRDOBA?
- Búsquedas/mes de "taller mecánico": ~1,600
- Búsquedas/mes de "electricidad automotriz": ~700
- Total: ~2,300 búsquedas/mes
- Sin presencia digital: pierden 90% = 2,070 búsquedas/mes

Si el 25% se convierte:
- 2,070 × 25% = 517 clientes potenciales PERDIDOS/mes
- 517 × $310 (promedio trabajo) = $160,270/mes = $1,923,240/AÑO

SOLUCIÓN - WEB + IA + AGENTE DE VOZ:

🌐 Con tu {reseñas}⭐, falta convertir búsquedas en clientes:
1. Te encuentran en Google (web optimizada + Google Business)
2. Ven tus {reseñas}⭐ + trabajos realizados + horarios
3. Llaman
4. Agente IA contesta: "¿Es mecánica, electricidad o ambos?"
5. Especialidad identificada
6. Agente agenda cita automáticamente
7. Tú vas y trabajas

SIN PERDER LLAMADAS. SIN HORAS ADMINISTRATIVAS.

IMAGINA:
De 17 clientes/semana a 48+ clientes/semana.
Tu taller funcionando a plena capacidad.
Tu equipo enfocado solo en trabajos, no en llamadas.
Tus {reseñas}⭐ atrayendo aún más clientes.

¿Vale la pena una llamada de 15 minutos?

📱 Teléfono: {telefono}
📧 Email: argentia.ai@gmail.com
🌐 Web: https://argent-ia.com/
📸 Instagram: @argent.iar"""

    return cuerpo

def enviar_emails():
    """Envía los emails automáticamente"""

    print("="*60)
    print("📧 ENVIANDO EMAILS A TALLERES CÓRDOBA (3.0-4.0⭐)")
    print("="*60)

    enviados = 0
    fallidos = 0

    try:
        # Conecta a Gmail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(TU_EMAIL, TU_PASSWORD)

        # Envía cada email
        for taller in TALLERES:

            print(f"\n📤 Enviando a {taller['nombre']} ({taller['reseñas']}⭐) ({taller['email']})...")

            try:
                # Crea el mensaje
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = taller['email']
                mensaje['Subject'] = taller['asunto']

                # Obtiene el cuerpo personalizado
                cuerpo = obtener_cuerpo_email(taller['nombre'], taller['reseñas'], TU_TELEFONO)

                # Agrega el cuerpo
                mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

                # Envía
                server.send_message(mensaje)

                print(f"   ✅ Email enviado exitosamente")
                enviados += 1

                # Pausa pequeña para no saturar
                time.sleep(2)

            except Exception as e:
                print(f"   ❌ Error: {e}")
                fallidos += 1

        server.quit()

    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        print("Verifica que tengas credenciales correctas de Gmail")
        return

    # Resumen
    print("\n" + "="*60)
    print(f"✅ ENVIADOS: {enviados}")
    print(f"❌ FALLIDOS: {fallidos}")
    print("="*60)

    if enviados == 17:
        print("\n🎉 ¡TODOS LOS EMAILS ENVIADOS EXITOSAMENTE!")
        print("\nProximos pasos:")
        print("1. Monitorea respuestas en los próximos 2-3 días")
        print("2. Responde rápido (profesionalismo)")
        print("3. Agenda llamadas para presentar propuesta")

if __name__ == "__main__":
    # Verifica credenciales
    if TU_EMAIL == "tu_email@gmail.com":
        print("❌ CONFIGURA TUS CREDENCIALES PRIMERO")
        exit()

    # Envía
    enviar_emails()
