---
permalink: /
title: "Chaehyun Kim"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="wordwrap">
  <p style="margin:0 0 0.45rem;">I am an integrated M.S./Ph.D. student of KAIST <a href="https://cvlab.kaist.ac.kr">CVLAB</a> under Prof. Seungryong Kim and a research intern at Naver Cloud, with a focus on generative world modeling.</p>
  <p style="margin:0 0 0.45rem;">My research interests lie at the intersection of computer vision and embodied agents, focusing on developing semantically rich perception and generative models to advance robot perception and world modeling.</p>
  <p style="margin:0;">If you have any questions or suggestions, please feel free to contact me via email (<a href="mailto:kchyun@kaist.ac.kr">kchyun@kaist.ac.kr</a>) or <a href="https://www.linkedin.com/in/kchyun0910">LinkedIn</a>!</p>
</div>

## Publications

{% include base_path %}
<div class="publications-list">
{% assign pubs = site.data.publications | sort: 'pub_date' | reverse %}
{% for p in pubs %}
  <div class="pub-item" style="display:flex; gap:20px; align-items:flex-start; margin-bottom:28px;">
    <div class="pub-teaser" style="flex:0 0 225px; display:flex; flex-direction:column; align-items:center;">
      {% if p.teaser_img %}
  <img src="{{ p.teaser_img | strip }}" alt="teaser {{ p.title | escape }}" class="image-container" style="border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,0.15);">
      {% else %}
        <div style="width:200px; height:100; background:#eee; display:flex; align-items:center; justify-content:center; font-size:12px; color:#777; border-radius:6px;">No Image</div>
      {% endif %}
  <div class="pub-links" style="margin-top:10px; display:flex; flex-direction:row; gap:12px; width:100%; justify-content:center; align-items:center;">
          {% if p.slides_url %}
            <a href="{{ p.slides_url }}" target="_blank" rel="noopener" class="pub-link-btn" style="padding:0; background:none; border:none;">
              <img src="../images/homepage_icon.svg" alt="Homepage" class="pub-link-icon" style="width:20px; height:20px; vertical-align:middle; box-shadow:none;">
            </a>
          {% endif %}
          {% if p.code_url %}
            <a href="{{ p.code_url }}" target="_blank" rel="noopener" class="pub-link-btn" style="padding:0; background:none; border:none;">
              <img src="../images/github_icon.svg" alt="GitHub" class="pub-link-icon" style="width:20px; height:20px; vertical-align:middle; box-shadow:none;">
            </a>
          {% endif %}
          {% if p.paper_url %}
            <a href="{{ p.paper_url }}" target="_blank" rel="noopener" class="pub-link-btn" style="padding:0; background:none; border:none;">
              <img src="../images/arxiv_icon.svg" alt="arXiv" class="pub-link-icon" style="width:20px; height:20px; vertical-align:middle; box-shadow:none;">
            </a>
          {% endif %}
        </div>
      </div>
      <div class="pub-meta" style="flex:1; min-width:0;">
      <h3 style="margin:0 0 6px; font-size:1.05rem; line-height:1.3;">{{ p.title }}</h3>
      <div class="author">{{ p.authors }}</div>
      {% if p.venue %}
        <div class="venue"><i>{{ p.venue }}</i></div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

<!-- Click-to-zoom Lightbox -->
<link rel="stylesheet" href="{{ '/assets/css/custom-lightbox.css' | relative_url }}">
<script src="{{ '/assets/js/custom-lightbox.js' | relative_url }}"></script>
