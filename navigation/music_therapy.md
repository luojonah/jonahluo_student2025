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
        iframe {
            width: 100%;
            height: 380px;
            border: none;
            margin-top: 10px;
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
        <div id="spotify"></div>
        <div id="youtube"></div>
    </div>

    <script>
        function getPlaylist() {
            const mood = document.getElementById("mood").value;
            const playlistDiv = document.getElementById("playlist");
            const spotifyDiv = document.getElementById("spotify");
            const youtubeDiv = document.getElementById("youtube");

            let spotifyPlaylists = {
                happy: "37i9dQZF1DXdPec7aLTmlC",
                sad: "37i9dQZF1DX7qK8ma5wgG1",
                relaxed: "37i9dQZF1DX4sWSpwq3LiO",
                energetic: "37i9dQZF1DX8FwnYE6PRvL",
                stressed: "37i9dQZF1DX3YSRoSdA634",
                romantic: "37i9dQZF1DXbEm2sKzgoJ8",
                motivated: "37i9dQZF1DXdxcBWuJkbcy",
                nostalgic: "37i9dQZF1DX4OzrY981I1W",
                angry: "37i9dQZF1DX3H5z3ZVpVZB",
                hopeful: "37i9dQZF1DXcBWIGoYBM5M",
                lonely: "37i9dQZF1DX3YSRoSdA634",
                excited: "37i9dQZF1DX1s9knjP51Oa"
            };

            let youtubePlaylists = {
                happy: "https://www.youtube.com/watch?v=ZbZSe6N_BXs&list=PLFZnsq5sh00D95BvFcdZ4oL7R4qLy_XvG",
                sad: "https://www.youtube.com/watch?v=YQHsXMglC9A&list=PLFZnsq5sh00BZCMEQJDFtxj0Plzyh5b8h",
                relaxed: "https://www.youtube.com/watch?v=UfcAVejslrU&list=PLFZnsq5sh00Dhu_lgrHpLxzjH-3DNhQUZ",
                energetic: "https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PLFZnsq5sh00Dx4_XDCcM5wFz0iRQ1eFMR",
                stressed: "https://www.youtube.com/watch?v=2NuvLbR2F4w&list=PLFZnsq5sh00D-YbF71aP1nq8_DpYb7aQj",
                romantic: "https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=PLFZnsq5sh00A1r9Ch3FTpOb-0tdwpX6DQ",
                motivated: "https://www.youtube.com/watch?v=2X_2IdybTV0&list=PLFZnsq5sh00CgWQQJrfdy4thZG-6P_r6e",
                nostalgic: "https://www.youtube.com/watch?v=hTWKbfoikeg&list=PLFZnsq5sh00DHw4LXaOL57ufj9rEKGL8V",
                angry: "https://www.youtube.com/watch?v=ZpUYjpKg9KY&list=PLFZnsq5sh00Cl6H-bhH0SHHPaPyYpLKpm",
                hopeful: "https://www.youtube.com/watch?v=eT7nD02Im5E&list=PLFZnsq5sh00CWVwRzZwxtvXk5b-MxaLZ7",
                lonely: "https://www.youtube.com/watch?v=gxEPV4kolz0&list=PLFZnsq5sh00A0Oix60FbJpHbR8MKqE3cR",
                excited: "https://www.youtube.com/watch?v=4fndeDfaWCg&list=PLFZnsq5sh00AVPMH4F2e1ZdmzLbuL7hhV"
            };

            spotifyDiv.innerHTML = `<iframe src="https://open.spotify.com/embed/playlist/${spotifyPlaylists[mood]}" allow="encrypted-media"></iframe>`;
            youtubeDiv.innerHTML = `<p><a href="${youtubePlaylists[mood]}" target="_blank">🎵 Open YouTube Playlist</a></p>`;
        }
    </script>
</body>
</html>
