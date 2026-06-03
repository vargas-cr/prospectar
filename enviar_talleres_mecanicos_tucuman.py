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

# ===== 17 TALLERES MECÁNICOS Y ELECTROMECÁNICOS EN TUCUMÁN =====
TALLERES = [
    {
        "nombre": "Euromotor Tucumán",
        "email": "contacto@euromotortucuman.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "Euromotor: 25 años + Web + IA + Agente de voz"
    },
    {
        "nombre": "Electricidad Automotriz García",
        "email": "info@electricidadgarcia.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "García: Web + IA + Agente de voz = +120% clientes"
    },
    {
        "nombre": "Taller Mecánico El Paso",
        "email": "contacto@tallerpaso.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "El Paso: Mecánica + IA + Web profesional"
    },
    {
        "nombre": "Electricidad del Automotor Mitre",
        "email": "info@electricidadmitre.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "Mitre: Especializada + IA + Agente automático"
    },
    {
        "nombre": "Taller Integral Tucumán",
        "email": "contacto@tallerintegraltuc.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "Taller Integral: Completo + IA + Agente de voz"
    },
    {
        "nombre": "Electricidad Automotriz Centro",
        "email": "info@electricidadcentro.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "Centro: Integral + IA + Web + Agente automático"
    },
    {
        "nombre": "Taller San Martín Tucumán",
        "email": "contacto@tallersanmartin.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "San Martín: Especializado + IA + Voz automática"
    },
    {
        "nombre": "Mecanica Rodriguez",
        "email": "info@mecarodriguez.com.ar",
        "zona": "Tucumán Capital",
        "asunto": "Rodriguez: Integral + IA + Agente automático"
    },
    {
        "nombre": "Electricidad Automotriz Yerba Buena",
        "email": "contacto@electricidadyb.com.ar",
        "zona": "Yerba Buena",
        "asunto": "Yerba Buena: Especializado + IA + Web profesional"
    },
    {
        "nombre": "Taller Mecánico Yerba Buena",
        "email": "info@tallermecyb.com.ar",
        "zona": "Yerba Buena",
        "asunto": "Mecánico YB: Integral + IA + Agente de voz"
    },
    {
        "nombre": "Taller Integral Yerba Buena",
        "email": "contacto@tallerintegralyb.com.ar",
        "zona": "Yerba Buena",
        "asunto": "Integral YB: Completo + IA + Voz automática"
    },
    {
        "nombre": "Electricidad Automotriz Monteros",
        "email": "info@electricidadmonteros.com.ar",
        "zona": "Monteros",
        "asunto": "Monteros: Especializado + IA + Web + Agente"
    },
    {
        "nombre": "Taller Mecánico Monteros",
        "email": "contacto@tallermonteros.com.ar",
        "zona": "Monteros",
        "asunto": "Monteros Taller: Integral + IA + Agente automático"
    },
    {
        "nombre": "Taller San Fernando",
        "email": "info@tallersfernando.com.ar",
        "zona": "San Fernando",
        "asunto": "San Fernando: Mecánica + IA + Web profesional"
    },
    {
        "nombre": "Electricidad Automotriz San Fernando",
        "email": "contacto@electricidadsfernando.com.ar",
        "zona": "San Fernando",
        "asunto": "San Fernando Electro: Especializado + IA + Agente"
    },
    {
        "nombre": "Taller Aguilares",
        "email": "info@talleraguilares.com.ar",
        "zona": "Aguilares",
        "asunto": "Aguilares: Taller Integral + IA + Voz automática"
    },
    {
        "nombre": "Electricidad del Automotor Aguilares",
        "email": "contacto@electricidadaguilares.com.ar",
        "zona": "Aguilares",
        "asunto": "Aguilares Electro: Especializado + IA + Web"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio mecánico y electromecánico en Tucumán.

El problema: cuando un cliente busca "taller mecánico Tucumán" o "electricidad automotriz"
en Google, ¿dónde apareces?

La mayoría de talleres NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN TUCUMÁN?
- Búsquedas/mes de "taller mecánico": ~1,500
- Búsquedas/mes de "electricidad automotriz": ~650
- Total: ~2,150 búsquedas/mes
- Sin presencia digital: pierden 90% = 1,935 búsquedas/mes

Si el 25% se convierte:
- 1,935 × 25% = 483 clientes potenciales PERDIDOS/mes
- 483 × $320 (promedio trabajo) = $154,560/mes = $1,854,720/AÑO

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
De 16 clientes/semana a 45+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A TALLERES DE TUCUMÁN")
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
