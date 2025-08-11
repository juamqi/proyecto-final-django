#!/usr/bin/env python3
"""
Script para configurar el email de Gmail para la recuperación de contraseñas
"""

import os
import sys

def configurar_email():
    print("=" * 60)
    print("CONFIGURACIÓN DE EMAIL PARA RECUPERACIÓN DE CONTRASEÑAS")
    print("=" * 60)
    print()
    
    print("Para que funcione la recuperación de contraseñas, necesitas:")
    print("1. Una cuenta de Gmail")
    print("2. Verificación en dos pasos activada")
    print("3. Una contraseña de aplicación")
    print()
    
    print("PASOS PARA CONFIGURAR:")
    print("1. Ve a https://myaccount.google.com/")
    print("2. Seguridad > Verificación en dos pasos (actívala)")
    print("3. Seguridad > Contraseñas de aplicación")
    print("4. Selecciona 'Django' y genera una contraseña")
    print("5. Copia esa contraseña de 16 caracteres")
    print()
    
    email = input("Ingresa tu dirección de Gmail: ").strip()
    password = input("Ingresa la contraseña de aplicación: ").strip()
    
    if not email or not password:
        print("Error: Debes ingresar tanto el email como la contraseña.")
        return
    
    # Actualizar settings.py
    settings_path = "nuevo/settings.py"
    
    try:
        with open(settings_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Reemplazar las configuraciones de email
        content = content.replace(
            "EMAIL_HOST_USER = 'tu-email@gmail.com'",
            f"EMAIL_HOST_USER = '{email}'"
        )
        content = content.replace(
            "EMAIL_HOST_PASSWORD = 'tu-contraseña-de-aplicación'",
            f"EMAIL_HOST_PASSWORD = '{password}'"
        )
        
        with open(settings_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print()
        print("✅ Configuración completada exitosamente!")
        print(f"Email configurado: {email}")
        print()
        print("Ahora puedes usar la funcionalidad de recuperación de contraseñas.")
        print("Para probar, ve a Login > ¿Olvidaste tu contraseña?")
        
    except Exception as e:
        print(f"Error al actualizar la configuración: {e}")
        print("Por favor, actualiza manualmente el archivo settings.py")

if __name__ == "__main__":
    configurar_email() 