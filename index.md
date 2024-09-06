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
            top: 65%;
            left: -100px; /* Start position off the screen */
            width: 90px; /* Adjust size as needed */
            height: auto;
            z-index: 1000; /* Ensures it appears above other content */
            animation: runAcross 8s linear infinite; /* Adjust duration as needed */
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
    <img src="https://media.tenor.com/UkvleU1dQK4AAAAi/2d-mario-running.gif" alt="Mario Running" class="mario-animation">

    

</body>
</html>


