# SuperDesign Project Template

This template provides a complete workflow for building and deploying static websites using **SuperDesign** for UI iteration and **GitHub + Cloudflare Pages** for deployment.

---

## ⚡ Quick Start (60 Sekunden)

**👉 Lies zuerst:** `START-HERE.md`

---

## Quick Start (English)

### 1. Copy Template to New Project
```bash
# Create new project directory
mkdir my-new-project
cd my-new-project

# Copy template files
cp -r /path/to/TEMPLATE/* .
cp -r /path/to/TEMPLATE/.cursor .
```

### 2. Initialize SuperDesign Structure
```bash
# Create SuperDesign working directory
mkdir -p .superdesign/design_iterations

# Create initial project structure
mkdir -p css js images
```

### 3. Start Designing
- Open Cursor/VS Code
- Run: `Ctrl/Cmd + Shift + P` → `SuperDesign: Open Canva`
- Tell the agent: "Design [your UI idea]"
- The agent will follow the 4-step workflow automatically

### 4. Initialize Git
```bash
git init
git add .
git commit -m "Initial commit from SuperDesign template"
```

---

## What's Included

### Workflow Documentation
- **SUPERDESIGN-WORKFLOW.md**: Complete SuperDesign design process (4 steps)
- **SUPERDESIGN-TO-PRODUCTION.md**: Deployment guide (GitHub → Cloudflare)
- **CURSOR-ROLES.md**: AI agent behavior (Architect → Implementer → QA → Release)
- **QUALITY-GATES.md**: Pre-merge checklist and QA standards

### Cursor Rules
- **.cursor/rules/design.mdc**: SuperDesign agent instructions (already included in template)

---

## Project Structure (After Setup)

```
my-new-project/
├── .superdesign/
│   └── design_iterations/      # SuperDesign prototypes go here
│       ├── ui_1.html
│       ├── ui_1_1.html
│       └── theme_1.css
├── .cursor/
│   └── rules/
│       └── design.mdc          # SuperDesign agent rules
├── css/
│   ├── reset.css               # CSS reset (optional)
│   ├── variables.css           # Theme variables (from SuperDesign)
│   ├── base.css                # Base styles
│   └── main.css                # Component styles
├── js/
│   ├── main.js                 # Core interactions
│   └── components.js           # Feature-specific logic
├── images/                     # Optimized images
├── index.html                  # Main HTML file
├── _headers                    # Cloudflare caching rules (optional)
├── _redirects                  # Cloudflare routing rules (optional)
├── .gitignore
├── SUPERDESIGN-WORKFLOW.md
├── SUPERDESIGN-TO-PRODUCTION.md
├── CURSOR-ROLES.md
└── QUALITY-GATES.md
```

---

## Workflow Overview

### Phase 1: Design (SuperDesign)
1. Open SuperDesign canvas
2. Agent creates layout (ASCII wireframe)
3. Agent generates theme (CSS variables)
4. Agent defines animations (micro-syntax)
5. Agent builds HTML prototype in `.superdesign/design_iterations/`

### Phase 2: Adapt (Production)
1. Extract styles from prototype → `css/`
2. Extract scripts from prototype → `js/`
3. Fix asset paths (relative)
4. Optimize images
5. Test locally in browser

### Phase 3: Deploy (GitHub → Cloudflare)
1. Commit and push to GitHub
2. Cloudflare auto-deploys preview URL
3. Test preview URL (QA checklist)
4. Merge to `main` → Production deploy
5. Monitor production for errors

---

## Key Commands

### SuperDesign
```
Ctrl/Cmd + Shift + P → SuperDesign: Open Canva
```

### Git Workflow
```bash
# Start new feature
git checkout -b feature/new-design

# Commit changes
git add .
git commit -m "Add new hero section design"

# Push to GitHub (triggers Cloudflare preview)
git push origin feature/new-design

# After PR approval, merge to main
git checkout main
git merge feature/new-design
git push origin main
```

---

## Quality Gates

Before merging to production:

- [ ] No console errors
- [ ] No 404/500 errors
- [ ] Preview URL manually tested
- [ ] Responsive on mobile/tablet/desktop
- [ ] Lighthouse Performance > 90
- [ ] Lighthouse Accessibility > 90
- [ ] All interactive elements working
- [ ] Images optimized

See **QUALITY-GATES.md** for full checklist.

---

## Cloudflare Pages Setup

### First-Time Setup
1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com) → Pages
2. Click "Create a project" → "Connect to Git"
3. Select your GitHub repository
4. Configure build settings:
   - **Framework preset**: None (or Static HTML)
   - **Build command**: (leave empty)
   - **Build output directory**: `/` (root)
5. Click "Save and Deploy"

### Automatic Deployments
- **Push to `main`**: Deploys to production (`your-site.pages.dev`)
- **Open PR**: Creates preview URL (`abc123.your-site.pages.dev`)
- **Update PR**: Preview URL updates automatically

---

## Common Issues & Solutions

### Problem: Agent doesn't follow SuperDesign workflow
**Solution**: Make sure `.cursor/rules/design.mdc` exists and SuperDesign extension is installed

### Problem: Assets not loading on Cloudflare
**Solution**: Use relative paths (`./css/main.css`) instead of absolute (`/css/main.css`)

### Problem: Fonts not rendering
**Solution**: Check Google Fonts URL and add `<link rel="preconnect">`

### Problem: SuperDesign designs look different in production
**Solution**: Extract inline styles to external CSS files, keep CDN scripts

---

## Customization

### Add Custom Fonts
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Your+Font&display=swap" rel="stylesheet">
```

### Add Cloudflare Caching
Create `_headers` file:
```
/css/*
  Cache-Control: public, max-age=31536000, immutable
```

### Add Redirects
Create `_redirects` file:
```
/old-page    /new-page    301
```

---

## Best Practices

### Design Phase
- ✅ Iterate quickly in SuperDesign (don't worry about production structure yet)
- ✅ Get user approval at each step (Layout → Theme → Animation → HTML)
- ✅ Fork designs to explore multiple directions

### Development Phase
- ✅ Keep commits small and focused
- ✅ Test locally before pushing
- ✅ Document assumptions in code comments
- ✅ Use relative paths for all local assets

### Deployment Phase
- ✅ Always test preview URL before merging
- ✅ Run Lighthouse audit on preview
- ✅ Monitor production after deploy
- ✅ Keep PRs small (easier to review and revert)

---

## Support & Resources

- **SuperDesign**: [GitHub](https://github.com/superdesigndev/superdesign) | [Website](https://superdesign.dev/ide-extension)
- **Cloudflare Pages**: [Documentation](https://developers.cloudflare.com/pages/)
- **Workflow Docs**: See files in this directory

---

## License

This template is free to use for any project. No attribution required.

---

## Next Steps

1. **Copy this template** to your new project
2. **Initialize SuperDesign** structure (`.superdesign/design_iterations/`)
3. **Tell the agent**: "Design [your UI idea]"
4. **Let the workflow guide you**: Architect → Implementer → QA → Release

Happy building! 🚀

