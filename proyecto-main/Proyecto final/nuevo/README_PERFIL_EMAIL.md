# Funcionalidades de Perfil de Usuario y Recuperación de Contraseña

## 🎯 Nuevas Funcionalidades Implementadas

### 1. Perfil de Usuario
- **Ver perfil**: Muestra información del usuario logueado
- **Editar perfil**: Permite modificar datos personales y foto de perfil
- **Cambiar contraseña**: Permite cambiar la contraseña de forma segura

### 2. Recuperación de Contraseña
- **Envío de email**: Sistema completo de recuperación por email
- **Templates mejorados**: Interfaz moderna y responsive

## 🚀 Cómo Usar

### Perfil de Usuario
1. **Acceder al perfil**: 
   - Inicia sesión en la aplicación
   - Haz clic en tu nombre de usuario en la barra de navegación
   - Selecciona "Mi Perfil"

2. **Editar perfil**:
   - Desde el perfil, haz clic en "Editar Perfil"
   - Modifica los campos que desees
   - Sube una nueva foto de perfil (opcional)
   - Guarda los cambios

3. **Cambiar contraseña**:
   - Desde el perfil, haz clic en "Cambiar Contraseña"
   - Ingresa la nueva contraseña (mínimo 8 caracteres)
   - Confirma la contraseña
   - Guarda los cambios

### Recuperación de Contraseña
1. **Configurar email** (solo una vez):
   ```bash
   python configurar_email.py
   ```

2. **Usar la recuperación**:
   - Ve a Login
   - Haz clic en "¿Olvidaste tu contraseña?"
   - Ingresa tu email
   - Revisa tu bandeja de entrada
   - Haz clic en el enlace de recuperación

## ⚙️ Configuración de Email

### Pasos para configurar Gmail:

1. **Activar verificación en dos pasos**:
   - Ve a https://myaccount.google.com/
   - Seguridad > Verificación en dos pasos

2. **Generar contraseña de aplicación**:
   - Seguridad > Contraseñas de aplicación
   - Selecciona "Django"
   - Copia la contraseña de 16 caracteres

3. **Ejecutar script de configuración**:
   ```bash
   cd "Proyecto final/nuevo"
   python configurar_email.py
   ```

### Configuración Manual (Alternativa)

Si prefieres configurar manualmente, edita `nuevo/settings.py`:

```python
EMAIL_HOST_USER = 'tu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'tu-contraseña-de-aplicación'
```

## 📁 Archivos Creados/Modificados

### Nuevos Archivos:
- `template/usuario/perfil.html` - Vista del perfil
- `template/usuario/editar_perfil.html` - Edición del perfil
- `template/usuario/cambiar_password.html` - Cambio de contraseña
- `configurar_email.py` - Script de configuración
- `README_PERFIL_EMAIL.md` - Este archivo

### Archivos Modificados:
- `apps/usuario/views.py` - Nuevas vistas agregadas
- `apps/usuario/urls.py` - Nuevas URLs agregadas
- `nuevo/settings.py` - Configuración de email agregada
- `template/base.html` - Menú de usuario mejorado
- `template/registration/recuperar_contraseña.html` - Template mejorado

## 🔧 URLs Disponibles

### Perfil de Usuario:
- `/usuario/perfil/` - Ver perfil
- `/usuario/perfil/editar/` - Editar perfil
- `/usuario/perfil/cambiar-password/` - Cambiar contraseña

### Recuperación de Contraseña:
- `/usuario/password_reset/` - Solicitar recuperación
- `/usuario/reset/<uidb64>/<token>/` - Confirmar nueva contraseña
- `/usuario/reset/done/` - Confirmación completada

## 🎨 Características de la Interfaz

- **Diseño responsive**: Funciona en móviles y desktop
- **Iconos FontAwesome**: Interfaz moderna y atractiva
- **Mensajes de feedback**: Confirmaciones y errores claros
- **Validaciones**: Contraseñas seguras y datos válidos
- **Navegación intuitiva**: Menú desplegable para usuarios logueados

## 🔒 Seguridad

- **Autenticación requerida**: Solo usuarios logueados pueden acceder
- **Validación de contraseñas**: Mínimo 8 caracteres
- **Tokens seguros**: Para recuperación de contraseña
- **CSRF protection**: Protección contra ataques CSRF

## 🐛 Solución de Problemas

### Email no se envía:
1. Verifica que la verificación en dos pasos esté activada
2. Asegúrate de usar una contraseña de aplicación (no tu contraseña normal)
3. Revisa que el email esté bien configurado en settings.py

### Error al subir imagen:
1. Verifica que la carpeta `media/` tenga permisos de escritura
2. Asegúrate de que el formato de imagen sea válido (JPG, PNG, etc.)

### Error en el perfil:
1. Verifica que estés logueado
2. Revisa que las migraciones estén aplicadas: `python manage.py migrate`

## 📞 Soporte

Si tienes problemas, verifica:
1. Que todas las dependencias estén instaladas
2. Que las migraciones estén aplicadas
3. Que el servidor esté corriendo
4. Los logs del servidor para errores específicos 