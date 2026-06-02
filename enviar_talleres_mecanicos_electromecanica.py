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

# ===== 17 TALLERES MECÁNICOS Y ELECTROMECÁNICOS A CONTACTAR =====
TALLERES = [
    {
        "nombre": "Electrohollywood",
        "email": "info@electrohollywood.com.ar",
        "zona": "Chacarita",
        "asunto": "Electrohollywood: Tu web + IA + Agente de voz = +100% clientes"
    },
    {
        "nombre": "Taller Mecánico Almagro",
        "email": "info@tallermecanicoalmagro.com.ar",
        "zona": "Almagro",
        "asunto": "Taller Almagro: Mecánica + IA + Web = Negocios automáticos"
    },
    {
        "nombre": "Taller Marchesi",
        "email": "contacto@tallermarchesi.com.ar",
        "zona": "Caballito",
        "asunto": "Marchesi: Inyección + Web + IA = De 20 a 50+ clientes/semana"
    },
    {
        "nombre": "Em Electromecánica",
        "email": "contacto@emelectromecanica.com.ar",
        "zona": "Capital Federal",
        "asunto": "Em Electromecánica: Servicio completo + IA automática"
    },
    {
        "nombre": "Taller Charlie",
        "email": "info@tallercharlie.com.ar",
        "zona": "Coghlan",
        "asunto": "Taller Charlie: Electricidad automotriz + Web + IA"
    },
    {
        "nombre": "Electricidad del Automóvil Caracas",
        "email": "info@electricidaddelautomovil.com.ar",
        "zona": "Capital Federal",
        "asunto": "Electricidad Caracas: Cerrajería + Web + Agente de voz"
    },
    {
        "nombre": "Taller Electromecánico Tapalqué",
        "email": "contacto@tallerelectromecanico.com.ar",
        "zona": "Capital Federal",
        "asunto": "Tapalqué: Electromecánica + IA = Cero llamadas perdidas"
    },
    {
        "nombre": "Electromecánica Herz",
        "email": "contacto@electromecanicaherz.com.ar",
        "zona": "Capital Federal",
        "asunto": "Herz: Aire + Inyección + Electricidad + IA"
    },
    {
        "nombre": "Taller Repro",
        "email": "info@repro.com.ar",
        "zona": "Belgrano",
        "asunto": "Repro: Mecánica integral + Web + Agente automático"
    },
    {
        "nombre": "Destapaciones Electromecánica",
        "email": "contacto@destapaciones.com.ar",
        "zona": "Capital Federal",
        "asunto": "Destapaciones: Máquinas + IA + Web profesional"
    },
    {
        "nombre": "CIRVE Electromecánica",
        "email": "info@cirve.com.ar",
        "zona": "Palermo",
        "asunto": "CIRVE: Especializado + IA + Voz automática"
    },
    {
        "nombre": "Electronec Servicios",
        "email": "contacto@electronec.com.ar",
        "zona": "Capital Federal",
        "asunto": "Electronec: Electricista + Gasista + Plomero + IA"
    },
    {
        "nombre": "Taller Eléctrico Acuña de Figueroa",
        "email": "info@tallerelectricopalermo.com.ar",
        "zona": "Palermo Viejo",
        "asunto": "Palermo Viejo: Eléctrica automotriz + IA + Web"
    },
    {
        "nombre": "Taller Eléctrico Gorriti",
        "email": "contacto@tallerelectricogorriti.com.ar",
        "zona": "Palermo Soho",
        "asunto": "Palermo Soho: Especializado + IA + Agente de voz"
    },
    {
        "nombre": "Taller Eléctrico Guardia Vieja",
        "email": "info@tallerelectricoabasto.com.ar",
        "zona": "Abasto",
        "asunto": "Abasto: Reparación eléctrica + Web + IA automática"
    },
    {
        "nombre": "Taller Eléctrico Rojas",
        "email": "contacto@tallerelectricorojas.com.ar",
        "zona": "Caballito",
        "asunto": "Rojas: Electricidad automotriz + IA + Cero esperas"
    },
    {
        "nombre": "Servicio Batería y Alternador",
        "email": "info@serviciobateriaaltarnador.com.ar",
        "zona": "Capital Federal",
        "asunto": "Batería y Alternador: Especializado + IA + Agente automático"
    }
]

def obtener_cuerpo_email(nombre, telefono):
    """Retorna el cuerpo del email personalizado"""

    cuerpo = f"""Hola {nombre},

Vi que ofrecen servicio mecánico y electromecánico en Capital Federal.

El problema: cuando un cliente busca "taller mecánico CABA" o "electricidad automotriz"
en Google, ¿dónde apareces?

La mayoría de talleres NO aparecen en Google. Eso significa:
- Clientes nuevos buscan online
- No te encuentran
- Van a la competencia

¿NÚMEROS?
- Búsquedas/mes de "taller mecánico CABA": ~2,000
- Búsquedas/mes de "electricidad automotriz": ~1,500
- Total: ~3,500 búsquedas/mes
- Sin presencia digital: pierden 95% = 3,325 búsquedas/mes

Si el 25% se convierte:
- 3,325 × 25% = 831 clientes potenciales PERDIDOS/mes
- 831 × $350 (promedio trabajo) = $290,850/mes = $3,490,200/AÑO

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
De 25 clientes/semana a 60+ clientes/semana.
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
    print("📧 ENVIANDO EMAILS A TALLERES MECÁNICOS Y ELECTROMECÁNICOS")
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
