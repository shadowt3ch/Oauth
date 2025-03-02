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
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 0 0 15px cyan;
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            z-index: 100;
        }

        .logo {
            font-size: 26px;
            color: cyan;
            text-shadow: 0 0 15px cyan;
            font-weight: bold;
            margin-right: 20px;
        }

        nav {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        nav a, nav .dropbtn {
            color: white;
            text-decoration: none;
            font-size: 16px;
            padding: 10px;
            border: none;
            background: none;
            cursor: pointer;
        }

        nav .dropdown {
            position: relative;
        }

        nav .dropdown-content {
            display: none;
            position: absolute;
            background: rgba(0, 0, 0, 0.9);
            box-shadow: 0 0 15px cyan;
            min-width: 150px;
        }

        nav .dropdown-content a {
            display: block;
            padding: 10px;
        }

        nav .dropdown-content a:hover {
            background: cyan;
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

        .intro h2 {
            font-size: 48px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 20px cyan;
            margin-bottom: 15px;
        }

        .intro p {
            font-size: 20px;
            opacity: 0.8;
            line-height: 1.5;
        }

        .buttons a {
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            margin-right: 10px;
        }

        .discord-btn {
            background: #5865F2;
            box-shadow: 0 0 15px #5865F2;
        }

        .commands-btn {
            background: gray;
            box-shadow: 0 0 15px gray;
        }

        .bot-preview img {
            width: 400px;
            border-radius: 10px;
            box-shadow: 0 0 25px rgba(0, 255, 255, 0.7);
        }

        footer {
            text-align: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 0 0 15px cyan;
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
                    <a href="#">PullJoinAll</a>
                    <a href="#">Verify</a>
                    <a href="#">Stop Pull</a>
                    <a href="#">Restart Pull</a>
                    <a href="#">Whitelist</a>
                    <a href="#">Unwhitelist</a>
                    <a href="#">Users</a>
                    <a href="#">BotInfo</a>
                    <a href="#">PayPal</a>
                    <a href="#">CashApp</a>
                </div>
            </div>
            <div class="dropdown">
                <button class="dropbtn">Resources</button>
                <div class="dropdown-content">
                    <a href="#">Docs</a>
                    <a href="#">Support</a>
                </div>
            </div>
            <a href="/login">Login</a>
            <a href="#">Invite</a>
            <a href="https://discord.gg/CV8FMgcrJZ">Discord</a>
        </nav>
    </header>

    <div class="main-container">
        <div class="intro">
            <h2>The best Verification bot for Discord</h2>
            <p>AuthCord is a complete Discord bot, easy-to-use, that millions of Discord servers worldwide trust.</p>
            <div class="buttons">
                <a href="#" class="discord-btn">Add To Discord</a>
                <a href="#" class="commands-btn">See Commands</a>
            </div>
        </div>
        <div class="bot-preview">
            <img src="https://media.discordapp.net/attachments/1345022514505449536/1345490425699631165/IMG_0006.png" alt="Bot Preview">
        </div>
    </div>

    <footer>
        <p>&copy; 2025 AuthCord 🔥 Version 1.0</p>
    </footer>

</body>
</html>
    ''')

@app.route('/admin')
def admin():
    return render_template_string('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AuthCord - Admin Login</title>
    <style>
        body {
            background: #0a0a0a;
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            overflow-x: hidden;
        }

        .admin-container {
            text-align: center;
            padding: 40px;
            background: rgba(0, 0, 0, 0.9);
            box-shadow: 0 0 10px cyan;
            border-radius: 10px;
            max-width: 90%;
        }

        h2 {
            font-size: 32px;
            text-shadow: 0 0 10px cyan;
        }

        .admin-form input {
            padding: 10px;
            margin: 10px 0;
            width: 100%;
            border-radius: 5px;
            border: none;
            outline: none;
            box-shadow: 0 0 10px cyan;
            background: #333;
            color: white;
            font-size: 16px;
        }

        .admin-form button {
            background: cyan;
            color: white;
            padding: 12px 15px;
            border-radius: 5px;
            font-size: 18px;
            border: none;
            cursor: pointer;
            width: 100%;
            box-shadow: 0 0 10px cyan;
        }

        .back-btn {
            margin-top: 20px;
            background: gray;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 16px;
            text-decoration: none;
            box-shadow: 0 0 10px cyan;
            max-width: 100%;
            display: block;
        }

    </style>
</head>
<body>

    <div class="admin-container">
        <h2>Admin Login</h2>
        <form class="admin-form" action="admin_dashboard.html" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <a href="/" class="back-btn">Back to Home</a>
    </div>

</body>
</html>
    ''')

@app.route('/login')
def login():
    return render_template_string('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AuthCord - Login</title>
    <style>
        body {
            background: #0a0a0a;
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            overflow-x: hidden;
        }

        .login-container {
            text-align: center;
            padding: 40px;
            background: rgba(0, 0, 0, 0.9);
            box-shadow: 0 0 10px cyan;
            border-radius: 10px;
            max-width: 90%;
        }

        h2 {
            font-size: 32px;
            text-shadow: 0 0 10px cyan;
        }

        .discord-btn {
            background: #5865F2;
            color: white;
            padding: 12px 15px;
            border-radius: 5px;
            font-size: 18px;
            text-decoration: none;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            box-shadow: 0 0 10px #5865F2;
            cursor: pointer;
            max-width: 100%;
        }

        .discord-btn img {
            width: 24px;
        }

        .back-btn {
            margin-top: 20px;
            display: none;
            background: gray;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            font-size: 16px;
            text-decoration: none;
            box-shadow: 0 0 10px gray;
            max-width: 100%;
        }

    </style>
</head>
<body>

    <div class="login-container">
        <h2>Login with Discord</h2>
        <a href="https://discord.com/oauth2/authorize?client_id=1345207651503702086&redirect_uri=https%3A%2F%2Fbvmdph6r-8080.usw3.devtunnels.ms%2Fcallback&response_type=code&scope=identify" class="discord-btn">
            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111370.png" alt="Discord"> Login with Discord
        </a>                
        <a href="/" class="back-btn" id="back-btn">Back to Home</a>
    </div>

    <script>
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has("logged_in")) {
            document.getElementById("login-btn").style.display = "none";
            document.getElementById("back-btn").style.display = "block";
        }
    </script>

</body>
</html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
