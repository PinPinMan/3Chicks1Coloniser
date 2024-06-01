const jsConfetti = new JSConfetti();


const emojisList = ['😈', '👩🏽‍💻', '👺', '👹', '👾', '👽', '💀', '💩']
window.onload = async () => {
    while (true) {
        await jsConfetti.addConfetti({
            emojis: emojisList,
        })
    }
};


audio_tags = document.getElementsByTagName('audio')
for (var i = 0; i < audio_tags.length; i++) {
  audio_tags[i].addEventListener("loadstart", function() {
    this.volume = this.getAttribute('volume');
  }, true);
}