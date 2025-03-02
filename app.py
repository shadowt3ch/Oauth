from flask import Flask, Response, render_template_string, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AuthCord - The Best Verification Bot</title>
    <style>
        body {
            background: #0a0a0a;
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        header {
            display: flex;
            align-items: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.9);
            box-shadow: 0 0 10px lime;
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            z-index: 100;
        }

        .logo {
            font-size: 26px;
            color: lime;
            text-shadow: 0 0 10px lime;
            font-weight: bold;
            margin-right: 20px;
        }

        nav {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        nav .dropdown {
            position: relative;
            display: inline-block;
        }

        nav .dropbtn {
            color: white;
            background: none;
            border: none;
            cursor: pointer;
            font-size: 16px;
            padding: 10px;
        }

        nav .dropdown-content {
            display: none;
            position: absolute;
            background: rgba(0, 0, 0, 0.9);
            box-shadow: 0 0 10px lime;
            min-width: 150px;
        }

        nav .dropdown-content a {
            color: white;
            padding: 10px;
            text-decoration: none;
            display: block;
        }

        nav .dropdown-content a:hover {
            background: lime;
            color: black;
        }

        nav .dropdown:hover .dropdown-content {
            display: block;
        }

        .main-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 100vh;
            padding: 150px 80px 50px;
        }

        .intro {
            max-width: 600px;
        }

        .intro h2 {
            font-size: 48px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 15px lime;
            margin-bottom: 15px;
        }

        .intro p {
            font-size: 20px;
            color: white;
            opacity: 0.8;
            line-height: 1.5;
        }

        .buttons {
            margin-top: 30px;
        }

        .discord-btn {
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            background: #5865F2;
            color: white;
            box-shadow: 0 0 10px #5865F2;
            display: inline-block;
        }

        .commands-btn {
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            background: gray;
            color: white;
            box-shadow: 0 0 10px gray;
            display: inline-block;
        }

        .bot-preview {
            position: relative;
            max-width: 500px;
            text-align: right;
        }

        .bot-preview img {
            width: 400px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
        }

        .overlay-image {
            position: absolute;
            bottom: -30px;
            right: -30px;
            width: 200px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(255, 0, 255, 0.8);
        }

        footer {
            text-align: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.9);
            box-shadow: 0 0 10px lime;
            margin-top: 50px;
        }

    </style>
</head>
<body>

    <header>
        <h1 class="logo">AuthCord</h1>
        <nav>
            <div class="dropdown">
                <button class="dropbtn">Commands</button>
                <div class="dropdown-content">
                    <a href="NOT DONE YET TO LAZY">PullJoinAll</a>
                    <a href="NOT DONE YET TO LAZY">Verify</a>
                    <a href="NOT DONE YET TO LAZY">Stop Pull</a>
                    <a href="NOT DONE YET TO LAZY">Restart Pull</a>
                    <a href="NOT DONE YET TO LAZY">Whitelist</a>
                    <a href="NOT DONE YET TO LAZY">Unwhitelist</a>
                    <a href="NOT DONE YET TO LAZY">Users</a>
                    <a href="NOT DONE YET TO LAZY">BotInfo</a>
                    <a href="NOT DONE YET TO LAZY">PayPal</a>
                    <a href="NOT DONE YET TO LAZY">CashApp</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Resources</button>
                <div class="dropdown-content">
                    <a href="#">Docs</a>
                    <a href="#">Support</a>
                </div>
            </div>
            <a href="login.html">Login</a>
            <a href="#">Invite</a>
            <a href="#">Discord</a>
        </nav>
    </header>

    <div class="main-container">
        <div class="intro">
            <h2>The best Verification bot for Discord</h2>
            <p>AuthCord is a complete Discord bot, easy-to-use, that millions of Discord servers worldwide trust.</p>
            <div class="buttons">
                <a href="YOUR_BOT_INVITE_LINK_HERE" class="discord-btn">Add To Discord</a>
                <a href="#" class="commands-btn">See Commands</a>
            </div>
        </div>
        <div class="bot-preview">
            <img src="https://media.discordapp.net/attachments/1345022514505449536/1345490425699631165/IMG_0006.png" alt="Bot Preview">
            <img src="https://media.discordapp.net/attachments/1345022514505449536/1345490426068471839/IMG_0005.png" alt="Overlay Image" class="overlay-image">
        </div>
    </div>

    <footer>
        <p>&copy; 2025 AuthCord. All rights reserved.</p>
    </footer>

</body>
</html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
