document.addEventListener('DOMContentLoaded', function() {
    const music = document.getElementById('bg-music');
    const playButton = document.getElementById('play-button');
    let isPlaying = false;

    playButton.addEventListener('click', function() {
        if (isPlaying) {
            music.pause();
            playButton.textContent = "Play Music";
            isPlaying = false;
        } else {
            music.play();
            playButton.textContent = "Pause Music";
            isPlaying = true;
        }
    });
});
