// 飄動愛心動畫
function createHeart() {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerText = "❤️";
    heart.style.left = Math.random() * window.innerWidth + "px";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 5000);
}
setInterval(createHeart, 500);

// 謎題驗證邏輯
function checkAnswer() {
    const userInput = document.getElementById("answer").value.trim().toLowerCase();
    const correctAnswer = "love2024";

    if (userInput === correctAnswer) {
        window.location.href = "success.html";
    } else {
        document.getElementById("error").textContent = "答錯囉，再想想！";
    }
}
