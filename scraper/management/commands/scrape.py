from django.core.management.base import BaseCommand
from scraper.services.scrape import scrape_website
from scraper.models import ScrapedData

class Command(BaseCommand):
    help = "Run the web scraper"
    # Hereda de BaseCommand, lo que permite que este comando sea ejecutable mediante python manage.py <nombre_comando>.

    def handle(self, *args, **kwargs):
        # Ejecuta función
        data = scrape_website()
        print("Scraped Data:", data)  # Agrega esta línea para depurar
        # Guarda
        # for item in data:
        #     ScrapedData.objects.create(text=item["text"], author=item["author"])
        # # Confirma
        # self.stdout.write(self.style.SUCCESS("Scraping completed!"))
        
        # 2. Guardamos en la base de datos nueva
        for item in data:
            # Truco: Convertimos la lista de tags ['amor', 'vida'] a texto "amor, vida"
            tags_as_text = ", ".join(item["tags"])
            
            ScrapedData.objects.create(
                quote=item["quote"],     # Usamos la clave 'quote' del diccionario
                author=item["author"],   # Usamos la clave 'author'
                tags=tags_as_text        # Guardamos los tags
            )
        self.stdout.write(self.style.SUCCESS(f"¡Guardadas {len(data)} citas nuevas!"))