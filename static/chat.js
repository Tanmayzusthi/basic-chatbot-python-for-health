const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");


// ---------------------------------------------------
// ADD MESSAGE TO CHAT UI
// ---------------------------------------------------
function addMessage(text, isUser = false) {
    const bubble = document.createElement("div");
    bubble.className = isUser ? "user-bubble" : "bot-bubble";
    bubble.textContent = text;
    chatBox.appendChild(bubble);

    // Auto scroll
    chatBox.scrollTop = chatBox.scrollHeight;
}


// ---------------------------------------------------
// SEND MESSAGE TO BACKEND
// ---------------------------------------------------
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, true);
    userInput.value = "";

    // Bot typing placeholder
    addMessage("Thinking...", false);

    const allBubbles = document.getElementsByClassName("bot-bubble");
    const loadingBubble = allBubbles[allBubbles.length - 1];

    try {
        const response = await fetch("/get_response", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ msg: message })
        });

        const data = await response.json();

        // Replace "Thinking..." with real reply
        loadingBubble.textContent = data.reply;

    } catch (error) {
        loadingBubble.textContent =
            "Network issue. Try again in a moment.";
    }
}


// ---------------------------------------------------
// BUTTON CLICK
// ---------------------------------------------------
sendBtn.addEventListener("click", sendMessage);


// ---------------------------------------------------
// ENTER KEY SEND
// ---------------------------------------------------
userInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
