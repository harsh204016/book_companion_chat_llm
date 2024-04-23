
from main import response_generator
import streamlit as st
from streamlit_mic_recorder import speech_to_text


text = speech_to_text(language='en', use_container_width=False, just_once=True,
                           key='STT',start_prompt="⏺️", stop_prompt="⏹️")

print(text)

prompt = st.chat_input("Ask anything")    


js = f"""
    <script>
        function insertText() {{
            var chatInput = parent.document.querySelector('textarea[data-testid="stChatInput"]');
            var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, "value").set;
            nativeInputValueSetter.call(chatInput, "{prompt}");
            var event = new Event('input', {{ bubbles: true}});
            chatInput.dispatchEvent(event);
        }}
        insertText();
    </script>
    """
st.components.v1.html(js) 


# with st.chat_message("assistant"):
    # response = st.write_stream(response_generator())
# Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})


