import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ===== TUS CREDENCIALES =====
TU_EMAIL = "argentia.ai@gmail.com"
TU_PASSWORD = "Bo01cas2025+"
TU_NOMBRE = "Cristian Vargas"

# ===== CONFIGURACIÓN GMAIL =====
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

print("="*60)
print("📧 PRUEBA DE CONEXIÓN GMAIL")
print("="*60)

print(f"\n📤 Conectando a Gmail con: {TU_EMAIL}")
print(f"   App Password: {TU_PASSWORD[:3]}...{TU_PASSWORD[-3:]}")

try:
    # Conecta a Gmail
    print("\n⏳ Conectando al servidor SMTP...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()

    print("⏳ Iniciando sesión...")
    server.login(TU_EMAIL, TU_PASSWORD)

    print("✅ CONEXIÓN EXITOSA\n")

    # Crea el email de prueba
    print("📝 Creando email de prueba...")
    mensaje = MIMEMultipart()
    mensaje['From'] = TU_EMAIL
    mensaje['To'] = TU_EMAIL  # A ti mismo
    mensaje['Subject'] = "✅ PRUEBA DE CONEXIÓN GMAIL - Prospecting IA"

    cuerpo = f"""Hola {TU_NOMBRE},

Este es un email de PRUEBA para verificar que tu conexión a Gmail funciona correctamente.

Si recibiste este email, significa que:
✅ Tu App Password es correcto
✅ La conexión a Gmail funciona
✅ Puedes enviar emails automáticamente
✅ TODO ESTÁ OK para enviar los 5 emails a electricistas

PRÓXIMO PASO:
Cuando confirmes que recibiste este email, ejecutaremos el script final para enviar a:
1. Electricista La Boca
2. VIP Electricidad
3. Electricista Almagro 24hs
4. General Electric Service
5. AA Service Eléctrico

Fecha de prueba: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}

¡A PROSPECTAR! 🚀

---
Script automático de Prospecting IA
"""

    mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

    # Envía
    print("📤 Enviando email de prueba a ti mismo...")
    server.send_message(mensaje)
    server.quit()

    print("✅ EMAIL ENVIADO EXITOSAMENTE\n")

    print("="*60)
    print("🎉 PRUEBA COMPLETADA CON ÉXITO")
    print("="*60)
    print("\n✅ La conexión a Gmail funciona correctamente")
    print("✅ Tu App Password es válido")
    print("✅ Puedes enviar emails automáticamente")
    print("\n📧 Ahora revisa tu Gmail (carpeta Entrada)")
    print("   Deberías ver el email de prueba")
    print("\n🚀 Cuando lo confirmes, ejecutamos el script final")
    print("   para enviar a los 5 electricistas")
    print("="*60)

except smtplib.SMTPAuthenticationError:
    print("\n❌ ERROR: APP PASSWORD INCORRECTA")
    print("\nVerifica que:")
    print("1. Generaste correctamente el App Password en Google")
    print("2. Copiaste SIN ESPACIOS")
    print("3. Reemplazaste en TU_PASSWORD")
    print("\nRe-genera en: myaccount.google.com → Seguridad → Contraseña de aplicación")

except smtplib.SMTPException as e:
    print(f"\n❌ ERROR DE GMAIL: {e}")
    print("\nVerifica que:")
    print("1. Tu email es correcto")
    print("2. Tienes conexión a internet")
    print("3. Gmail no está bloqueando la conexión")

except Exception as e:
    print(f"\n❌ ERROR GENERAL: {e}")
    print("\nIntenta nuevamente con credenciales correctas")
