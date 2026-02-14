
import os
import markdown
import frontmatter
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
# SECURITY: Change this in production! Use an environment variable.
app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_DO_NOT_USE_IN_PRODUCTION')

@app.route("/")
def home():
    return render_template("index.html")

# Sample Data for Projects
projects_data = [
    {
        "id": 1,
        "title": "Secure AI Pipeline",
        "description": "An end-to-end MLOps pipeline with built-in security scanning for model vulnerabilities.",
        "long_description": "We build a secure pipeline for deploying machine learning models. This includes automated scanning for vulnerabilities in model dependencies and input validation layers to prevent adversarial attacks.",
        "tech": ["Python", "Docker", "TensorFlow", "Snyk"],
        "link": "#"
    },
    {
        "id": 2,
        "title": "Threat Intel Dashboard",
        "description": "Real-time visualization of cyber threats using open-source intelligence feeds.",
        "long_description": "A comprehensive dashboard that aggregates threat intelligence from multiple sources. It displays real-time attack maps, top threat actors, and emerging vulnerabilities.",
        "tech": ["React", "D3.js", "FastAPI", "PostgreSQL"],
        "link": "#"
    },
    {
        "id": 3,
        "title": "Automated Penetration Tool",
        "description": "A CLI tool that automates reconnaissance and basic vulnerability scanning for authorized audits.",
        "long_description": "Designed for security professionals, this CLI tool automates the initial phases of penetration testing. It performs subdomain enumeration, port scanning, and basic service fingerprinting.",
        "tech": ["Go", "Bash", "Nmap"],
        "link": "#"
    },
    {
        "id": 4,
        "title": "Cloud Compliance Bot",
        "description": "Serverless bot that automatically remediates non-compliant AWS resources.",
        "long_description": "This serverless application monitors AWS infrastructure for compliance violations. It can automatically tag resources, encrypt buckets, or restrict security groups based on predefined policies.",
        "tech": ["AWS Lambda", "Python", "Boto3", "Terraform"],
        "link": "#"
    },
    {
        "id": 5,
        "title": "Zero Trust Network Auth",
        "description": "Implementation of a zero-trust authentication gateway for microservices.",
        "long_description": "A robust authentication gateway that enforces mutual TLS between microservices. It integrates with OIDC providers for user identity propagation and fine-grained access control.",
        "tech": ["Rust", "gRPC", "mTLS", "OIDC"],
        "link": "#"
    },
    {
        "id": 6,
        "title": "Personal Finance Tracker",
        "description": "Privacy-focused finance tracker that runs entirely locally with encrypted backups.",
        "long_description": "A desktop application for tracking finances without sharing data with third parties. It features local database storage, encrypted backups, and insightful spending visualizations.",
        "tech": ["Electron", "React", "SQLite"],
        "link": "#"
    }
]

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_data)

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    project = next((p for p in projects_data if p["id"] == project_id), None)
    if project:
        return render_template("project_detail.html", project=project)
    return "Project not found", 404

@app.route("/blog")
def blog():
    posts = []
    posts_dir = os.path.join(app.root_path, 'posts')
    if os.path.exists(posts_dir):
        for filename in os.listdir(posts_dir):
            if filename.endswith('.md'):
                filepath = os.path.join(posts_dir, filename)
                post = frontmatter.load(filepath)
                posts.append({
                    'slug': filename[:-3],
                    'title': post.get('title', 'Untitled'),
                    'date': post.get('date'),
                    'description': post.get('description', '')
                })
        # Sort posts by date, newest first
        posts.sort(key=lambda x: str(x['date']) if x['date'] else '', reverse=True)
    return render_template("blog.html", posts=posts)

@app.route("/blog/<slug>")
def blog_post(slug):
    posts_dir = os.path.join(app.root_path, 'posts')
    filepath = os.path.join(posts_dir, f"{slug}.md")
    
    if not os.path.exists(filepath):
        return "Post not found", 404
        
    post = frontmatter.load(filepath)
    content = markdown.markdown(post.content, extensions=['tables', 'fenced_code'])
    
    post_data = {
        'title': post.get('title', 'Untitled'),
        'date': post.get('date'),
        'description': post.get('description', ''),
        'content': content
    }
    
    return render_template("blog_post.html", post=post_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Here you would typically send an email
        # For now, we'll just print to the console
        print(f"New Message from {name} ({email}): {message}")
        
        flash("Thanks for reaching out! I'll get back to you soon.", "success")
        return redirect(url_for("contact"))
        
    return render_template("contact.html")

# @app.route("/products")
# def products():
#     return render_template("products.html")

if __name__ == "__main__":
    dev_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=dev_mode)
