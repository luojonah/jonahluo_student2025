---
layout: page
title: Cookie Clicker
permalink: /game/
---

<p>Welcome to Cookie Clicker! Go on and click that cookie!</p>
<!-- Cookie Clicker Game -->
<div id="cookie-game-container" style="text-align: center; margin-top: 20px;">
  <h2>Game 2: Cookie Clicker</h2>
  <img id="cookie" src="{{site.baseurl}}/images/cookie.png" alt="Cookie" width="200px" height="200px" style="cursor: pointer;">
  <img source>
  <p>Cookies clicked: <span id="counter">0</span></p>
</div>
<script>
  let counter = 0;
  document.getElementById('cookie').addEventListener('click', function() {
    counter++;
    document.getElementById('counter').textContent = counter;
  });
</script>