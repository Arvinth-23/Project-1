# Spam Predictor & Career Guide Chatbot

A multi-project repository containing a spam detection ML model and an AI-powered career guidance chatbot application.

## 📁 Project Structure

### Spam Predictor (Root Level)
- **`app.py`** - Streamlit web interface for spam prediction
- **`train_model.py`** - ML model training script
- **`spam.csv`** - Dataset for training the spam classifier
- **`requirements.txt`** - Python dependencies for spam predictor

### Career Guide Chatbot (`career-guide-chatbot/`)
- **Backend**: FastAPI server with async SQLAlchemy and Google Gemini integration
- **Frontend**: Vanilla JavaScript web interface
- **Database**: PostgreSQL with async support
- See [career-guide-chatbot/.github/copilot-instructions.md](career-guide-chatbot/.github/copilot-instructions.md) for detailed backend documentation

## 🚀 Getting Started

### Spam Predictor Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model (optional):**
   ```bash
   python train_model.py
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

### Career Guide Chatbot Setup

1. **Navigate to backend:**
   ```bash
   cd career-guide-chatbot/backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in `backend/` with:
   ```
   GEMINI_API_KEY=your_api_key_here
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/chatbot_db
   SECRET_KEY=your_secret_key
   ```

5. **Run the server:**
   ```bash
   python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

6. **Open frontend:**
   Open `career-guide-chatbot/frontend/index.html` in your browser

## 📦 Dependencies

### Spam Predictor
- streamlit
- pandas
- scikit-learn
- matplotlib
- joblib

### Career Guide Chatbot (Backend)
- fastapi
- uvicorn[standard]
- sqlalchemy[asyncio]
- asyncpg
- python-dotenv
- pydantic-settings
- httpx
- google-generativeai

## 🔧 Key Technologies

- **ML Framework**: scikit-learn
- **Web Framework**: FastAPI & Streamlit
- **Database**: PostgreSQL with async SQLAlchemy
- **LLM**: Google Generative AI (Gemini)
- **Frontend**: Vanilla JavaScript, HTML, CSS

## 📝 Notes

- The spam predictor uses a trained ML model for classification
- The chatbot includes fallback mock responses when the Gemini API is unavailable
- Database migrations are handled manually (no Alembic setup)
- Both applications run independently and can be used separately

## 🔗 Repository

GitHub: https://github.com/Arvinth-23/Project-1
