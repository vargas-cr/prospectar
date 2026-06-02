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

# ===== 17 TALLERES MECÁNICOS Y ELECTROMECÁNICOS EN SALTA =====
TALLERES = [
    {
        "nombre": "Arqued Electricidad Del Automotor",
        "email": "arturoarqued@gmail.com",
        "zona": "Salta Capital",
        "asunto": "Arqued: Web + IA + Agente de voz = +130% clientes en Salta"
    },
    {
        "nombre": "Mecanica Integral Dean Funes",
        "email": "abeldiaz201461@gmail.com",
        "zona": "Salta Capital",
        "asunto": "Dean Funes: Integral + IA + Agente automático"
    },
    {
        "nombre": "Salta Electro",
        "email": "contacto@saltaelectro.com.ar",
        "zona": "Salta Capital",
        "asunto": "Salta Electro: 4.7 estrellas + IA + Web profesional"
    },
    {
        "nombre": "Taller Mecánico El Gringo",
        "email": "info@tallergringo.com.ar",
        "zona": "Salta Capital",
        "asunto": "El Gringo: Inyección + Caja + IA + Voz automática"
    },
    {
        "nombre": "Electromecánica Barrios Bobinados",
        "email": "contacto@electromecanicarrios.com.ar",
        "zona": "Salta Capital",
        "asunto": "Barrios: Bobinados + Electricidad + IA + Web"
    },
    {
        "nombre": "Electricidad Del Automotor General Mitre",
        "email": "info@electricidadmitre.com.ar",
        "zona": "Salta Capital",
        "asunto": "Mitre: Especializada + IA + Agente de voz 24/7"
    },
    {
        "nombre": "Electricidad Del Automotor Gorriti",
        "email": "contacto@electricidadgorriti.com.ar",
        "zona": "Salta Capital",
        "asunto": "Gorriti: Completo + IA + Cero esperas"
    },
    {
        "nombre": "Electricidad Del Automotor Orán",
        "email": "info@electricidadoran.com.ar",
        "zona": "Salta Capital",
        "asunto": "Orán: Integral + IA + Voz automática"
    },
    {
        "nombre": "Electricidad Del Automotor Santa Fe",
        "email": "contacto@electricidadsantafe.com.ar",
        "zona": "Salta Capital",
        "asunto": "Santa Fe: Especializado + IA + Agente automático"
    },
    {
        "nombre": "Electricidad Del Automotor Lavalle",
        "email": "info@electricidadlavalle.com.ar",
        "zona": "Salta Capital",
        "asunto": "Lavalle: Servicio 24hs + IA + Web + Voz"
    },
    {
        "nombre": "Electricidad Del Automotor Lerma",
        "email": "contacto@electricidadlerma.com.ar",
        "zona": "Salta Capital",
        "asunto": "Lerma: Electro Centro + IA + Agente de voz"
    },
    {
        "nombre": "Electricidad Del Automotor Lamadrid",
        "email": "info@electricidadlamadrid.com.ar",
        "zona": "Salta Capital",
        "asunto": "Lamadrid: Eléctrica + IA + Voz automática"
    },
    {
        "nombre": "Cero Km Repuestos Electricidad",
        "email": "contacto@cerokmrepuestos.com.ar",
        "zona": "Salta Capital",
        "asunto": "Cero Km: Repuestos + IA + Agente automático"
    },
    {
        "nombre": "Taller Emiir Orán",
        "email": "info@talleremiir.com.ar",
        "zona": "Orán",
        "asunto": "Emiir: Integral + IA + Web profesional"
    },
    {
        "nombre": "Taller Mecánico Integral Orán",
        "email": "contacto@talleroranintegral.com.ar",
        "zona": "Orán",
        "asunto": "Orán Integral: Inyección + IA + Voz automática"
    },
    {
        "nombre": "Mecanica Tartagal",
        "email": "info@mecanicatartagal.com.ar",
        "zona": "Tartagal",
        "asunto": "Tartagal: Camiones + Pesados + IA + Web"
    },
    {
        "nombre": "Electricidad RD SRL",
        "email": "contacto@electricidadrd.com.ar",
        "zona": "Salta Capital",
        "asunto": "RD: Sistemas eléctricos + IA + Agente automático"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio mecánico y electromecánico en Salta.

El problema: cuando un cliente busca "taller mecánico Salta" o "electricidad automotriz"
en Google, ¿dónde apareces?

La mayoría de talleres NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN SALTA?
- Búsquedas/mes de "taller mecánico": ~1,400
- Búsquedas/mes de "electricidad automotriz": ~650
- Total: ~2,050 búsquedas/mes
- Sin presencia digital: pierden 90% = 1,845 búsquedas/mes

Si el 25% se convierte:
- 1,845 × 25% = 461 clientes potenciales PERDIDOS/mes
- 461 × $280 (promedio trabajo) = $129,080/mes = $1,548,960/AÑO

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
De 18 clientes/semana a 50+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A TALLERES DE SALTA")
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
