
import gradio as gr

users = {}
current_user = None

class User:
    def __init__(self, id):
        self.id = id
        self.points = 0
        self.skills_offered = []
        self.skills_requested = []

    def add_points(self, amount):
        self.points += amount

def login(username):
    global current_user
    if username not in users:
        users[username] = User(username)
    current_user = users[username]
    return f"Welcome {username}! You have {current_user.points} points."

def add_skill(skill_name):
    if current_user:
        current_user.skills_offered.append(skill_name)
        return f"Skill '{skill_name}' added."
    return "Please log in first."

def request_skill(skill_name):
    if current_user:
        current_user.skills_requested.append(skill_name)
        return f"Requested skill: '{skill_name}'."
    return "Please log in first."

def find_matching_skills():
    if current_user:
        matches = []
        for user in users.values():
            if user != current_user:
                common = set(current_user.skills_requested).intersection(user.skills_offered)
                if common:
                    matches.append(f"{user.id}: {', '.join(common)}")
        return "\n".join(matches) if matches else "No matches found."
    return "Please log in first."

def complete_swap():
    if current_user:
        current_user.add_points(10)
        return f"Swap completed. You earned 10 points. Total: {current_user.points}"
    return "Please log in first."

with gr.Blocks() as demo:
    gr.Markdown("# 🤝 Swaply: Skill Exchange Platform")

    with gr.Row():
        username_input = gr.Textbox(label="Username")
        login_button = gr.Button("Login")
    login_output = gr.Textbox(label="Login Result")
    login_button.click(fn=login, inputs=username_input, outputs=login_output)

    with gr.Row():
        skill_input = gr.Textbox(label="Skill to Offer")
        add_button = gr.Button("Add Skill")
    add_output = gr.Textbox(label="Add Skill Result")
    add_button.click(fn=add_skill, inputs=skill_input, outputs=add_output)

    with gr.Row():
        request_input = gr.Textbox(label="Skill to Request")
        request_button = gr.Button("Request Skill")
    request_output = gr.Textbox(label="Request Result")
    request_button.click(fn=request_skill, inputs=request_input, outputs=request_output)

    match_button = gr.Button("Find Matches")
    match_output = gr.Textbox(label="Matches")
    match_button.click(fn=find_matching_skills, outputs=match_output)

    complete_button = gr.Button("Complete Swap")
    complete_output = gr.Textbox(label="Points")
    complete_button.click(fn=complete_swap, outputs=complete_output)

demo.launch()
