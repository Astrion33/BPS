<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vanta.js Halo Effect</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r121/three.min.js"></script>
<script src="https://www.vantajs.com/dist/vanta.halo.min.js"></script>
<style>
    body, html {
        margin: 0;
        padding: 0;
        height: 100%;
    }
    #gui-container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 1;
        text-align: center;
    }
    #search-bar {
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        width: 300px;
    }
    #enter-button, #chrome-button {
        background-color: blue;
        color: white;
        border: none;
        padding: 10px 20px;
        margin: 5px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    #enter-button:hover, #chrome-button:hover {
        background-color: darkblue;
    }
</style>
</head>
<body>
<div id="vanta-container"></div>
<div id="gui-container">
    <input type="text" id="search-bar" placeholder="Enter your search query...">
    <br><br>
    <button id="enter-button">Enter</button>
    <button id="chrome-button">Open Chrome</button>
</div>
<script>
    VANTA.HALO({
        el: "#vanta-container",
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200,
        minWidth: 200,
        backgroundColor: 0x0
    });

    // Function to open search query in Google Chrome
    function searchInChrome() {
        var searchQuery = document.getElementById("search-bar").value;
        var searchUrl = "https://www.google.com/search?q=" + encodeURIComponent(searchQuery);
        window.open(searchUrl, "_blank");
    }

    // Event listener for the Enter button
    document.getElementById("enter-button").addEventListener("click", searchInChrome);

    // Event listener for the Open Chrome button
    document.getElementById("chrome-button").addEventListener("click", function() {
        window.open("https://www.google.com", "_blank");
    });

    
</script>
</body>
</html>
