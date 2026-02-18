const API_URL = "http://127.0.0.1:8002";

let userId = 1;
let sessionId = null;

const messagesContainer = document.getElementById("messages");
const userInput = document.getElementById("userInput");
const chatForm = document.getElementById("chatForm");
const quickButtons = document.querySelectorAll(".quick-btn");
const clearBtn = document.getElementById("clearBtn");
const loadingIndicator = document.getElementById("loadingIndicator");
const sessionDisplay = document.getElementById("sessionDisplay");

// Topic to question mapping
const topicQuestions = {
    "ai": "What are the best AI and machine learning careers?",
    "programming": "What are the best programming languages to learn?",
    "learning": "What's a good learning path for someone interested in tech careers?",
    "skills": "What are the most important skills for a tech career?",
    "salary": "What are typical salaries for tech careers?",
    "internships": "How do I find and get internships in tech companies?"
};

// Initialize
document.addEventListener("DOMContentLoaded", () => {
    setupEventListeners();
    removeWelcomeMessage();
});

function setupEventListeners() {
    chatForm.addEventListener("submit", handleFormSubmit);
    
    quickButtons.forEach(btn => {
        btn.addEventListener("click", handleQuickTopic);
    });
    
    clearBtn.addEventListener("click", handleNewChat);
}

function removeWelcomeMessage() {
    const welcome = document.querySelector(".welcome-message");
    if (welcome && messagesContainer.children.length === 1) {
        welcome.remove();
    }
}

function handleQuickTopic(e) {
    e.preventDefault();
    const topic = e.target.dataset.topic;
    const message = topicQuestions[topic];
    if (message) {
        userInput.value = message;
        sendMessage(message);
    }
}

function handleFormSubmit(e) {
    e.preventDefault();
    const text = userInput.value.trim();
    if (text) {
        sendMessage(text);
    }
}

async function sendMessage(text) {
    // Remove welcome message if it exists
    removeWelcomeMessage();

    // Add user message
    addMessage("user", text);
    userInput.value = "";

    // Show loading indicator
    showLoading(true);

    try {
        const response = await fetch(`${API_URL}/chat/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                user_id: userId,
                message: text,
                session_id: sessionId
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error("Backend error:", response.status, errorText);
            addMessage("assistant", "Sorry, I encountered an error. Please try again.");
            showLoading(false);
            return;
        }

        const data = await response.json();
        console.log("Backend response:", data);

        if (data.reply) {
            sessionId = data.session_id;
            updateSessionDisplay();
            addMessage("assistant", data.reply);
        } else {
            addMessage("assistant", "No response received. Please try again.");
        }

    } catch (error) {
        console.error("Connection error:", error);
        addMessage("assistant", "Unable to connect to server. Please make sure the backend is running.");
    } finally {
        showLoading(false);
    }
}

function addMessage(role, content) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(role === "user" ? "user-message" : "assistant-message");

    const bubble = document.createElement("div");
    bubble.classList.add("message-bubble");
    
    // Format the content (handle line breaks and markdown-like formatting)
    bubble.innerHTML = formatContent(content);

    messageDiv.appendChild(bubble);
    messagesContainer.appendChild(messageDiv);

    // Auto-scroll to bottom
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function formatContent(content) {
    // Escape HTML
    content = content
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    
    // Convert line breaks to <br>
    content = content.replace(/\n/g, "<br>");
    
    // Convert **bold** to <strong>
    content = content.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    
    // Convert markdown bullet points
    content = content.replace(/^• /gm, "• ");
    content = content.replace(/^\* /gm, "• ");
    content = content.replace(/^\d+\. /gm, (match) => `<br>${match}`);
    
    return content;
}

function updateSessionDisplay() {
    if (sessionId) {
        const shortId = sessionId.substring(0, 8) + "...";
        sessionDisplay.textContent = `Session: ${shortId}`;
    }
}

function handleNewChat() {
    // Clear messages
    messagesContainer.innerHTML = `
        <div class="welcome-message">
            <h2>Welcome! 👋</h2>
            <p>I'm your AI career advisor. Click a quick topic or ask me anything about careers!</p>
        </div>
    `;
    
    // Reset session
    sessionId = null;
    userId = Math.floor(Math.random() * 1000000);
    userInput.value = "";
    sessionDisplay.textContent = "Session: New";
    
    userInput.focus();
}

function showLoading(show) {
    if (show) {
        loadingIndicator.classList.remove("hidden");
    } else {
        loadingIndicator.classList.add("hidden");
    }
}
