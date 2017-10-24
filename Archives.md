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
        <a class="page-heading pink-highlight post-url" href="{{ post.url }}">{{ post.title }}</a>
        <div class="date"> Published on {{ post.date | date_to_string }}</div>
        <!-- <div class="excerpt description"> {{ post.excerpt }} </div> -->
      </li>
    {% endfor %}
  </ul>
</div>