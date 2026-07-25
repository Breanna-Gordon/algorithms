import marimo

__generated_with = "0.18.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objs as go
    import random
    return go, mo, np, random


@app.cell
def _(mo):
    mo.md(
        r"""
# Breanna Gordon
### Computer Science Student @ UAL 

London | bregordonhelen3@gmail.com |
LinkedIn : https://www.linkedin.com/in/breanna-gordon-b77b33269/ | GitHub : https://github.com/Breanna-3
"""
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
## About Me

Motivated Computer Science student at UAL who loves turning ideas into code. I stay calm when things break, learn fast, and enjoy solving problems. Whether it's debugging code or managing a group of energetic kids, I bring a reliable and friendly approach to everything I do. Currently seeking opportunities to gain real-world experience and make a positive impact.
"""
    )
    return





@app.cell
def _(mo):
    fun_fact = mo.ui.dropdown(
        options=[
            "Click to learn something fun about me!",
            "I paint in my free time (traditional and digital).",
            "I play chess and enjoy it casually.",
            "Dystopian stories are my favorite genre across books, games, and films (Detroit: Become Human, Cyberpunk 2077, and The Hunger Games are repeat favorites).",
            "I enjoy games as a way to unwind with friends.",
            "Professional babysitter since 2021 (patience level: expert).",
            "Sitcom fan (The Office, Parks & Rec, Brooklyn 99, The Good Place, Community, Abbott Elementary).",
            "Manga/manhua/manwha and comics fan (Solo Leveling, Omniscient Reader’s Viewpoint, Elceed, and more).",
            "Bob's Burgers is my comfort show.",
        ],
        value="Click to learn something fun about me!",
        label="Fun facts about me",
    )
    fun_fact
    return fun_fact


@app.cell
def _(fun_fact, mo):
    if fun_fact.value != "Click to learn something fun about me!":
        mo.md(
            f"""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px; border-radius: 15px; text-align: center; margin: 15px 0;
            animation: slideIn 0.5s ease-out;">
  <p style="color: white; font-size: 1.1em; margin: 0;">
    {fun_fact.value}
  </p>
</div>

<style>
@keyframes slideIn {{
  from {{ transform: translateY(-20px); opacity: 0; }}
  to {{ transform: translateY(0); opacity: 1; }}
}}
</style>
"""
        )
    else:
        mo.md("")
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
## Skills
Click a category to explore:
"""
    )
    return


@app.cell
def _(mo):
    
    skill_category = mo.ui.tabs(
        {
            "Tech": "Technical Skills",
            "Soft": "Soft Skills",
            "Creative": "Creative Skills",
        }
    )
    skill_category
    return skill_category


@app.cell
def _(mo, skill_category):
    skill_sets = {
        "Tech": {
            "Python": 70,
            "JavaScript": 80,
            "HTML/CSS": 72,
            "Web Development": 85,
            "Data Entry": 60,
            "Git/GitHub": 70,
        },
        "Soft": {
            "Organisation": 52,
            "Communication": 70,
            "Teamwork": 70,
            "Problem Solving": 72,
            "Time Management": 60,
            "Enthusiasm": 68,
        },
        "Creative": {
            "Painting": 65,
            "UI/UX Design": 50,
            "Chess Strategy": 50,
            "Creative Thinking": 60,
            "Attention to Detail": 80,
        },
    }

    selected_skills = skill_sets.get(skill_category.value, skill_sets["Tech"])

    skills_html = "<div style='margin: 20px 0;'>"
    for skill, level in selected_skills.items():
        color = "#667eea" if level >= 85 else "#4facfe" if level >= 70 else "#f093fb"
        skills_html += f"""
<div style="margin: 15px 0;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
    <strong>{skill}</strong>
    <span>{level}%</span>
  </div>
  <div style="background: #e0e0e0; border-radius: 10px; height: 20px; overflow: hidden;">
    <div style="background: linear-gradient(90deg, {color} 0%, {color}dd 100%);
                width: {level}%; height: 100%; border-radius: 10px;
                transition: width 0.5s ease-out;">
    </div>
  </div>
</div>
"""
    skills_html += "</div>"

    mo.md(skills_html)
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Education Journey""")
    return


@app.cell
def _(mo):
    
    education_tab = mo.ui.tabs(
        {
            "university": "University (Current)",
            "sixth_form": "Sixth Form",
            "secondary": "Secondary School",
        }
    )
    education_tab
    return education_tab


@app.cell
def _(education_tab, mo):
    education_info = {
        "university": """
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 25px; border-radius: 15px; margin: 20px 0; color: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
  <h2 style="margin-top: 0;">University of the Arts London (UAL)</h2>
  <h3>BSc Computer Science | 2024 – Present</h3>
  <ul>
    <li>Software Engineering & Development</li>
    <li>Data Structures & Algorithms</li>
    <li>Web Technologies</li>
    <li>Creative Coding Projects</li>
  </ul>
  <p><strong>Status:</strong> Building projects, learning daily.</p>
</div>
""",
        "sixth_form": """
<div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            padding: 25px; border-radius: 15px; margin: 20px 0; color: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
  <h2 style="margin-top: 0;">City and Islington Sixth Form College</h2>
  <h3>A-Levels | 2022 – 2024</h3>
  <ul>
    <li>Computer Science - <strong>B</strong></li>
    <li>English - <strong>B</strong></li>
    <li>Electronics - <strong>C</strong></li>
  </ul>
</div>
""",
        "secondary": """
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 25px; border-radius: 15px; margin: 20px 0; color: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
  <h2 style="margin-top: 0;">Copthall Secondary School</h2>
  <h3>GCSEs | 2017 – 2022</h3>
  <ul>
    <li>Maths - <strong>Grade 6</strong></li>
    <li>English - <strong>Grade 7</strong></li>
    <li>Science - <strong>Grade 7</strong></li>
  </ul>
</div>
""",
    }

    mo.md(education_info.get(education_tab.value, education_info["university"]))
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Experience""")
    return


@app.cell
def _(mo):
    # IMPORTANT: no options= in marimo 0.18.1
    experience_tabs = mo.ui.tabs(
        {
            "babysitting": "Babysitting",
            "web_dev": "Web Development",
        }
    )
    experience_tabs
    return experience_tabs


@app.cell
def _(experience_tabs, mo):
    experience_content = {
        "babysitting": """
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 25px; border-radius: 15px; margin: 20px 0; color: white;">
  <h2 style="margin-top: 0;">Professional Babysitter</h2>
  <p style="font-style: italic;">Private Families | 2021 – Present</p>
  <ul>
    <li>Dependable childcare for children aged 3–10</li>
    <li>Meal prep, homework help, bedtime routines</li>
    <li>Built trust with families and kept kids safe</li>
    <li><strong>Frequently rebooked</strong></li>
  </ul>
</div>
""",
        "web_dev": """
<div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 25px; border-radius: 15px; margin: 20px 0; color: white;">
  <h2 style="margin-top: 0;">Web Development</h2>
  <p style="font-style: italic;">Personal Projects | 2023 – Present</p>
  <ul>
    <li>Responsive websites using HTML, CSS, and JavaScript</li>
    <li>Accessible layouts and clean UI</li>
    <li>Improved UX with interactive elements</li>
  </ul>
</div>
""",
    }

    mo.md(experience_content.get(experience_tabs.value, experience_content["babysitting"]))
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _(mo):
    mo.md(r"""## My Coding Journey""")
    return


@app.cell
def _(go, mo):
    years = [2021, 2022, 2023, 2024, 2025]
    python_skills = [0, 20, 45, 50, 65]
    web_skills = [10, 35, 40, 45, 50]
    problem_solving = [30, 50, 65, 67, 75]
    communication = [60, 70, 75, 76, 78]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=years,
            y=python_skills,
            mode="lines+markers",
            name="Python",
            hovertemplate="<b>Python</b><br>Year: %{x}<br>Level: %{y}%<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=years,
            y=web_skills,
            mode="lines+markers",
            name="Web Development",
            hovertemplate="<b>Web Dev</b><br>Year: %{x}<br>Level: %{y}%<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=years,
            y=problem_solving,
            mode="lines+markers",
            name="Problem Solving",
            hovertemplate="<b>Problem Solving</b><br>Year: %{x}<br>Level: %{y}%<extra></extra>",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=years,
            y=communication,
            mode="lines+markers",
            name="Communication",
            hovertemplate="<b>Communication</b><br>Year: %{x}<br>Level: %{y}%<extra></extra>",
        )
    )

    fig.update_layout(
        title="Skills Development Over Time",
        xaxis_title="Year",
        yaxis_title="Proficiency Level (%)",
        yaxis=dict(range=[0, 100]),
        hovermode="x unified",
        height=450,
        showlegend=True,
        legend=dict(orientation="h", y=1.02, x=1, xanchor="right", yanchor="bottom"),
    )

    mo.ui.plotly(fig)
    return


@app.cell
def _(mo):
    mo.md(r"""---""")
    return


@app.cell
def _(mo):
    mo.md(r"""## My Personality Profile""")
    return


@app.cell
def _(go, mo):
    personality_traits = {
        "Creativity": 60,
        "Logic": 70,
        "Patience": 88,
        "Enthusiasm": 75,
        "Adaptability": 79,
        "Humor": 70,
    }

    fig_personality = go.Figure()
    fig_personality.add_trace(
        go.Scatterpolar(
            r=list(personality_traits.values()),
            theta=list(personality_traits.keys()),
            fill="toself",
            name="Personality",
            line=dict(width=2),
            fillcolor="rgba(102, 126, 234, 0.35)",
        )
    )

    fig_personality.update_layout(
        title="Personality Radar",
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        height=420,
    )

    mo.ui.plotly(fig_personality)
    return


if __name__ == "__main__":
    app.run()
