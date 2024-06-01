const jsConfetti = new JSConfetti();

const emojisList = ['🌈', '⚡️', '💥', '✨', '💫', '🌸']
window.onload = async () => {
    while (true) {
        await jsConfetti.addConfetti({
            emojis: emojisList,
        })
    }
};