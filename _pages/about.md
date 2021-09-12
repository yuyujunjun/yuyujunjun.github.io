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
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>


Projects
------
  <ul>{% for post in site.projects reversed  %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>