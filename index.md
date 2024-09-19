---
layout: base
title: Student Home 
description: Home Page
hide: true
---

<h1> My Page </h1>
<br>
<br>
## Gaming Submenu
<br>
<br>
<style>
  .dropdown {
    position: relative;
    display: inline-block;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #F9F9F9;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    min-width: 160px;
    z-index: 1;
  }
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    border-radius: 5px;
    margin: 5px;
  }
  .dropdown-content a:hover {
    background-color: #ddd;
  }
  .dropdown:hover .dropdown-content {
    display: block;
  }
  .dropdown:hover .dropdown-button {
    background-color: #3E8E41;
  }
</style>
<div class="dropdown">
  <button class="dropdown-button" style="background-color: white; color: white; padding: 16px; font-size: 16px; border-color: white; cursor: pointer; border-radius: 8px;">
    Gaming Submenu
  </button>
  <div class="dropdown-content">
    <a href="navigation/game.html" style="background-color: green; color: white;">Cookie Clicker</a>
    <a href="navigation/calculator.html" style="background-color: orange; color: white;">Binary Calculator</a>
    <a href="navigation/snake.html" style="background-color: red; color: white;">Snake Game</a>
  </div>
  <br>
  <br>
  <br>
</div>



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
            top: 1275px;
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
    
    <img src="https://media.tenor.com/UkvleU1dQK4AAAAi/2d-mario-running.gif" alt="Mario Running" class="mario-animation">
    <br><br><br>
    <button onclick="window.open('https://www.youtube.com/watch?v=T4NOt727wqI', '_blank')">Fun Video (Click Me!!)</button>
    <button onclick="window.open('https://www.youtube.com/watch?v=coaN2VBNgYA&t=3s', '_blank')">Fun Video (Click Me!!)</button>
    <br><br><br>
    
    <h3>Fire Music</h3>
    <br>
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5dj1vz9bgxeev4mkUrnjM1?utm_source=generator" width="100%" height="400" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    

</body>
</html>

