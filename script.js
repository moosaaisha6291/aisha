document.addEventListener('DOMContentLoaded', function() {
    const music = document.getElementById('bg-music'); // Correct ID reference
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
