import streamlit as st
from github_search import fetch_repositories
from rank_projects import rank_projects
from llm_summarizer import generate_summary
from user_manager import save_user_history, load_user_history



st.title('Project Plaza Recommender System')

username = st.text_input("Enter your username:")

if username:
    st.subheader(f"Welcome, {username}!")

    prompt = st.text_input("Describe the project you want:")

    if st.button("Find Projects"):
        if prompt:
            repos = fetch_repositories(prompt)

            if not repos:
                st.warning("No projects found. Try a different prompt!")
            else:
                ranked_projects = rank_projects(prompt, repos)

                st.subheader("🔎 All Projects (Ranked by Relevance):")
                for idx, (project, similarity) in enumerate(ranked_projects, 1):
                    st.markdown(f"**{idx}. [{project['name']}]({project['url']})**")
                    st.markdown(f"- {project['description']}")
                    st.markdown(f"- Similarity: `{similarity:.2f}`")
                    st.write("---")

                best_project, best_similarity = ranked_projects[0]
                reason = generate_summary(best_similarity)

                st.success("✅ Best Project Selected:")
                st.markdown(f"**[{best_project['name']}]({best_project['url']})**")
                st.markdown(f"- {best_project['description']}")
                st.markdown(f"**Reason:** {reason}")

                # Save history
                save_user_history(username, prompt, best_project)

    # Show past searches
    st.subheader("🕑 Past Searches:")
    history = load_user_history(username)
    if history:
        for item in history:
           # st.markdown(f"- **Prompt:** {item['prompt']}")
            st.markdown(f"  - **Best Project:** [{item['best_project']['name']}]({item['best_project']['url']})")
    else:
        st.write("No past searches yet.")