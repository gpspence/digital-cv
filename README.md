# digital-cv

A modern, web-based digital CV to showcase professional background, skills, and projects.

## 🌟 Features

- **Attractive design:** CVs presented with clean, responsive HTML and CSS.
- **Easy customization:** All content is editable via simple markup—no frameworks required.
- **Portable:** Works locally or can be hosted anywhere (GitHub Pages, Netlify, etc.).
- **Printable:** Optimized for both screen and print (PDF export via browser print).

## 🗂️ Repository Structure

```
digital-cv/
├── index.html             # Main CV
├── index_template.html    # CV template
├── generate_portfolio.py  # Python script to generate CV from template
├── portfolio.json         # Content to fill into template 
├── css/                   # Custom styles
├── img/                   # Images
├── README.md
├── LICENSE.txt
```

## 🚀 Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/gpspence/digital-cv.git
   cd digital-cv
   ```

2. **Open `index.html` in your browser** to view the CV.

3. **Edit `portfolio.json`, `index_template.html` and `style.css`** to add details and personalize the look.

4. **Run `generate_portfolio.py`** to update index.html with the latest data and styling.

## 🛠️ Customization Tips

- Update personal information, work experience, skills, and projects in `portfolio.json`.
- Tweak colors, fonts, and layout in `css/main.css`.
- Place photos or icons in the `images/` folder and reference them in your HTML.

## 💡 Deployment

- **GitHub Pages:**  
  1. In repository settings, enable Pages for your selected branch.
  2. Visit `https://gpspence.github.io/digital-cv/` to see your live CV.

- **Other hosts:**  
  Upload the files to your preferred web host or serve locally.

## 📄 License

MIT License — free for personal and commercial use.

---

**Built by [gpspence](https://github.com/gpspence)**