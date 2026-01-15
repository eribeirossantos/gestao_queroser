from django.forms.widgets import FileInput
from django.utils.html import format_html

class CameraWidget(FileInput):
    """Widget para capturar foto via câmera do navegador"""
    
    def __init__(self, attrs=None):
        default_attrs = {'accept': 'image/*', 'capture': 'environment'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
    
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        
        # Adicionar botão para câmera
        camera_html = format_html(
            '<div style="margin-top: 10px;">'
            '<button type="button" id="camera-btn-{}" onclick="openCamera(\'{}\')" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer;">'
            'Abrir Câmera'
            '</button>'
            '</div>'
            '<div id="camera-container-{}" style="display:none; margin-top: 10px;">'
            '<video id="video-{}" style="width: 100%; max-width: 400px; border-radius: 4px;"></video><br>'
            '<button type="button" onclick="takePhoto(\'{}\')" style="padding: 10px 20px; background-color: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; margin-top: 10px;">'
            'Capturar Foto'
            '</button>'
            '<button type="button" onclick="closeCamera(\'{}\')" style="padding: 10px 20px; background-color: #dc3545; color: white; border: none; border-radius: 4px; cursor: pointer; margin-top: 10px; margin-left: 10px;">'
            'Fechar'
            '</button>'
            '</div>'
            '<canvas id="canvas-{}" style="display:none;"></canvas>',
            name, name,
            name,
            name,
            name, name,
            name
        )
        
        return html + camera_html


# JavaScript para o widget
CAMERA_JS = """
<script>
let currentStream = null;

function openCamera(fieldName) {
    const container = document.getElementById('camera-container-' + fieldName);
    const video = document.getElementById('video-' + fieldName);
    
    container.style.display = 'block';
    
    navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'user' }
    }).then(function(stream) {
        currentStream = stream;
        video.srcObject = stream;
        video.play();
    }).catch(function(err) {
        alert('Erro ao acessar câmera: ' + err.message);
    });
}

function takePhoto(fieldName) {
    const video = document.getElementById('video-' + fieldName);
    const canvas = document.getElementById('canvas-' + fieldName);
    const fileInput = document.getElementById('id_' + fieldName);
    
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0);
    
    canvas.toBlob(function(blob) {
        const file = new File([blob], 'camera_photo_' + Date.now() + '.jpg', { type: 'image/jpeg' });
        
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        fileInput.files = dataTransfer.files;
        
        closeCamera(fieldName);
        alert('Foto capturada com sucesso!');
    }, 'image/jpeg', 0.9);
}

function closeCamera(fieldName) {
    const container = document.getElementById('camera-container-' + fieldName);
    const video = document.getElementById('video-' + fieldName);
    
    if (currentStream) {
        currentStream.getTracks().forEach(track => track.stop());
        currentStream = null;
    }
    
    video.srcObject = null;
    container.style.display = 'none';
}
</script>
"""
