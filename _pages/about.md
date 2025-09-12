---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<!-- jekyll serve -l -H localhost -->

I am a M.S. / Ph.D. Integrated student of [CVLAB](https://cvlab.kaist.ac.kr) at KAIST, under the supervision of Prof. Seungryong Kim. My current work involves a variety of computer vision tasks, including image segmentation, text-to-image/video generation, and 3D modeling.

My research interests lie at <i style="color:#697FBD;">the intersection of computer vision and robotic agents</i>, with a focus on developing accurate and semantically rich perception and generative models for advancing robot perception and world modeling.
I believe that integrating these fields will make the world more convenient and safer, and I am excited to be part of this journey. If you have any questions or suggestions, please feel free to contact me!

<div style="margin-bottom:24px;"></div>


Publications
======

{% include base_path %}
<div class="publications-list">
{% assign pubs = site.data.publications | sort: 'pub_date' | reverse %}
{% for p in pubs %}
  <div class="pub-item" style="display:flex; gap:20px; align-items:flex-start; margin-bottom:28px;">
    <div class="pub-teaser" style="flex:0 0 200px; max-width:200px; display:flex; flex-direction:column; align-items:center;">
      {% if p.teaser_img %}
  <img src="{{ p.teaser_img | strip }}" alt="teaser {{ p.title | escape }}" class="image-container" style="width:200px; border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,0.15);">
      {% else %}
        <div style="width:200px; height:100; background:#eee; display:flex; align-items:center; justify-content:center; font-size:12px; color:#777; border-radius:6px;">No Image</div>
      {% endif %}
  <div class="pub-links" style="margin-top:10px; display:flex; flex-direction:row; gap:12px; width:100%; justify-content:center; align-items:center;">
          {% if p.slides_url %}
            <a href="{{ p.slides_url }}" target="_blank" rel="noopener" class="pub-link-btn" style="padding:0; background:none; border:none;">
              <img src="../images/homepage_icon.svg" alt="Homepage" style="width:20px; height:20px; vertical-align:middle; box-shadow:none;">
            </a>
          {% endif %}
          {% if p.code_url %}
            <a href="{{ p.code_url }}" target="_blank" rel="noopener" class="pub-link-btn" style="padding:0; background:none; border:none;">
              <img src="../images/github_icon.svg" alt="GitHub" style="width:20px; height:20px; vertical-align:middle; box-shadow:none;">
            </a>
          {% endif %}
          {% if p.paper_url %}
            <a href="{{ p.paper_url }}" target="_blank" rel="noopener" class="pub-link-btn" style="padding:0; background:none; border:none;">
              <img src="../images/arxiv_icon.svg" alt="arXiv" style="width:20px; height:20px; vertical-align:middle; box-shadow:none;">
            </a>
          {% endif %}
        </div>
      </div>
      <div class="pub-meta" style="flex:1; min-width:0;">
      <h3 style="margin:0 0 6px; font-size:1.05rem; line-height:1.3;">{{ p.title }}</h3>
      <div style="margin:0 0 0px; font-size:0.9rem; font-weight:400; color:#555; line-height:1.4;"><i>{{ p.authors }}</i></div>
      {% if p.venue %}
        <div style="font-size:0.9rem; color:#444; margin-bottom:6px;">{{ p.venue }}</div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

<style>
@media (max-width: 640px) {
  .pub-item { flex-direction: column; }
  .pub-teaser { max-width:100%; }
  .pub-teaser img { width:100%; height:auto; }
}
</style>
<!-- Click-to-zoom Lightbox -->
<script>
// -----------------------------
// 🖼️ Click-to-zoom Lightbox
// -----------------------------
const lightbox = document.createElement('div');
lightbox.className = 'lightbox-overlay';
lightbox.setAttribute('role', 'dialog');
lightbox.setAttribute('aria-modal', 'true');
lightbox.innerHTML = '<img alt="Expanded image">';
document.body.appendChild(lightbox);
const lightboxImg = lightbox.querySelector('img');
function openLightbox(src, alt) {
    lightboxImg.src = src;
    lightboxImg.alt = alt || '';
    lightbox.classList.add('active');
    document.body.classList.add('no-scroll');
}
function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.classList.remove('no-scroll');
    lightboxImg.src = '';
}
lightbox.addEventListener('click', closeLightbox);
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && lightbox.classList.contains('active')) closeLightbox();
});
window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.image-container').forEach(img => {
        img.classList.add('zoomable');
        img.addEventListener('click', () => {
            const src = img.getAttribute('data-fullsrc') || img.currentSrc || img.src;
            openLightbox(src, img.alt);
        });
    });
});
</script>
<style>
.lightbox-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.85);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}
.lightbox-overlay.active {
  opacity: 1;
  pointer-events: auto;
}
.lightbox-overlay img {
  max-width: 90vw;
  max-height: 90vh;
  border-radius: 12px;
  box-shadow: 0 4px 32px rgba(0,0,0,0.25);
}
.no-scroll {
  overflow: hidden !important;
}
.zoomable {
  cursor: zoom-in;
}
.image-container:hover {
  box-shadow: 0 10px 30px 0px rgba(0, 0, 0, 0.25), 0 10px 15px 0px rgba(0, 0, 0, 0.15) !important;
}
}
</style>

