---
layout: base
title: Music Generator
permalink: /music/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mood-Based Music Recommender</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        select, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        #playlist {
            margin-top: 20px;
            text-align: left;
        }
    </style>
<body>
    <div class="container">
        <h1>Mood-Based Music Recommender</h1>
        <p>Enter your mood and get a personalized playlist!</p>
        <label for="mood">Select your mood:</label>
        <select id="mood">
            <option value="happy">Happy</option>
            <option value="sad">Sad</option>
            <option value="relaxed">Relaxed</option>
            <option value="energetic">Energetic</option>
            <option value="stressed">Stressed</option>
        </select>
        <button onclick="getPlaylist()">Get Playlist</button>
        <div id="playlist"></div>
    </div>

    <script>
        function getPlaylist() {
            const mood = document.getElementById("mood").value;
            const playlistDiv = document.getElementById("playlist");
            let playlists = {
                happy: ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake", "Walking on Sunshine - Katrina & The Waves"],
                sad: ["Someone Like You - Adele", "Fix You - Coldplay", "Hallelujah - Jeff Buckley"],
                relaxed: ["Weightless - Marconi Union", "Sunset Lover - Petit Biscuit", "Better Together - Jack Johnson"],
                energetic: ["Stronger - Kanye West", "Uptown Funk - Mark Ronson ft. Bruno Mars", "Eye of the Tiger - Survivor"],
                stressed: ["Weightless - Marconi Union", "Clair de Lune - Debussy", "Breathe Me - Sia"]
            };
            
            let playlist = playlists[mood] || [];
            playlistDiv.innerHTML = "<h3>Your Playlist:</h3><ul>" + playlist.map(song => `<li>${song}</li>`).join('') + "</ul>";
        }
    </script>
