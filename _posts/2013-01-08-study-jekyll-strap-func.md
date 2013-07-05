---
layout: post
category : study
published: false
tags : [study, jekyll]
---
{% include JB/setup %}


### Get posts
    <ul class="posts">
        {% for post in site.posts %}
        <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
        {% endfor %}
    </ul>

### Get tags
    <ul class="tag_box inline">
    {% assign tags_list = site.tags %}  
    {% include JB/tags_list %}
    </ul>


    {% for tag in site.tags %} 
    <h2 id="{{ tag[0] }}-ref">{{ tag[0] }}</h2>
    <ul>
    {% assign pages_list = tag[1] %}  
    {% include JB/pages_list %}
    </ul>
    {% endfor %}

### Get Site Maps
    {% for page in site.pages %}
    {{site.production_url}}{{ page.url }}{% endfor %}
    {% for post in site.posts %}
    {{site.production_url}}{{ post.url }}{% endfor %}