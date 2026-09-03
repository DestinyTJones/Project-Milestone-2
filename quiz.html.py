<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Self Assessment Quiz</title>
<link rel="stylesheet" href="css/style.css">
</head>

<body>

<header>
<h1>Self Assessment Quiz</h1>

<nav>
<ul>
<li><a href="index.html">Home</a></li>
<li><a href="quiz.html">Quiz</a></li>
</ul>
</nav>
</header>

<form id="quizForm">

<!-- Fill in the blank -->
<div class="question">
<h3>1. HTML stands for:</h3>
<input type="text" id="q1">
</div>

<!-- Multiple Choice -->
<div class="question">
<h3>2. Which language styles webpages?</h3>
<label><input type="radio" name="q2" value="A"> HTML</label><br>
<label><input type="radio" name="q2" value="B"> CSS</label><br>
<label><input type="radio" name="q2" value="C"> Python</label>
</div>

<div class="question">
<h3>3. JavaScript is mainly used for:</h3>
<label><input type="radio" name="q3" value="A"> Structure</label><br>
<label><input type="radio" name="q3" value="B"> Interactivity</label><br>
<label><input type="radio" name="q3" value="C"> Database</label>
</div>

<div class="question">
<h3>4. Which tag creates hyperlinks?</h3>
<label><input type="radio" name="q4" value="A"> &lt;a&gt;</label><br>
<label><input type="radio" name="q4" value="B"> &lt;p&gt;</label><br>
<label><input type="radio" name="q4" value="C"> &lt;img&gt;</label>
</div>

<!-- Multi-selection -->
<div class="question">
<h3>5. Select ALL frontend technologies:</h3>
<label><input type="checkbox" value="HTML"> HTML</label><br>
<label><input type="checkbox" value="CSS"> CSS</label><br>
<label><input type="checkbox" value="Python"> Python</label><br>
<label><input type="checkbox" value="JavaScript"> JavaScript</label>
</div>

<button type="button" onclick="gradeQuiz()">Submit Quiz</button>
<button type="button" onclick="resetQuiz()">Reset Quiz</button>

</form>

<div id="results"></div>

<script src="js/quiz.js"></script>

</body>
</html>