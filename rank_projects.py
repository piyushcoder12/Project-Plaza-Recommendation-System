# rank_projects.py

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_projects(prompt, projects):
    prompt_embedding = model.encode(prompt, convert_to_tensor=True)

    ranked = []
    for project in projects:
        project_text = f"{project['name']}. {project['description']}"
        project_embedding = model.encode(project_text, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(prompt_embedding, project_embedding).item()
        ranked.append((project, similarity))

    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked