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
            top: 899px;
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
    </style>
</head>
<body>
    <br>
    My homepage consists of some fun videos, fire songs and other shenanagans. Have fun! 
    <br>
    <br>
    <br>
</body>
<body>
    <h3>Bored?</h3>
    <br>
    Usually when I'm bored, I enjoy watching funny videos and memes. I also enjoy listening to and playing music.
    <br> My favorite music to listen to is Christian music whether that'd be Christian worship music when I'm by myself
    <br> doing homework or Christian rap in a more causual setting. Below are a few buttons linked to some funny memes and
    <br> videos as well as my spotify playlists. Enjoy!!
</body>
<body>
    <img src="https://media.tenor.com/UkvleU1dQK4AAAAi/2d-mario-running.gif" alt="Mario Running" class="mario-animation">
    <br>
    <br>
    <br>
    <button onclick="window.open('https://www.youtube.com/watch?v=SeHYcxohxCk', '_blank')">Fun Video</button>
    <br>
    <br>
    <br>
    <h3>Fire Music</h3>
    <br>
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5dj1vz9bgxeev4mkUrnjM1?utm_source=generator" width="75%" height="350" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

</body>
</html>


