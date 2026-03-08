function sendMessage() {
    let input = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<p><b>You:</b> ${input}</p>`;

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input })
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += `<p><b>AI Bot:</b><pre>${data.reply}</pre></p>`;
    });
}
