let video = document.getElementById('video');
let canvas = document.getElementById('canvas');
let captureButton = document.getElementById('capture');
let result = document.getElementById('result');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing the camera", err);
    });

captureButton.addEventListener('click', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    
    canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append('file', blob, 'capture.jpg');

        fetch('/predict/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            result.textContent = `Seña reconocida: ${data.prediction}`;
        })
        .catch(error => {
            console.error('Error:', error);
            result.textContent = 'Error al procesar la imagen';
        });
    }, 'image/jpeg');
});