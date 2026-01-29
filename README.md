# Web Scraper Project

Un proyecto Django de web scraping automatizado que utiliza Selenium y Firefox en un contenedor Docker, con ejecución programada mediante cron.

## 📋 Descripción

Este proyecto implementa un web scraper que:
- Extrae datos de sitios web usando Selenium con Firefox
- Guarda los datos en una base de datos SQLite
- Toma capturas de pantalla automáticas
- Se ejecuta automáticamente cada minuto mediante cron
- Funciona completamente dentro de un contenedor Docker

## 🚀 Características

- **Scraping automatizado**: Extracción de títulos y URLs de páginas web
- **Capturas de pantalla**: Almacenamiento de screenshots con timestamp
- **Ejecución programada**: Cron job configurado para ejecutarse cada minuto
- **Dockerizado**: Totalmente containerizado para fácil despliegue
- **Base de datos**: SQLite para almacenar datos scrapeados
- **Admin de Django**: Panel de administración para ver datos recolectados

## 🛠️ Tecnologías

- **Python 3.12**
- **Django 6.0.1**
- **Selenium 4.40.0**
- **Firefox ESR** (headless)
- **GeckoDriver 0.35.0**
- **Docker & Docker Compose**
- **Cron**

## 📦 Estructura del Proyecto

```
.
├── scraper/                      # Aplicación Django principal
│   ├── management/
│   │   └── commands/
│   │       └── scrape.py        # Comando personalizado de scraping
│   ├── services/
│   │   └── scrape.py            # Lógica de scraping con Selenium
│   ├── models.py                # Modelo ScrapedData
│   └── admin.py                 # Configuración del admin
├── webscraper_project/          # Configuración Django
│   ├── settings.py
│   └── urls.py
├── screenshots/                 # Volumen para capturas de pantalla
├── Dockerfile                   # Configuración del contenedor
├── compose.yaml                 # Orquestación Docker
├── cronfile                     # Configuración de cron
├── requirements.txt             # Dependencias Python
└── manage.py                    # CLI de Django
```

## 🔧 Instalación y Uso

### Prerrequisitos

- Docker
- Docker Compose

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone <tu-repositorio>
cd webscraper_project
```

2. **Construir y ejecutar el contenedor**
```bash
docker compose up --build
```

3. **El scraper se ejecutará automáticamente cada minuto**

### Verificar funcionamiento

**Ver logs de cron:**
```bash
docker compose exec server tail -f /var/log/cron.log
```

**Acceder al contenedor:**
```bash
docker compose exec server bash
```

**Ver capturas de pantalla:**
Las capturas se guardan en `./screenshots/` en tu máquina host

**Acceder a la base de datos:**
```bash
docker compose exec server python manage.py dbshell
```

## 🎯 Comandos Útiles

### Ejecutar scraping manualmente
```bash
docker compose exec server python manage.py scrape
```

### Crear superusuario (para acceder al admin)
```bash
docker compose exec server python manage.py createsuperuser
```

### Ver logs del contenedor
```bash
docker compose logs -f server
```

### Reiniciar el contenedor
```bash
docker compose restart
```

## 📊 Acceso al Admin de Django

1. Crear superusuario (ver comando arriba)
2. Si deseas acceder al panel admin, modifica el `Dockerfile` para ejecutar el servidor Django:
```dockerfile
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
3. Descomenta la línea en `compose.yaml` para exponer el puerto
4. Accede a `http://localhost:8000/admin`

## 🔄 Configuración de Cron

El archivo `cronfile` define la frecuencia de ejecución:
```
* * * * * /usr/local/bin/python /app/manage.py scrape >> /var/log/cron.log 2>&1
```

**Formato:** `minuto hora día mes día_semana comando`

**Ejemplos:**
- Cada minuto: `* * * * *`
- Cada hora: `0 * * * *`
- Cada día a las 2 AM: `0 2 * * *`
- Cada lunes a las 9 AM: `0 9 * * 1`

## 🐛 Solución de Problemas

### Cron no ejecuta el scraper
- Verificar logs: `docker compose exec server cat /var/log/cron.log`
- Verificar que cron esté corriendo: `docker compose exec server ps aux | grep cron`

### Error con caracteres Windows en cronfile
El Dockerfile incluye: `RUN sed -i 's/\r$//' /etc/cron.d/scrape-cron`

### Permisos de escritura
Los directorios `/app` y `/app/screenshots` tienen permisos 777 para evitar problemas

### Firefox no se inicia
Verificar que todos los paquetes estén instalados correctamente en el Dockerfile

## 📝 Personalización

### Cambiar URL objetivo
Edita `scraper/services/scrape.py`:
```python
url = "https://tu-sitio-web.com"
```

### Modificar selectores CSS
Edita los selectores en `scrape.py`:
```python
titles = driver.find_elements(By.CSS_SELECTOR, "tu-selector")
```

### Ajustar tiempo de espera
Modifica el timeout en `scrape.py`:
```python
WebDriverWait(driver, 10).until(...)  # Cambiar 10 por segundos deseados
```

## ⚠️ Notas Importantes

- El proyecto usa **root** dentro del contenedor por simplicidad
- En producción, considera usar un usuario no privilegiado
- La `SECRET_KEY` debe cambiarse en producción
- `DEBUG = True` debe ser `False` en producción
- Las capturas de pantalla se acumulan - implementa limpieza periódica si es necesario

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia que elijas especificar.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios propuestos.
