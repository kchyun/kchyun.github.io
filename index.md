---
layout: default
---

<!-- Profile Header -->
<div class="profile-header">
  <div class="profile-photo">
    <img src="/images/profile3.jpeg" alt="Chaehyun Kim">
  </div>
  <div class="profile-info">
    <h1>Chaehyun Kim</h1>
    <p class="profile-subtitle">M.S./Ph.D. Integrated Student · CVLAB, KAIST</p>
    <div class="profile-links">
      <a href="mailto:kchyun@kaist.ac.kr"><i class="fas fa-envelope"></i> kchyun@kaist.ac.kr</a>
      <a href="https://scholar.google.com/citations?user=qTKC_2cAAAAJ&hl=en" target="_blank" rel="noopener">
        <i class="ai ai-google-scholar"></i> Google Scholar
      </a>
      <a href="https://github.com/kchyun" target="_blank" rel="noopener">
        <i class="fab fa-github"></i> GitHub
      </a>
      <a href="https://www.linkedin.com/in/kchyun0910" target="_blank" rel="noopener">
        <i class="fab fa-linkedin"></i> LinkedIn
      </a>
    </div>
  </div>
</div>

<!-- Intro -->
<div class="bio">
  <p>I am an integrated M.S./Ph.D. student at <a href="https://cvlab.kaist.ac.kr">KAIST CVLAB</a>, advised by Prof. Seungryong Kim, and currently a research intern at NVIDIA Research Taiwan. Previously, I was a research intern at Naver Cloud.</p>
  <p>My research interests lie at the intersection of computer vision and embodied agents, focusing on developing semantically and geometrically rich vision models to advance robot perception and world modeling.</p>
  <p>If you have any questions or suggestions, please feel free to contact me via email (<a href="mailto:kchyun@kaist.ac.kr">kchyun@kaist.ac.kr</a>) or <a href="https://www.linkedin.com/in/kchyun0910">LinkedIn</a>!</p>
</div>

## Experience

<!--
  Logo files go in images/logos/.
  Set the src of each .exp-logo img to match your filename.
  Recommended size: ~120px wide, any height (auto-scaled).
-->

<ul class="cv-list exp-grid">
  <li class="exp-item">
    <div class="exp-content">
      <div class="exp-logo">
        <img src="/images/logos/nvidia.png" alt="NVIDIA">
      </div>
      <div class="exp-text">
        <div class="exp-company">NVIDIA Research Taiwan</div>
        <div class="exp-role">Research Intern</div>
        <div class="exp-period">2026.04 – Now</div>
      </div>
    </div>
  </li>
  <li class="exp-item">
    <div class="exp-content">
      <div class="exp-logo">
        <img src="/images/logos/naver_cloud.png" alt="Naver Cloud">
      </div>
      <div class="exp-text">
        <div class="exp-company">Naver Cloud</div>
        <div class="exp-role">Research Intern</div>
        <div class="exp-period">2025.10 – 2026.04</div>
      </div>
    </div>
  </li>
</ul>

## Publications

<div class="publications-list">
{% assign pubs = site.data.publications | sort: 'pub_date' | reverse %}
{% for p in pubs %}
  <div class="pub-item">
    <div class="pub-teaser">
      {% if p.teaser_img %}
        <img src="{{ p.teaser_img | strip | replace: '../', '/' }}" alt="teaser {{ p.title | escape }}" class="image-container">
      {% else %}
        <div style="width:100%; height:120px; background:#eee; display:flex; align-items:center; justify-content:center; font-size:12px; color:#777; border-radius:6px;">No Image</div>
      {% endif %}
      <div class="pub-links">
        {% if p.slides_url %}
          <a href="{{ p.slides_url }}" target="_blank" rel="noopener">
            <img src="/images/homepage_icon.svg" alt="Project page">
          </a>
        {% endif %}
        {% if p.code_url %}
          <a href="{{ p.code_url }}" target="_blank" rel="noopener">
            <img src="/images/github_icon.svg" alt="GitHub">
          </a>
        {% endif %}
        {% if p.paper_url %}
          <a href="{{ p.paper_url }}" target="_blank" rel="noopener">
            <img src="/images/arxiv_icon.svg" alt="arXiv">
          </a>
        {% endif %}
      </div>
    </div>
    <div class="pub-meta">
      <h3>{{ p.title }}</h3>
      <div class="author">{{ p.authors }}</div>
      {% if p.venue %}<div class="venue">{{ p.venue }}</div>{% endif %}
    </div>
  </div>
{% endfor %}
</div>

## Education

<ul class="cv-list">
  <li>
    M.S. / Ph.D Integrated Student @ Korea Advanced Institute of Science &amp; Technology (KAIST)
    <ul>
      <li>Kim Jaechul Graduate School of AI, CVLAB (PI: Prof. Seungryong Kim)</li>
      <li>2024.09 – 2029 (expected)</li>
    </ul>
  </li>
  <li>
    B.S. at Korea University
    <ul>
      <li>Computer Science &amp; Engineering</li>
      <li>2020.03 – 2024.08 · Graduated Magna Cum Laude</li>
    </ul>
  </li>
</ul>

## Academic Service

<!--
  HOW TO ADD ACADEMIC SERVICE ENTRIES:
  Each entry is a <li> inside the <ul class="cv-list"> below.
  Use this structure for each role:

  <li>
    Role · Conference/Journal Name · Year
    <ul>
      <li>Optional detail (e.g. number of papers reviewed)</li>
    </ul>
  </li>

  Common roles: Reviewer, Program Committee Member, Area Chair,
  Workshop Organizer, Session Chair, etc.

  Example:
  <li>
    Reviewer · NeurIPS 2025
  </li>
  <li>
    Reviewer · CVPR, ICCV, ECCV · 2025
  </li>
-->

<ul class="cv-list">
  <li>Reviewer · AAAI · 2026</li>
  <li>Reviewer · ECCV · 2026</li>
</ul>

## Honors &amp; Awards

<ul class="cv-list">
  <li>STX Scholarship · 2022.03
    <ul><li>Issued by STX Foundation</li></ul>
  </li>
  <li>The National Scholarship for Science and Engineering · 2022.03
    <ul><li>Issued by KOSAF (Korea Student Aid Foundation)</li></ul>
  </li>
  <li>Merit Based Scholarship · 2021.01
    <ul><li>Issued by Suwon-si</li></ul>
  </li>
</ul>
