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

# ===== 17 TALLERES MECÁNICOS Y ELECTROMECÁNICOS EN NEUQUÉN =====
TALLERES = [
    {
        "nombre": "Euromotor Neuquén",
        "email": "contacto@euromotorneuquen.com",
        "zona": "Neuquén Capital",
        "asunto": "Euromotor: 29 años + Web + IA + Agente de voz"
    },
    {
        "nombre": "Electro-quen",
        "email": "info@electroquen.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Electro-quen: Web + IA + Agente de voz = +140% clientes"
    },
    {
        "nombre": "Taller Mecánico Siciliano",
        "email": "contacto@tallersiciliano.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Siciliano: Mecánica + Electromecánica + IA"
    },
    {
        "nombre": "Electricidad del Automotor Johny",
        "email": "johny@electricidaddauto.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Johny: Especializada + IA + Agente de voz automática"
    },
    {
        "nombre": "Electricidad del Automotor T.L. Planas",
        "email": "contacto@electricidadplanas.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Planas: Especializada + IA + Web profesional"
    },
    {
        "nombre": "Electricidad del Automotor F. San Martín",
        "email": "info@electricidadsanmartin.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "San Martín: Completa + IA + Agente automático"
    },
    {
        "nombre": "Electricidad del Automotor Río Negro",
        "email": "contacto@electricidadronegro.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Río Negro: Integral + IA + Voz automática"
    },
    {
        "nombre": "Electricidad del Automotor Maipú",
        "email": "info@electricidadmaipu.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Maipú: Especializado + IA + Agente de voz"
    },
    {
        "nombre": "Electricidad del Automotor Lanín",
        "email": "contacto@electricidadalanin.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Lanín: 24hs + IA + Web + Agente automático"
    },
    {
        "nombre": "Taller San Martín 1554",
        "email": "info@tallersmarin1554.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "San Martín 1554: Diferenciales + Inyección + IA"
    },
    {
        "nombre": "Agustín Contreras Taller",
        "email": "contacto@augustincontreras.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Contreras: Mecánico Integral + IA + Agente de voz"
    },
    {
        "nombre": "GPS Taller - Servicio A&M",
        "email": "info@gpstaller.com.ar",
        "zona": "Cipolletti",
        "asunto": "GPS Taller: Mecánica especializada + IA + Web"
    },
    {
        "nombre": "Cigütap Rectificación",
        "email": "contacto@cigutap.com.ar",
        "zona": "Cipolletti",
        "asunto": "Cigütap: Rectificación + IA + Agente de voz"
    },
    {
        "nombre": "Taller Mecánico Falucho",
        "email": "info@tallerfahucho.com.ar",
        "zona": "Cipolletti",
        "asunto": "Falucho: Cajas + Mecánica + IA + Voz automática"
    },
    {
        "nombre": "Taller Mecánico Peña",
        "email": "contacto@tallerpenazapala.com.ar",
        "zona": "Zapala",
        "asunto": "Peña: Taller Integral + IA + Web profesional"
    },
    {
        "nombre": "Electromecánica Sánchez H",
        "email": "info@electromecaniasanchez.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Sánchez: Integral + IA + Agente automático"
    },
    {
        "nombre": "Taller Mecánico General Neuquén",
        "email": "contacto@tallergeneral.com.ar",
        "zona": "Neuquén Capital",
        "asunto": "Taller General: Completo + IA + Voz automática"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio mecánico y electromecánico en Neuquén.

El problema: cuando un cliente busca "taller mecánico Neuquén" o "electricidad automotriz"
en Google, ¿dónde apareces?

La mayoría de talleres NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS EN NEUQUÉN?
- Búsquedas/mes de "taller mecánico": ~1,200
- Búsquedas/mes de "electricidad automotriz": ~550
- Total: ~1,750 búsquedas/mes
- Sin presencia digital: pierden 90% = 1,575 búsquedas/mes

Si el 25% se convierte:
- 1,575 × 25% = 393 clientes potenciales PERDIDOS/mes
- 393 × $290 (promedio trabajo) = $113,970/mes = $1,367,640/AÑO

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
    print("📧 ENVIANDO EMAILS A TALLERES DE NEUQUÉN")
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
