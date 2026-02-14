# TanLabs Portfolio

Welcome to the official repository for **TanLabs**, a personal portfolio and blog platform built with Python and Flask. This project showcases my work as a Security Analyst and AI Engineer, featuring a dynamic blog, project portfolio, and professional profile.

## 🚀 Features

*   **Dynamic Portfolio**: Showcase projects with detailed descriptions, tech stacks, and links.
*   **Markdown Blog**: Write blog posts in Markdown with support for code blocks, tables, and images.
*   **Responsive Design**: Modern, mobile-friendly UI built with Tailwind CSS.
*   **Project Details**: Dedicated pages for deep-diving into specific projects.
*   **About Page**: specific page to showcase professional bio and social links.

## 🛠️ Tech Stack

*   **Backend**: Python, Flask
*   **Frontend**: HTML5, Tailwind CSS
*   **Data**: JSON/Internal Data Structures (No SQL database required for this version)
*   **Rendering**: Jinja2 Templating
*   **Blog Engine**: `markdown` + `python-frontmatter`

## 📦 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Tan-w/tanlabs-portfolio.git
    cd tanlabs-portfolio
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, install manually: `pip install flask markdown python-frontmatter`)*

4.  **Run the application**:
    ```bash
    python app.py
    ```

5.  **Visit**: Open http://127.0.0.1:5000 in your browser.

## 📝 Adding Content

*   **Blog Posts**: Add new `.md` files to the `posts/` directory. Ensure they have the correct frontmatter (title, date, description).
*   **Projects**: Update the `projects_data` list in `app.py`.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
