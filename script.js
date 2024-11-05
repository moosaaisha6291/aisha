document.addEventListener('DOMContentLoaded', function() {
    const music = document.getElementById('Tum_Hi_Ho_-_Aashiqui_2_128_Kbps.mp3');
    let isPlaying = true;

    document.body.addEventListener('click', function() {
        if (isPlaying) {
            music.pause();
            isPlaying = false;
        } else {
            music.play();
            isPlaying = true;
        }
    });
});
