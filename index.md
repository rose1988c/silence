---
layout: page
title: Rose1988'c Blog
tagline: insky
---
{% include JB/setup %}

**back up**

<ul class="listing">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator">{{ y }}</li>
  {% endif %}
  <li class="listing-item">
    <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
    <a href="{{ BASE_PATH }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}8uj</a>
  </li>
{% endfor %}
</ul>

