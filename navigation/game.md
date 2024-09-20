---
layout: base
title: Cookie Clicker
---
<br>
<br>
<h3>Click the Cookie!</h3>
<!-- Cookie Clicker Game -->
<div id="cookie-game-container" style="text-align: center; margin-top: 20px;">
  <img id="cookie" src="{{site.baseurl}}/images/cookie.png" alt="Cookie" width="200px" height="200px" style="cursor: pointer;">
  <p>Cookies clicked: <span id="counter">0</span></p>
</div>

<style>
  /* Define the bounce animation */
  @keyframes bounce {
    0% { transform: scale(1); }
    25% { transform: scale(1.1); }
    50% { transform: scale(0.99); }
    75% { transform: scale(1.05); }
    100% { transform: scale(1); }
  }

  /* Set the bounce animation to trigger */
  .bounce {
    animation: bounce 0.3s ease-in-out;
  }
</style>

<script>
  let counter = 0;

  document.getElementById('cookie').addEventListener('click', function() {
    counter++;

    // Update the cookie click counter
    document.getElementById('counter').textContent = counter;

    // Add the bounce animation class to the cookie
    const cookie = document.getElementById('cookie');
    cookie.classList.add('bounce');

    // Remove the animation class after it finishes (0.3s)
    setTimeout(() => {
      cookie.classList.remove('bounce');
    }, 300);  // 300ms matches the animation duration
  });
</script>
