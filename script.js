document.addEventListener('DOMContentLoaded', function() {
    const tumhiAudio = document.getElementById('tumhi-audio');
    const aishaAudio = document.getElementById('aisha-audio');
    const tumhiButton = document.getElementById('tumhi-button');
    const aishaButton = document.getElementById('aisha-button');
    let isTumhiPlaying = false;
    let isAishaPlaying = false;

    // Control for Tum Hi Ho audio
    tumhiButton.addEventListener('click', function() {
        if (isTumhiPlaying) {
            tumhiAudio.pause();
            tumhiButton.textContent = "Play Tum Hi Ho";
            isTumhiPlaying = false;
        } else {
            // Pause other audio if playing
            if (isAishaPlaying) {
                aishaAudio.pause();
                aishaButton.textContent = "Aisha";
                isAishaPlaying = false;
            }
            tumhiAudio.play();
            tumhiButton.textContent = "Pause Tum Hi Ho";
            isTumhiPlaying = true;
        }
    });

    // Control for Aisha's audio
    aishaButton.addEventListener('click', function() {
        if (isAishaPlaying) {
            aishaAudio.pause();
            aishaButton.textContent = "Aisha";
            isAishaPlaying = false;
        } else {
            // Pause other audio if playing
            if (isTumhiPlaying) {
                tumhiAudio.pause();
                tumhiButton.textContent = "Play Tum Hi Ho";
                isTumhiPlaying = false;
            }
            aishaAudio.play();
            aishaButton.textContent = "Pause Aisha";
            isAishaPlaying = true;
        }
    });
});
