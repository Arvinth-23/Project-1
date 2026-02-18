import google.generativeai as genai
from app.config import settings

# Configure Gemini API
genai.configure(api_key=settings.gemini_api_key)

# Mock response for testing when API fails
MOCK_RESPONSES = {
    "ai": "Great question! AI careers are booming right now. Here are the best paths:\n\n1. **Machine Learning Engineer** - Build and train ML models. Requires Python, TensorFlow/PyTorch knowledge.\n\n2. **AI Research Scientist** - Develop new AI algorithms and techniques. Usually requires a Master's or PhD.\n\n3. **Data Scientist** - Analyze data and build predictive models. Need strong stats and programming skills.\n\n4. **AI/ML Operations Engineer** - Deploy and maintain AI systems in production.\n\n5. **Prompt Engineer** - Design and optimize prompts for large language models.\n\nStart with Python, learn SQL, and take courses on machine learning fundamentals!",
    "programming": "Here are the best programming languages for AI careers:\n\n1. **Python** - THE most popular language for AI/ML. Libraries: TensorFlow, PyTorch, Scikit-learn.\n\n2. **R** - Excellent for data analysis and statistics.\n\n3. **Java** - Great for production ML systems and scalability.\n\n4. **C++** - Used for high-performance AI applications.\n\n5. **JavaScript** - Increasingly important for browser-based ML with TensorFlow.js.\n\nRecommendation: Start with **Python**! It has the best libraries and community support for AI.",
    "learning": "Here's a recommended learning path:\n\n1. **Fundamentals (3-6 months)**\n   - Python programming\n   - Mathematics (Linear Algebra, Calculus, Probability)\n   - SQL & databases\n\n2. **Core Skills (6-12 months)**\n   - Machine Learning algorithms\n   - Deep Learning basics\n   - Data preprocessing & visualization\n\n3. **Practice (Ongoing)**\n   - Kaggle competitions\n   - Personal projects\n   - Open source contributions\n\n4. **Specialization (1-2 years)**\n   - NLP, Computer Vision, Reinforcement Learning, etc.\n\nBest resources: Andrew Ng's ML course, Fast.ai, DataCamp, Coursera.",
}

async def get_chat_response(conversation, user_context=""):
    system_prompt = f"""
You are a career guidance advisor for college students.
{user_context}
Provide helpful, accurate, and encouraging advice.
Be concise but informative.
"""

    try:
        # Try to get available models and use the first one
        try:
            models = genai.list_models()
            available_models = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
            model_name = available_models[0].replace('models/', '') if available_models else 'gemini-pro'
        except:
            model_name = 'gemini-pro'
        
        model = genai.GenerativeModel(model_name)
        
        # Format conversation history for Gemini
        chat_messages = []
        for msg in conversation:
            chat_messages.append({
                "role": "user" if msg["role"] == "user" else "model",
                "parts": [msg["content"]]
            })
        
        # Add system prompt to the first user message
        if chat_messages and chat_messages[0]["role"] == "user":
            chat_messages[0]["parts"][0] = system_prompt + "\n\n" + chat_messages[0]["parts"][0]
        
        # Start chat session
        chat = model.start_chat(history=chat_messages[:-1] if len(chat_messages) > 1 else [])
        
        # Send the latest message
        response = chat.send_message(chat_messages[-1]["parts"][0] if chat_messages else "Hello")
        
        return response.text

    except Exception as e:
        print("GEMINI ERROR:", e)
        
        # Fallback to mock response if API fails
        last_message = conversation[-1]["content"].lower() if conversation else ""
        
        # Try to match user intent
        for keyword, mock_response in MOCK_RESPONSES.items():
            if keyword in last_message:
                return mock_response
        
        # Default helpful response
        return "I'm here to help with career advice! Ask me about AI careers, programming languages, learning paths, or any other career guidance."
