**Repository Overview**
- **Backend:** FastAPI app in `backend/app/`.
- **Frontend:** Static UI in `frontend/` (`index.html`, `app.js`, `style.css`).

**Big-picture architecture**
- HTTP frontend -> `frontend/app.js` calls backend `/chat/` endpoint.
- Two chat implementations exist:
  - `backend/app/main.py`: simple, in-memory chat (uses UUID `session_id`, returns `{reply, session_id, status}`).
  - `backend/app/routes/chat.py`: DB-backed chat using async SQLAlchemy models in `backend/app/models.py` and `backend/app/schemas.py` (returns `ChatResponse`).
- LLM integration is implemented in `backend/app/services/llm.py` using `google.generativeai` (Gemini). It includes robust fallback `MOCK_RESPONSES` when the API fails.

**Key files to inspect first**
- `backend/app/main.py` — quick local server & minimal flow (good for fast iteration).
- `backend/app/routes/chat.py` — production-style flow storing sessions/messages in DB.
- `backend/app/services/llm.py` — LLM calls, model selection, and fallback behavior.
- `backend/app/config.py` — pydantic `Settings`; reads `.env` at `backend/.env`.
- `backend/app/database.py` & `backend/app/models.py` — async SQLAlchemy engine and table definitions.
- `frontend/app.js` — shows client expectations: POST `/chat/` with `{user_id,message,session_id}` and expects `data.reply` + `data.session_id`.

**Developer workflows & run commands**
- Install deps and run backend (from project root):

  cd backend
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  # start server
  venv/bin/python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

- Frontend: open `frontend/index.html` in a browser (it talks to `http://127.0.0.1:8000`).
- Quick API test (example):

  curl -X POST http://127.0.0.1:8000/chat/ \
    -H "Content-Type: application/json" \
    -d '{"user_id":1,"message":"What are the best AI careers?"}'

**Environment & secrets**
- `backend/.env` is used by `config.Settings`.
- Important variables: `GEMINI_API_KEY`, `DATABASE_URL` (format: `postgresql+asyncpg://user:pass@host/dbname`), `SECRET_KEY`.

**Project-specific patterns & gotchas**
- Async SQLAlchemy: `database.py` creates an `AsyncSession` with `create_async_engine`. Use `AsyncSession` in routes and `await` DB operations.
- Two chat implementations coexist — be explicit which you modify: `main.py` (in-memory, string `session_id`) vs `routes/chat.py` (DB, integer `session_id`). Schemas and frontend assume slightly different session_id types.
- `services/llm.py` uses `google.generativeai` (Gemini). It calls `list_models()` and `GenerativeModel.start_chat()`; any failures fall back to keyword-matching `MOCK_RESPONSES`.
- No migration tooling included (no Alembic). If you change DB models, create tables manually or add migrations.
- `voice.py` is a standalone CLI voice assistant with heavy dependencies (speech_recognition, pyttsx3) and is not wired to the web API.

**Testing & debugging tips**
- If local LLM calls fail, `services/llm.py` prints exceptions and returns a mock reply — useful for offline dev.
- For DB issues, enable `DATABASE_URL` to a local Postgres and inspect `engine` logs (`echo=True`).
- Frontend will consider any non-2xx response as an error; ensure backend returns JSON with `reply` and `session_id`.

If anything here is unclear or you want this tailored (e.g., add migration steps, CI commands, or test examples), tell me which area to expand.
