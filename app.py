import streamlit as st
from openai import OpenAI


MODEL = "gpt-4o-mini"

st.set_page_config(
    page_title="OpenAI 챗봇",
    page_icon="💬",
    layout="centered",
)

st.title("💬 OpenAI 챗봇")
st.caption(f"{MODEL} · Streamlit Community Cloud")


def get_api_key() -> str | None:
    """Read the API key from Streamlit secrets without exposing it in the UI."""
    try:
        return st.secrets["OPENAI_API_KEY"]
    except (KeyError, FileNotFoundError):
        return None


api_key = get_api_key()

with st.sidebar:
    st.subheader("설정")
    st.write(f"사용 모델: `{MODEL}`")
    if st.button("대화 초기화", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("API 키는 Streamlit Secrets에서 안전하게 읽습니다.")

if not api_key:
    st.error("OpenAI API 키가 설정되지 않았습니다.")
    st.info(
        "Streamlit Community Cloud의 앱 설정에서 Secrets를 열고 "
        '`OPENAI_API_KEY = "sk-..."` 형태로 추가해 주세요.'
    )
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 무엇을 도와드릴까요?",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=st.session_state.messages,
                stream=True,
                temperature=0.7,
            )
            response = st.write_stream(
                chunk.choices[0].delta.content
                for chunk in stream
                if chunk.choices and chunk.choices[0].delta.content
            )
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
        except Exception as exc:
            st.error(f"응답을 가져오지 못했습니다: {exc}")
