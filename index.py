html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horror Game Menu</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Creepster&display=swap">
    <style>
        body {
            background-color: black;
            color: #8b0000; /* Darker red color */
            font-family: 'Creepster', cursive; /* Creepster font */
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }

        section {
            margin: 20px;
            text-align: center;
            cursor: pointer;
            font-size: 2em;
        }

        .glitch {
            position: relative;
            display: inline-block;
            animation: glitch 1s infinite linear alternate-reverse;
        }

        .glitch::before, .glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
        }

        .glitch::before {
            color: #000;
            clip: rect(2px, auto, 4px, 0);
        }

        .glitch::after {
            color: #8b0000; /* Darker red color */
            clip: rect(5px, auto, 6px, 0);
        }

        @keyframes glitch {
            2%, 64% {
                transform: translate(2px, 0) skewX(10deg);
            }
            4%, 60% {
                transform: translate(-2px, 0) skewX(-10deg);
            }
            62% {
                transform: translate(0, 0) skew(0);
            }
        }

        #content {
            display: none;
            margin: 20px;
            text-align: center;
        }

        #content-text {
            font-size: 1.5em;
        }

        #back-button {
            padding: 10px 20px;
            background-color: #8b0000; /* Darker red color */
            color: black;
            border: none;
            cursor: pointer;
            font-size: 1.2em;
            font-family: 'Creepster', cursive; /* Creepster font */
        }

        #email-box {
            margin-top: 20px;
            text-align: center;
        }

        #email-input {
            padding: 10px;
            font-family: 'Creepster', cursive; /* Creepster font */
            color: #8b0000; /* Darker red color */
        }

        #join-button {
            padding: 10px 20px;
            background-color: #8b0000; /* Darker red color */
            color: black;
            border: none;
            cursor: pointer;
            font-family: 'Creepster', cursive; /* Creepster font */
        }
    </style>
</head>
<body>
    <section class="glitch" data-text="About" onclick="showContent('CrithLabs is the wicked creator brand ecosystem & Web3 microapp label.')">About</section>
    <section class="glitch" data-text="TV" onclick="showContent('Here\'s what\'s live right now (later we will embedd the livestream video to this section), and under that, it says \"weekly schedule\" (later we will create a separate html for this to work)')">TV</section>
    <section class="glitch" data-text="Join" onclick="showContent('Join')">Join</section>

    <div id="content">
        <p id="content-text"></p>
        <button id="back-button" onclick="hideContent()">Back</button>
    </div>

    <div id="email-box">
        <input type="email" id="email-input" placeholder="Enter your email">
        <button id="join-button">Join Newsletter</button>
    </div>

    <script>
        function showContent(content) {
            document.getElementById('content-text').innerText = content;
            document.getElementById('content').style.display = 'block';
            document.getElementById('email-box').style.display = 'none';
        }

        function hideContent() {
            document.getElementById('content').style.display = 'none';
            document.getElementById('email-box').style.display = 'block';
        }
    </script>
</body>
</html>
"""

# Save HTML code to a file
with open('index.html', 'w') as file:
    file.write(html_code)

print("HTML file generated: index.html")
