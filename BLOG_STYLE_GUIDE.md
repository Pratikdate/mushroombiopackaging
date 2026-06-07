# 🍄 Mushroom Bio Packaging — Blog Style Guide

> **Keep this file open when writing any new blog post.**  
> Follow every rule here to ensure all articles look and feel identical to the rest of the site.

---

## 1. Fonts

The site loads **two Google Fonts**. You must never use any other font family inside blog content.

| Role | Font Family | CSS Value | When to Use |
|------|-------------|-----------|-------------|
| **Body / General text** | Assistant | `font-family: 'Assistant', sans-serif;` | All paragraphs, lists, captions, labels |
| **Display / Accent headers** | VT323 | `font-family: 'VT323', monospace;` | Big hero numbers, decorative step counters, pull-quotes |

### Google Fonts Import (already in `index.html`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;500;600;700&family=VT323&display=swap" rel="stylesheet">
```

> **Do NOT add this `<link>` tag inside individual blog `.html` files.** The fonts are already loaded globally by `index.html`.

---

## 2. Colours

Every blog post must use only these colours. Do not invent new hex codes.

| Name | Hex | Usage |
|------|-----|-------|
| **Charcoal (Primary)** | `#252729` | Main headings, strong text, dark backgrounds, button backgrounds |
| **Amber (Accent)** | `#c8842a` | Step numbers, highlighted labels, hover underlines, icon fills |
| **Off-white / Page bg** | `#f5f3ee` | Section backgrounds, card backgrounds |
| **Light grey** | `#f0ede6` | Alternate card/row shading |
| **Mid grey** | `#888` | Subheadings, captions, meta labels |
| **Body text** | `#444` | Normal paragraph text inside articles |
| **Muted text** | `#555` | Secondary paragraphs, intro lines |
| **Light text** | `#666` | Tertiary captions and small notes |
| **White** | `#fff` | Text on dark backgrounds, button labels on dark buttons |

---

## 3. Typography Scale

Use these sizes consistently. All sizes are in `px`.

| Element | Font Size | Font Weight | Line Height | Notes |
|---------|-----------|-------------|-------------|-------|
| Article hero title | `28–32px` | `300` | `1.3` | Charcoal `#252729`, letter-spacing `-0.01em` |
| Section heading (h2) | `22–26px` | `400` | `1.4` | Charcoal `#252729` |
| Sub-heading (h3) | `18–20px` | `600` | `1.4` | Charcoal `#252729` |
| Body paragraph | `16px` | `400` | `1.8` | Colour `#444` |
| Caption / meta label | `11–12px` | `600` | `1.5` | Uppercase, letter-spacing `0.15em`, colour `#888` |
| List items | `15–16px` | `400` | `1.75` | Colour `#555` |
| Step / accent number | `48–64px` | `400` | `1` | **VT323** font, colour `#c8842a` |
| Button text | `12px` | `700` | — | Uppercase, letter-spacing `0.1em` |

---

## 4. Blog Post HTML Structure

Every blog file lives inside `content/blogs/`. Each file is an **HTML fragment** — no `<html>`, `<head>`, or `<body>` tags. It is loaded directly into the dynamic viewer.

### Minimal template to copy-paste for a new blog:

```html
<div class="sp-reveal" style="font-size:16px; line-height:1.8; color:#444;">

  <!-- HERO TITLE -->
  <h1 style="font-size:28px; font-weight:300; color:#252729; letter-spacing:-0.01em; margin-bottom:8px;">
    Your Blog Title Here
  </h1>
  <p style="font-size:12px; font-weight:600; letter-spacing:0.15em; text-transform:uppercase; color:#888; margin-bottom:40px;">
    CATEGORY &nbsp;·&nbsp; Month Year
  </p>

  <!-- INTRO PARAGRAPH -->
  <p>
    Lead-in paragraph text. Keep it to 2–3 sentences that clearly state what the article covers.
  </p>

  <!-- SECTION HEADING -->
  <h2 style="font-size:22px; font-weight:400; color:#252729; margin-top:48px; margin-bottom:16px;">
    Section Heading
  </h2>

  <p>
    Body paragraph text goes here. Use colour <code>#444</code> and 1.8 line-height (set on the wrapper div above).
  </p>

  <!-- HIGHLIGHTED CALLOUT BOX -->
  <div style="background:#f5f3ee; border-left:4px solid #c8842a; padding:20px 24px; margin:32px 0; border-radius:0 6px 6px 0;">
    <strong style="color:#252729;">Key fact or callout.</strong>
    Supporting sentence that adds context.
  </div>

  <!-- STEP GRID (use when showing a numbered process) -->
  <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:24px; margin:40px 0;">

    <div style="background:#fff; border:1px solid #e8e4dc; border-radius:8px; padding:24px; text-align:center;">
      <div style="font-family:'VT323',monospace; font-size:48px; color:#c8842a; line-height:1;">01</div>
      <h3 style="font-size:14px; font-weight:700; color:#252729; margin:8px 0 6px; text-transform:uppercase; letter-spacing:0.08em;">Step Name</h3>
      <p style="font-size:13px; color:#666; margin:0; line-height:1.6;">Short description of this step.</p>
    </div>

    <!-- Repeat the card above for each step -->

  </div>

  <!-- CLOSING PARAGRAPH -->
  <p>
    Closing thoughts. Tie back to the company mission.
  </p>

</div>
```

---

## 5. Spacing Rules

| Context | Value |
|---------|-------|
| Between paragraphs | `margin-bottom: 24px` (browser default is fine; add explicitly if needed) |
| After hero title before body | `margin-bottom: 40px` |
| Before a new `<h2>` section | `margin-top: 48px` |
| Inside cards/boxes | `padding: 24px` |
| Between grid cards | `gap: 24px` |
| Callout box left border | `border-left: 4px solid #c8842a` |
| Max readable paragraph width | `max-width: 720px` (apply on wrapper or per-paragraph when needed) |

---

## 6. Buttons

There are two button styles. Never create custom button colours.

```html
<!-- PRIMARY — dark fill -->
<button style="background:#252729; color:#fff; padding:14px 32px; font-size:12px; font-weight:700;
               letter-spacing:0.1em; text-transform:uppercase; border:none; cursor:pointer; font-family:inherit;">
  Button Label
</button>

<!-- SECONDARY — outline -->
<button style="background:none; border:2px solid #252729; color:#252729; padding:13px 32px; font-size:12px;
               font-weight:700; letter-spacing:0.1em; text-transform:uppercase; cursor:pointer;
               font-family:inherit; transition:all 0.2s;">
  Button Label
</button>
```

---

## 7. Adding a New Blog Post — Step-by-Step

1. **Create the file**  
   Save your new HTML fragment as `content/blogs/your-slug.html`.  
   Use the template from §4 above.

2. **Register it in `index.html`**  
   Open `index.html`, find the `ARTICLE_METADATA` constant and add your entry:

   ```js
   'blog-your-slug': {
     type: 'blogs',
     file: 'your-slug',
     title: 'Your Blog Title',
     section: 'Blog'
   },
   ```

3. **Add a card to the Blog section**  
   Inside the `#sp-blog` section, copy an existing `.blog-card` block and update:
   - The `onclick` → `openArticle('blog-your-slug')`
   - The title, date, and description

4. **Test locally**  
   Run `python3 -m http.server 8000` in the project root, open `http://localhost:8000`, click your card, and verify the article loads correctly.

5. **Commit and push**  
   ```bash
   git add content/blogs/your-slug.html index.html
   git commit -m "blog: add <Your Blog Title>"
   git push
   ```
   GitHub Pages will deploy automatically within ~60 seconds.

---

## 8. Quick Checklist Before Publishing

- [ ] Font is **Assistant** for body text, **VT323** only for accent numbers
- [ ] All colours match the palette in §2 — no custom hex codes
- [ ] Article file is saved inside `content/blogs/` (not directly in root)
- [ ] `ARTICLE_METADATA` in `index.html` has a matching entry
- [ ] A card has been added in the Blog section with the correct `openArticle()` call
- [ ] Text has been proofread — no placeholder copy like "Lorem ipsum"
- [ ] Tested on `localhost:8000` before committing

---

*Last updated: June 2026*
