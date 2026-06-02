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

# ===== 17 TALLERES MECÁNICOS Y ELECTROMECÁNICOS EN CÓRDOBA =====
TALLERES = [
    {
        "nombre": "Euromotor Córdoba",
        "email": "contacto@euromotorcordoba.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "Euromotor: 28 años + Web + IA + Agente de voz"
    },
    {
        "nombre": "Electricidad Automotriz García",
        "email": "info@electricidadgarcia.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "García: Web + IA + Agente de voz = +125% clientes"
    },
    {
        "nombre": "Taller Mecánico El Paso",
        "email": "contacto@tallerpaso.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "El Paso: Mecánica + IA + Web profesional"
    },
    {
        "nombre": "Electricidad del Automotor Mitre",
        "email": "info@electricidadmitre.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "Mitre: Especializada + IA + Agente automático"
    },
    {
        "nombre": "Taller Integral Córdoba",
        "email": "contacto@tallerintegralcba.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "Taller Integral: Completo + IA + Agente de voz"
    },
    {
        "nombre": "Electricidad Automotriz Centro",
        "email": "info@electricidadcentro.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "Centro: Integral + IA + Web + Agente automático"
    },
    {
        "nombre": "Taller San Martín Córdoba",
        "email": "contacto@tallersanmartin.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "San Martín: Especializado + IA + Voz automática"
    },
    {
        "nombre": "Mecanica Rodriguez",
        "email": "info@mecarodriguez.com.ar",
        "zona": "Córdoba Capital",
        "asunto": "Rodriguez: Integral + IA + Agente automático"
    },
    {
        "nombre": "Electricidad Automotriz Río Cuarto",
        "email": "contacto@electricidadrc.com.ar",
        "zona": "Río Cuarto",
        "asunto": "Río Cuarto: Especializado + IA + Web profesional"
    },
    {
        "nombre": "Taller Mecánico Río Cuarto",
        "email": "info@tallermecrc.com.ar",
        "zona": "Río Cuarto",
        "asunto": "Mecánico RC: Integral + IA + Agente de voz"
    },
    {
        "nombre": "Taller Integral Río Cuarto",
        "email": "contacto@tallerintegralrc.com.ar",
        "zona": "Río Cuarto",
        "asunto": "Integral RC: Completo + IA + Voz automática"
    },
    {
        "nombre": "Electricidad Automotriz Villa María",
        "email": "info@electricidadvm.com.ar",
        "zona": "Villa María",
        "asunto": "Villa María: Especializado + IA + Web + Agente"
    },
    {
        "nombre": "Taller Mecánico Villa María",
        "email": "contacto@tallervm.com.ar",
        "zona": "Villa María",
        "asunto": "Villa María Taller: Integral + IA + Agente automático"
    },
    {
        "nombre": "San Francisco Taller Mecánico",
        "email": "info@tallersfco.com.ar",
        "zona": "San Francisco",
        "asunto": "San Francisco: Mecánica + IA + Web profesional"
    },
    {
        "nombre": "Electricidad Automotriz San Francisco",
        "email": "contacto@electricidadsfco.com.ar",
        "zona": "San Francisco",
        "asunto": "San Francisco Electro: Especializado + IA + Agente"
    },
    {
        "nombre": "Taller Cosquín",
        "email": "info@tallercosquin.com.ar",
        "zona": "Cosquín",
        "asunto": "Cosquín: Taller Integral + IA + Voz automática"
    },
    {
        "nombre": "Electricidad del Automotor Cosquín",
        "email": "contacto@electricidadcosquin.com.ar",
        "zona": "Cosquín",
        "asunto": "Cosquín Electro: Especializado + IA + Web"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio mecánico y electromecánico en Córdoba.

El problema: cuando un cliente busca "taller mecánico Córdoba" o "electricidad automotriz"
en Google, ¿dónde apareces?

La mayoría de talleres NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN CÓRDOBA?
- Búsquedas/mes de "taller mecánico": ~1,600
- Búsquedas/mes de "electricidad automotriz": ~700
- Total: ~2,300 búsquedas/mes
- Sin presencia digital: pierden 90% = 2,070 búsquedas/mes

Si el 25% se convierte:
- 2,070 × 25% = 517 clientes potenciales PERDIDOS/mes
- 517 × $310 (promedio trabajo) = $160,270/mes = $1,923,240/AÑO

SOLUCIÓN - WEB + IA + AGENTE DE VOZ:

🌐 Cuando buscan tu servicio:
1. Te encuentran en Google (web optimizada + Google Business)
2. Ven trabajos realizados, precios, horarios
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
Sin perder ni una oportunidad de venta.

¿Vale la pena una llamada de 15 minutos?

📱 Teléfono: {telefono}
📧 Email: argentia.ai@gmail.com
🌐 Web: https://argent-ia.com/
📸 Instagram: @argent.iar"""

    return cuerpo

def enviar_emails():
    """Envía los emails automáticamente"""

    print("="*60)
    print("📧 ENVIANDO EMAILS A TALLERES DE CÓRDOBA")
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

            print(f"\n📤 Enviando a {taller['nombre']} ({taller['email']})...")

            try:
                # Crea el mensaje
                mensaje = MIMEMultipart()
                mensaje['From'] = TU_EMAIL
                mensaje['To'] = taller['email']
                mensaje['Subject'] = taller['asunto']

                # Obtiene el cuerpo personalizado
                cuerpo = obtener_cuerpo_email(taller['nombre'], TU_TELEFONO)

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
