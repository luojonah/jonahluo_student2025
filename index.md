---
layout: base
title: Student Home 
description: Home Page
hide: true
---

<h1> My Page </h1>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Website Title</title>
    <style>
        /* Additional styles for your website */
        body {
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Prevents horizontal scroll */
        }
        .mario-animation {
            position: absolute; /* Fixed position to stay on bottom */
            top: 1225px;
            left: -100px; /* Start position off the screen */
            width: 85px; /* Adjust size as needed */
            height: auto;
            z-index: 1000; /* Ensures it appears above other content */
            animation: runAcross 10s linear infinite; /* Adjust duration as needed */
        }
        @keyframes runAcross {
            0% {
                left: -900px; /* Start from the left edge */
            }
            100% {
                left: 100vw; /* Move to the right edge */
            }
        }
        button {
            padding: 10px 20px;
            border: 2px solid #4CAF50; /* Border similar to other buttons */
            background-color: #f4f4f4; /* Light background */
            color: #000; /* Text color */
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #4CAF50; /* Hover background color */
            color: white; /* Text color change on hover */
        }
        .games-section {
            text-align: center;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <br>
    My homepage consists of some fun videos, fire songs and other shenanigans. Have fun! 
    <br><br><br>

    <button onclick="window.open('https://www.youtube.com/watch?v=uvyTfRRs-kw', '_blank')">Button (Click Me!!)</button>
    <br><br><br>

    <h3>Bored?</h3>
    <br>
    Usually when I'm bored, I enjoy watching videos and memes. I also enjoy listening to and playing music.
    <br> My favorite music to listen to is Christian music whether that'd be Christian worship music when I'm by myself
    <br> doing homework or Christian rap in a more casual setting. Below are a few buttons linked to some funny memes and
    <br> videos as well as my Spotify playlists. Enjoy!!
</body>
<body>
    <img src="https://media.tenor.com/UkvleU1dQK4AAAAi/2d-mario-running.gif" alt="Mario Running" class="mario-animation">
    <br><br><br>
    <button onclick="window.open('https://www.youtube.com/watch?v=T4NOt727wqI', '_blank')">Fun Video (Click Me!!)</button>
    <button onclick="window.open('https://www.youtube.com/watch?v=coaN2VBNgYA&t=3s', '_blank')">Fun Video (Click Me!!)</button>
    <br><br><br>
    <h3>Fire Music</h3>
    <br>
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5dj1vz9bgxeev4mkUrnjM1?utm_source=generator" width="100%" height="400" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    <!-- Games section at the bottom -->
<div class="games-section">
    <h3>Games</h3>
    <br>
    <br>
    <button class="redirect-btn" onclick="navigateTo('game.md')">Cookie Clicker</button>
    <button class="redirect-btn" onclick="navigateTo('snake.md')">Snake</button>
</div>

<script>
    function navigateTo(page) {
        // Find the navigation bar (you might need to adjust the selector based on your layout)
        const navBar = document.querySelector('nav');

        // Create a new anchor tag that links to the .md page
        const navLink = document.createElement('a');
        navLink.href = '/' + page;
        navLink.innerText = page.replace('.md', '');  // Set text without .md extension

        // Add the link to the navigation bar
        navBar.appendChild(navLink);

        // Optionally: Navigate to the new page (emulates a real navigation)
        navLink.click();
    }
</script>

</body>
</html>

