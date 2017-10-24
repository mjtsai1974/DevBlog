---
layout: page
title: Archives
---

<p class="message">
  Summary of total posts.
</p>

<div class="wrapper">
  <div class="post-header page-title">Posts</div>
  <ul class="post-list">
    {% for post in site.posts %}
      <li>
	    <!-- {% assign date_format = site.minima.date_format | default: "%b %-d, %Y" %} --> <!-- copy from https://github.com/jekyll/minima/blob/master/_layouts/home.html -->
        <a class="page-heading pink-highlight post-url" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
        <!-- <div class="date"> Published on {{ post.date | date: date_format }}</div> --> <!-- copy from https://github.com/jekyll/minima/blob/master/_layouts/home.html -->
        <div class="date"> Published on {{ post.date | date_to_string }}</div>
        <!-- <div class="excerpt description"> {{ post.excerpt }} </div> -->
      </li>
    {% endfor %}
  </ul>
</div>