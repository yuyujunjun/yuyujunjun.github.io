---
permalink: /
title: "Homepage"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

About Me
======

To Do.

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Projects
------
  <ul>{% for post in site.projects %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>