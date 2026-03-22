def generate_roadmap(role):
    data = {
        "Frontend Developer": [
            "HTML, CSS, JavaScript",
            "React.js",
            "Version Control (Git)",
            "Projects + Portfolio"
        ],
        "Backend Developer": [
            "Python / Node.js",
            "Databases (MySQL, MongoDB)",
            "API Development",
            "Deployment"
        ],
        "AI Engineer": [
            "Python",
            "Machine Learning Basics",
            "Deep Learning",
            "Projects"
        ]
    }
    return data.get(role, ["No roadmap available"])
