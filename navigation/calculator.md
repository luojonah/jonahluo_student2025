---
layout: base
title: Calculator 
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binary Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        input {
            padding: 10px;
            margin: 5px;
            width: 100px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            margin: 5px;
            font-size: 16px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>
<body>

    <h1>Binary Calculator</h1>

    <input type="text" id="binary1" placeholder="Enter binary 1">
    <br>
    <input type="text" id="binary2" placeholder="Enter binary 2">
    <br><br>

    <button onclick="calculate('add')">Add</button>
    <button onclick="calculate('subtract')">Subtract</button>
    <button onclick="calculate('multiply')">Multiply</button>
    <button onclick="calculate('divide')">Divide</button>

    <div class="result">
        <p id="result"></p>
    </div>

    <script>
        function calculate(operation) {
            let binary1 = document.getElementById('binary1').value;
            let binary2 = document.getElementById('binary2').value;

            // Check if input is valid binary
            if (!/^[01]+$/.test(binary1) || !/^[01]+$/.test(binary2)) {
                document.getElementById('result').innerHTML = "Please enter valid binary numbers.";
                return;
            }

            // Convert binary inputs to decimal
            let decimal1 = parseInt(binary1, 2);
            let decimal2 = parseInt(binary2, 2);
            let result;

            // Perform the selected operation
            switch(operation) {
                case 'add':
                    result = decimal1 + decimal2;
                    break;
                case 'subtract':
                    result = decimal1 - decimal2;
                    break;
                case 'multiply':
                    result = decimal1 * decimal2;
                    break;
                case 'divide':
                    if (decimal2 === 0) {
                        document.getElementById('result').innerHTML = "Cannot divide by zero.";
                        return;
                    }
                    result = Math.floor(decimal1 / decimal2); // integer division
                    break;
            }

            // Convert the result back to binary
            let binaryResult = result.toString(2);

            // Display the result
            document.getElementById('result').innerHTML = `Result: ${binaryResult}`;
        }
    </script>

</body>
</html>
