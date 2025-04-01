---
layout: base
title: Music Generator
permalink: /music/
---

<!DOCTYPE html>
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
</head>
<body>
    <div class="container">
        <h1>Mood-Based Music Recommender</h1>
        <p>Enter your mood and get a personalized playlist!</p>
        <label for="mood">Select your mood:</label>
        <select id="mood">
            <option value="happy">😊 Happy</option>
            <option value="sad">😢 Sad</option>
            <option value="relaxed">😌 Relaxed</option>
            <option value="energetic">⚡ Energetic</option>
            <option value="stressed">😰 Stressed</option>
            <option value="romantic">❤️ Romantic</option>
            <option value="motivated">🔥 Motivated</option>
            <option value="nostalgic">🎵 Nostalgic</option>
            <option value="angry">😡 Angry</option>
            <option value="hopeful">🌟 Hopeful</option>
            <option value="lonely">💙 Lonely</option>
            <option value="excited">🎉 Excited</option>
        </select>
        <button onclick="getPlaylist()">Get Playlist</button>
        <div id="playlist"></div>
    </div>

    <script>
        function getPlaylist() {
            const mood = document.getElementById("mood").value;
            const playlistDiv = document.getElementById("playlist");
            let playlists = {
                happy: ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake", "Walking on Sunshine - Katrina & The Waves", "Best Day of My Life - American Authors", "Good as Hell - Lizzo"],
                sad: ["Someone Like You - Adele", "Fix You - Coldplay", "Hallelujah - Jeff Buckley", "Let Her Go - Passenger", "All I Want - Kodaline"],
                relaxed: ["Weightless - Marconi Union", "Sunset Lover - Petit Biscuit", "Better Together - Jack Johnson", "Banana Pancakes - Jack Johnson", "Imagine - John Lennon"],
                energetic: ["Stronger - Kanye West", "Uptown Funk - Mark Ronson ft. Bruno Mars", "Eye of the Tiger - Survivor", "Don't Stop Me Now - Queen", "Can't Hold Us - Macklemore & Ryan Lewis"],
                stressed: ["Weightless - Marconi Union", "Clair de Lune - Debussy", "Breathe Me - Sia", "Skinny Love - Bon Iver", "Fix You - Coldplay"],
                romantic: ["Perfect - Ed Sheeran", "Thinking Out Loud - Ed Sheeran", "All of Me - John Legend", "Unchained Melody - The Righteous Brothers", "Make You Feel My Love - Adele"],
                motivated: ["Lose Yourself - Eminem", "Stronger - Kanye West", "Eye of the Tiger - Survivor", "Hall of Fame - The Script ft. will.i.am", "Remember the Name - Fort Minor"],
                nostalgic: ["Smells Like Teen Spirit - Nirvana", "Take On Me - a-ha", "Bohemian Rhapsody - Queen", "Sweet Child O' Mine - Guns N' Roses", "Hey Jude - The Beatles"],
                angry: ["Break Stuff - Limp Bizkit", "Killing in the Name - Rage Against the Machine", "Last Resort - Papa Roach", "Before I Forget - Slipknot", "Given Up - Linkin Park"],
                hopeful: ["Rise Up - Andra Day", "What a Wonderful World - Louis Armstrong", "Somewhere Over the Rainbow - Israel Kamakawiwo'ole", "Heal the World - Michael Jackson", "Beautiful Day - U2"],
                lonely: ["Boulevard of Broken Dreams - Green Day", "Tears in Heaven - Eric Clapton", "All By Myself - Celine Dion", "Creep - Radiohead", "Yesterday - The Beatles"],
                excited: ["We Will Rock You - Queen", "Thunderstruck - AC/DC", "Let's Get It Started - Black Eyed Peas", "Party Rock Anthem - LMFAO", "Can't Stop - Red Hot Chili Peppers"]
            };
            
            let playlist = playlists[mood] || [];
            playlistDiv.innerHTML = "<h3>Your Playlist:</h3><ul>" + playlist.map(song => `<li>${song}</li>`).join('') + "</ul>";
        }
    </script>
</body>
</html>
