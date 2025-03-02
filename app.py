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

@app.route('/login')
def login():
    return render_template_string('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AuthCord - Admin Panel</title>
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

        .admin-panel {
            padding: 30px;
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 0 0 20px cyan;
            border-radius: 20px;
            max-width: 500px;
            width: 90%;
        }

        h2 {
            font-size: 36px;
            text-shadow: 0 0 15px cyan;
            margin-bottom: 20px;
        }

        .button {
            background: linear-gradient(45deg, cyan, #4dd2ff);
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-size: 20px;
            border: none;
            cursor: pointer;
            width: 100%;
            margin: 10px 0;
            box-shadow: 0 0 15px cyan;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .button:hover {
            transform: translateY(-5px);
            box-shadow: 0 0 25px cyan;
        }

        .user-list {
            margin: 20px 0;
            max-height: 200px;
            overflow-y: auto;
            box-shadow: 0 0 15px cyan;
            padding: 15px;
            background: #1a1a1a;
            border-radius: 10px;
        }

        .search-bar, .dropdown, .input-number {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 10px;
            border: none;
            outline: none;
            box-shadow: 0 0 15px cyan;
            background: #1a1a1a;
            color: white;
            font-size: 18px;
        }
    </style>
</head>
<body>

    <div class="admin-panel">
        <h2>Admin Panel</h2>
        <button class="button" onclick="showVerifiedUsers()">Verified Members</button>
        <button class="button">Whitelist</button>
        <button class="button">Blacklist</button>

        <input type="text" class="search-bar" placeholder="Search Usernames..." oninput="searchUsernames()">
        <div class="user-list" id="userList"></div>

        <button class="button" onclick="showMemberPullMenu()">Pull Members</button>
        <select class="dropdown" id="serverSelect">
            <option value="Server1">Server 1</option>
            <option value="Server2">Server 2</option>
        </select>
        <input type="number" class="input-number" placeholder="Number of Members" id="memberCount">
    </div>

    <script>
        const usernames = ['User1', 'User2', 'User3'];

        function showVerifiedUsers() {
            const userList = document.getElementById('userList');
            userList.innerHTML = '';
            usernames.forEach((user, index) => {
                const userItem = document.createElement('div');
                userItem.textContent = `${index + 1}. ${user}`;
                userList.appendChild(userItem);
            });
        }

        function searchUsernames() {
            const searchValue = document.querySelector('.search-bar').value.toLowerCase();
            const filteredUsernames = usernames.filter(user => user.toLowerCase().includes(searchValue));
            const userList = document.getElementById('userList');
            userList.innerHTML = '';
            filteredUsernames.forEach((user, index) => {
                const userItem = document.createElement('div');
                userItem.textContent = `${index + 1}. ${user}`;
                userList.appendChild(userItem);
            });
        }

        function showMemberPullMenu() {
            alert('Pull Members Menu Triggered');
        }

    </script>

</body>
</html>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
