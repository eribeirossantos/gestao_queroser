// JavaScript para widget de câmera no Django Admin
let currentStream = null;

function openCamera(fieldName) {
    const container = document.getElementById('camera-container-' + fieldName);
    const video = document.getElementById('video-' + fieldName);
    
    if (container) {
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
}

function takePhoto(fieldName) {
    const video = document.getElementById('video-' + fieldName);
    const canvas = document.getElementById('canvas-' + fieldName);
    const fileInput = document.getElementById('id_' + fieldName);
    
    if (video && canvas) {
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
}

function closeCamera(fieldName) {
    const container = document.getElementById('camera-container-' + fieldName);
    const video = document.getElementById('video-' + fieldName);
    
    if (currentStream) {
        currentStream.getTracks().forEach(track => track.stop());
        currentStream = null;
    }
    
    if (video) {
        video.srcObject = null;
    }
    
    if (container) {
        container.style.display = 'none';
    }
}

// Adicionar o JavaScript do widget
document.addEventListener('DOMContentLoaded', function() {
    // Injetar o CSS do widget se necessário
    const style = document.createElement('style');
    style.textContent = `
        .camera-widget-container {
            margin-top: 10px;
        }
        .camera-widget-button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-right: 10px;
        }
        .camera-widget-button:hover {
            background-color: #0056b3;
        }
        .camera-widget-capture {
            background-color: #28a745;
        }
        .camera-widget-capture:hover {
            background-color: #218838;
        }
        .camera-widget-close {
            background-color: #dc3545;
        }
        .camera-widget-close:hover {
            background-color: #c82333;
        }
        #camera-container video {
            width: 100%;
            max-width: 400px;
            border-radius: 4px;
            margin-top: 10px;
        }
    `;
    document.head.appendChild(style);
});
