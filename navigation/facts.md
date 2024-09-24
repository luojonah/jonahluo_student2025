---
layout: base
title: Random Facts Generator
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FC Barcelona Random Fact Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        #fact-box {
            background-color: #003A70;
            color: white;
            padding: 20px;
            border-radius: 10px;
            width: 300px;
            margin: auto;
            font-size: 1.2em;
        }
        button {
            background-color: #A50044;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
            font-size: 1em;
        }
        button:hover {
            background-color: #870033;
        }
    </style>
</head>
<body>

    <h1>FC Barcelona Random Fact Generator</h1>
    <br>
    <br>
    <div id="fact-box">Press the button to see a fact!</div>
    <br>
    <br>
    <button onclick="generateFact()">Get a Fact</button>

    <script>
        const facts = [
            "FC Barcelona was founded in 1899 by a group of Swiss, English, and Spanish footballers.",
            "Barcelona’s stadium, Camp Nou, is the largest in Europe with a seating capacity of nearly 100,000.",
            "Lionel Messi scored 672 goals for FC Barcelona, making him the club's all-time top scorer.",
            "FC Barcelona has won the UEFA Champions League five times.",
            "Barça is the only European football club to have played continental football every season since 1955.",
            "The team's motto is 'Més que un club' which means 'More than a club'.",
            "Barcelona's colors, blue and claret, were chosen by founder Hans Gamper to reflect his Swiss hometown’s colors.",
            "FC Barcelona has won the Spanish La Liga 26 times.",
            "Barcelona has fierce rivalries with both Real Madrid (El Clásico) and Espanyol (Derbi Barceloní).",
            "In 2009, Barcelona became the first club in history to win the sextuple (6 trophies in a calendar year)."
        ];

        function generateFact() {
            const randomIndex = Math.floor(Math.random() * facts.length);
            document.getElementById('fact-box').textContent = facts[randomIndex];
        }
    </script>

</body>
</html>
