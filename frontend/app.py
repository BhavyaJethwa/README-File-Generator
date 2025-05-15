import streamlit as st
import requests

st.title("📄 GitHub README Generator")

repo_url = st.text_input("🔗 Enter GitHub repository URL:")

# Note to the user
st.markdown("⚠️ **Note:** The repository must be **public** for this tool to access it.")

status_text = st.empty()
if st.button("🚀 Get README"):
    if repo_url:
        with st.spinner("Generating README..."):
            status_text.text("🛠️ Generating README...")
            response = requests.post(
                "http://localhost:8000/generate_readme",  # Backend URL
                json={"repo_url": repo_url}
            )
            if response.status_code == 200:
                readme_content = response.json()["readme"]
                status_text.text("Completed generating readme 🎉")
                st.download_button(
                    label="📥 Download README.md",
                    data=readme_content,
                    file_name="README.md",
                    mime="text/markdown"
                )
            else:
                st.error("❌ Failed to generate README. Try again.")
    else:
        st.warning("⚠️ Please enter a GitHub URL.")



