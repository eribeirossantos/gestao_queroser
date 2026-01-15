from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
import io
import os
from .models import Aluno

@receiver(pre_save, sender=Aluno)
def compress_image(sender, instance, **kwargs):
    """Comprime a imagem do aluno automaticamente"""
    
    if instance.foto:
        # Verificar se a imagem foi alterada
        try:
            old_instance = Aluno.objects.get(pk=instance.pk)
            if old_instance.foto == instance.foto:
                return  # Imagem não foi alterada
        except Aluno.DoesNotExist:
            pass  # É um novo aluno
        
        # Abrir a imagem
        try:
            img = Image.open(instance.foto)
            
            # Converter RGBA para RGB (se necessário)
            if img.mode in ('RGBA', 'LA', 'P'):
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = rgb_img
            
            # Redimensionar se for muito grande
            max_width = 800
            max_height = 800
            img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
            
            # Salvar em memória com compressão
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=70, optimize=True)
            img_io.seek(0)
            
            # Calcular tamanho original vs comprimido
            original_size = instance.foto.size
            compressed_size = len(img_io.getvalue())
            
            # Log de informações
            print(f"✅ Imagem comprimida: {original_size/1024:.1f}KB → {compressed_size/1024:.1f}KB")
            
            # Atualizar o arquivo
            instance.foto.save(
                instance.foto.name,
                img_io,
                save=False
            )
            
        except Exception as e:
            print(f"❌ Erro ao comprimir imagem: {str(e)}")
            # Continuar mesmo se houver erro na compressão
            pass
