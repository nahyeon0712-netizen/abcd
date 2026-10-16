# OpenAI Streamlit 챗봇

`gpt-4o-mini`를 사용하는 간단한 한국어 챗봇입니다. OpenAI 응답은 스트리밍으로 화면에 표시됩니다.

## 로컬 실행

```bash
pip install -r requirements.txt
streamlit run app.py
```

로컬 테스트를 위해 `.streamlit/secrets.toml` 파일을 만들고 다음처럼 설정하세요.

```toml
OPENAI_API_KEY = "sk-..."
```

`.streamlit/secrets.toml`은 절대 Git에 커밋하지 마세요.

## Streamlit Community Cloud 배포

1. GitHub 저장소에 `app.py`, `requirements.txt`를 업로드합니다.
2. Streamlit Community Cloud에서 앱을 배포합니다.
3. 앱의 **Settings → Secrets**에 다음을 입력합니다.

```toml
OPENAI_API_KEY = "sk-..."
```

4. 앱의 Main file path를 `app.py`로 지정합니다.
