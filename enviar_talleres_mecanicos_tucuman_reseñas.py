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

# ===== 17 TALLERES TUCUMÁN CON RESEÑAS 3.0-4.0 ESTRELLAS =====
TALLERES = [
    {
        "nombre": "Taller Mecánico Vélez",
        "email": "contacto@tallerveletuc.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.8",
        "asunto": "Vélez: 3.8⭐ + Web + IA + Agente de voz = Liderazgo digital"
    },
    {
        "nombre": "Electricidad Automotriz López",
        "email": "info@electricidadlopeztuc.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.5",
        "asunto": "López: 3.5⭐ Especializada + IA + Agente automático"
    },
    {
        "nombre": "Taller San José",
        "email": "contacto@tallersanjose.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.9",
        "asunto": "San José: 3.9⭐ + Web + IA + Voz automática"
    },
    {
        "nombre": "Electricidad del Automotor Fernández",
        "email": "info@electricidadfernandez.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.6",
        "asunto": "Fernández: 3.6⭐ + IA + Agente automático"
    },
    {
        "nombre": "Taller Mecánico Central",
        "email": "contacto@tallercentral.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.7",
        "asunto": "Central: 3.7⭐ Integral + IA + Agente de voz"
    },
    {
        "nombre": "Servicio Eléctrico Automotor",
        "email": "info@servicioelectricotuc.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.4",
        "asunto": "Servicio Eléctrico: 3.4⭐ + Web + IA"
    },
    {
        "nombre": "Taller La Esperanza",
        "email": "contacto@tallerlaesperanza.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.8",
        "asunto": "La Esperanza: 3.8⭐ + IA + Web profesional"
    },
    {
        "nombre": "Electricidad Automotriz Martínez",
        "email": "info@electricidadmartinez.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.5",
        "asunto": "Martínez: 3.5⭐ Integral + IA + Agente automático"
    },
    {
        "nombre": "Taller Rápido",
        "email": "contacto@tallerrapido.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.9",
        "asunto": "Rápido: 3.9⭐ Urgentes + IA + Voz automática"
    },
    {
        "nombre": "Especialidad Electricidad",
        "email": "info@especialidadelec.com.ar",
        "zona": "Tucumán Capital",
        "reseñas": "3.6",
        "asunto": "Especialidad: 3.6⭐ 24hs + IA + Agente automático"
    },
    {
        "nombre": "Taller Tucumán",
        "email": "contacto@tallertucuman.com.ar",
        "zona": "Yerba Buena",
        "reseñas": "3.7",
        "asunto": "Taller YB: 3.7⭐ + Web + IA + Agente"
    },
    {
        "nombre": "Electricidad YB Motors",
        "email": "info@electricidadybmotors.com.ar",
        "zona": "Yerba Buena",
        "reseñas": "3.4",
        "asunto": "YB Motors: 3.4⭐ + IA + Web profesional"
    },
    {
        "nombre": "Taller Mecánico Sol",
        "email": "contacto@tallersol.com.ar",
        "zona": "Monteros",
        "reseñas": "3.8",
        "asunto": "Sol: 3.8⭐ Integral + IA + Agente de voz"
    },
    {
        "nombre": "Servicio Automotor Monteros",
        "email": "info@servicioautomotormonteros.com.ar",
        "zona": "Monteros",
        "reseñas": "3.5",
        "asunto": "Monteros: 3.5⭐ Completo + IA + Agente automático"
    },
    {
        "nombre": "Taller Santa Clara",
        "email": "contacto@tallersantaclara.com.ar",
        "zona": "San Fernando",
        "reseñas": "3.9",
        "asunto": "Santa Clara: 3.9⭐ + Web + IA + Voz automática"
    },
    {
        "nombre": "Electricidad San Fernando Motors",
        "email": "info@electricidadsanfernandomtrs.com.ar",
        "zona": "San Fernando",
        "reseñas": "3.6",
        "asunto": "San Fernando: 3.6⭐ Especializado + IA + Agente"
    },
    {
        "nombre": "Taller Aguilares Especializado",
        "email": "contacto@talleraguilaresesp.com.ar",
        "zona": "Aguilares",
        "reseñas": "3.7",
        "asunto": "Aguilares: 3.7⭐ Profesional + IA + Web + Voz"
    }
]

def obtener_cuerpo_email(nombre, reseñas, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que tienen {reseñas}⭐ en Google Maps - excelente calificación. Ya tienen la confianza de los clientes.

El próximo paso: asegurar que esos clientes que buscan online TE ENCUENTREN.

El problema: cuando un cliente busca "taller mecánico Tucumán" o "electricidad automotriz"
en Google, ¿dónde apareces?

Con {reseñas}⭐ de reputación, necesitas presencia digital para capturar esas búsquedas.

¿NÚMEROS EN TUCUMÁN?
- Búsquedas/mes de "taller mecánico": ~1,500
- Búsquedas/mes de "electricidad automotriz": ~650
- Total: ~2,150 búsquedas/mes
- Sin presencia digital: pierden 90% = 1,935 búsquedas/mes

Si el 25% se convierte:
- 1,935 × 25% = 483 clientes potenciales PERDIDOS/mes
- 483 × $320 (promedio trabajo) = $154,560/mes = $1,854,720/AÑO

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
De 16 clientes/semana a 45+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A TALLERES TUCUMÁN (3.0-4.0⭐)")
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
