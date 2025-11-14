## Bäcker & Charlie · Brand Asset Map

### 1. Inventory Snapshot

- **Primary logo – horizontal (full colour)**  
  `Styleguide SVGs und co/FULL COLOUR- PRIMARY LOGO TYPE - HORIZONTAL/PNG/PNG---RED---PRIMARY-LOGO-TYPE----HORIZONTAL.png`  
  `Styleguide SVGs und co/FULL COLOUR- PRIMARY LOGO TYPE - HORIZONTAL/PNG/PNG--YELLOW--PRIMARY-LOGO-TYPE----HORIZONTAL.png`

- **Primary logo – stacked (full colour)**  
  `Styleguide SVGs und co/STACKED- PRIMARY LOGO TYPE/PNG/` → 4 PNG variants (red, yellow, reversed, outline)

- **Monogram (colour)**  
  `Styleguide SVGs und co/MONOGRAM/COLOUR MONOGRAM/PNG/PNG--RED--COLOUR---MONOGRAM.png`  
  `Styleguide SVGs und co/MONOGRAM/COLOUR MONOGRAM/PNG/PNG--RED-&-YELLOW---COLOUR---MONOGRAM.png`

- **Secondary branding unit (colour)**  
  `Styleguide SVGs und co/SECONDARY BRANDING UNIT/COLOUR/PNG/PNG--RED-COLOUR----SECONDARY-BRANDING-UNIT.png`  
  `Styleguide SVGs und co/SECONDARY BRANDING UNIT/COLOUR/PNG/PNG--YELLOW--COLOUR---SECONDARY-BRANDING-UNIT.png`

- **Branding stripes**  
  `Styleguide SVGs und co/BRANDING STRIPES/JUST STRIPES/JPEG/STRIPES-WITHOUT--BRANDING.jpg`  
  `Styleguide SVGs und co/BRANDING STRIPES/STRIPES WITH BRANDING/JPEG/STRIPES-WITH-BRANDING.jpg`

- **Typography locks**  
  `Styleguide SVGs und co/TYPOGRAPHY ASSETS/HANDCRAFTED - TYPOGRAPHY ASSETS/PNG/HANDCRAFTED-TYPO-*.png` (black, red, yellow, white)  
  Additional slogan sets live in sibling folders (`FROM BERLIN TO BENGALURU`, `A LITTLE TASTE ...`, `GUTEN MORGEN MAGA!`).

- **Illustrative elements**  
  `Styleguide SVGs und co/INDIVIDUAL -ILLUSTRATIVE ELEMENTS - FROM MONOGRAM/RED/PNG/*` (pretzel, wheat, cloud, etc.) and identical yellow/B&W sets.

- **Bear merch icons**  
  `Styleguide SVGs und co/MERCH - BEAR - FROM CONCEPT 2/BEAR NO BACKGROUND OR CIRCLE/PNG/*.png`  
  `Styleguide SVGs und co/MERCH - BEAR - FROM CONCEPT 2/MERCH - BEAR IN CIRCLE/PNG/*.png`

- **Copy fonts**  
  `Styleguide SVGs und co/B&C - COPY FONT - DOWNLOAD & INSTALL BEFORE USING/ALRIGHTSANS-*.OTF`


### 2. Placement & Sizing Guidelines

| Section | Asset | Notes |
| --- | --- | --- |
| Hero masthead | Full-colour horizontal logo (red) + Handcrafted typography png | Logo max-width 320px on desktop (180px mobile). Typography lock sits below headline at ~220px width with `mix-blend-mode: screen`. |
| Hero CTA badges | Secondary branding unit (yellow) | Use 160px-wide inline image ahead of CTA copy, `loading="lazy"` and `aria-hidden="true"` if decorative. |
| Menu sidebar (sticky) | Colour monogram PNG | Float top-left of category list, 96px square on desktop, 64px mobile. |
| Menu/product cards | Illustrative icons (pretzel, wheat, cloud) | Pair with category filter chips as subtle background watermark (opacity 0.15, size 120px). |
| Gallery divider | Branding stripes JPEG | Apply as CSS background-image on gallery wrapper; set `background-size: cover` and overlay with `linear-gradient` for contrast. |
| Experiential / café section | Bear merch icon in circle (peach-on-grey) | Place inside feature card at 140px width to humanize the brand story. |
| Footer/location block | Stacked primary logo + monogram | Use stacked logo (~200px) plus mini monogram (48px) for contact links; ensure alt text describes each mark. |
| Page-wide typography moments | `HANDCRAFTED-TYPO-*` PNG | Use as pull-quote style asset near testimonials. Keep width <= 360px and provide `role="presentation"` if purely decorative. |
| Fonts | Alright Sans (light, regular, medium, bold) | Load via `@font-face` once; use for headings/CTA to match brand kit. Fallback to `Space Grotesk` if unavailable. |

Accessibility checklist: every informative asset receives descriptive `alt`; decorative assets either move to CSS backgrounds or include `alt=""` with `aria-hidden="true"`. Prefer `loading="lazy"` for non-critical imagery and constrain max-widths with responsive media queries.

### 3. Integrated On `baecker_charlie_final_combined.html`

- Hero now displays the red horizontal logo plus the white “HANDCRAFTED” typography lock; CTA badge uses the yellow secondary branding unit.
- Sidebar includes the red & yellow monogram together with the pretzel illustration PNG as a contextual accent.
- Café feature list swaps pictograms for branded icons: yellow wheat, peach bear badge, and red secondary branding unit.
- Gallery wrapper pulls in `STRIPES-WITH-BRANDING.jpg` as a textured background overlay.
- Visit cards use the stacked red logo, full logo unit with monogram, and standalone red monogram.
- Additional brand moments: Alright Sans font powers the primary headings, and hero/café/CTA elements inherit `var(--brand-font)` for consistency.

