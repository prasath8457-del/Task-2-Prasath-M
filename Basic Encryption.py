from flask import Flask, request, render_template_string
import webbrowser
from threading import Timer

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Encryption & Decryption Tool</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container{
            width: 60%;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
        }

        h1{
            text-align:center;
            color:#333;
        }

        textarea{
            width:100%;
            height:120px;
            padding:10px;
            font-size:16px;
        }

        input{
            width:100%;
            padding:10px;
            margin-top:10px;
            font-size:16px;
        }

        button{
            width:100%;
            padding:12px;
            margin-top:15px;
            background:#007bff;
            color:white;
            border:none;
            font-size:16px;
            cursor:pointer;
        }

        button:hover{
            background:#0056b3;
        }

        .result{
            margin-top:20px;
            padding:15px;
            background:#eef;
            border-radius:8px;
        }

        .output{
            font-weight:bold;
            color:#222;
            word-wrap:break-word;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Basic Encryption & Decryption</h1>

    <form method="POST">
        <label>Enter Text</label>
        <textarea name="text" required></textarea>

        <label>Shift Value</label>
        <input type="number" name="shift" value="3" required>

        <button type="submit">Encrypt & Decrypt</button>
    </form>

    {% if encrypted %}
    <div class="result">
        <h3>Encrypted Text</h3>
        <p class="output">{{ encrypted }}</p>

        <h3>Decrypted Text</h3>
        <p class="output">{{ decrypted }}</p>
    </div>
    {% endif %}
</div>

</body>
</html>
"""

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

@app.route("/", methods=["GET", "POST"])
def home():
    encrypted = ""
    decrypted = ""

    if request.method == "POST":
        text = request.form["text"]
        shift = int(request.form["shift"])

        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)

    return render_template_string(
        HTML,
        encrypted=encrypted,
        decrypted=decrypted
    )

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=False)

    