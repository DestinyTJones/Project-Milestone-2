// Grade quiz function
function gradeQuiz(){

let score = 0;
let total = 5;
let results = "";

/* Question 1 */
let q1 = document.getElementById("q1").value.toLowerCase();

if(q1 === "hypertext markup language"){
score++;
results += "<p class='correct'>Q1 Correct</p>";
}else{
results += "<p class='wrong'>Q1 Incorrect — HyperText Markup Language</p>";
}

/* Question 2 */
let q2 = document.querySelector('input[name="q2"]:checked');

if(q2 && q2.value==="B"){
score++;
results += "<p class='correct'>Q2 Correct</p>";
}else{
results += "<p class='wrong'>Q2 Incorrect — CSS</p>";
}

/* Question 3 */
let q3 = document.querySelector('input[name="q3"]:checked');

if(q3 && q3.value==="B"){
score++;
results += "<p class='correct'>Q3 Correct</p>";
}else{
results += "<p class='wrong'>Q3 Incorrect — Interactivity</p>";
}

/* Question 4 */
let q4 = document.querySelector('input[name="q4"]:checked');

if(q4 && q4.value==="A"){
score++;
results += "<p class='correct'>Q4 Correct</p>";
}else{
results += "<p class='wrong'>Q4 Incorrect — <a></p>";
}

/* Question 5 Multi-select */
let checked = document.querySelectorAll('input[type="checkbox"]:checked');
let answers = [];

checked.forEach(c=>answers.push(c.value));

let correctAnswers=["HTML","CSS","JavaScript"];

if(JSON.stringify(answers.sort())===JSON.stringify(correctAnswers.sort())){
score++;
results += "<p class='correct'>Q5 Correct</p>";
}else{
results += "<p class='wrong'>Q5 Incorrect — HTML, CSS, JavaScript</p>";
}

/* Pass / Fail */
let passFail = score>=3 ? "PASS ✅" : "FAIL ❌";

document.getElementById("results").innerHTML=
`<h2>${passFail}</h2>
<h3>Total Score: ${score}/${total}</h3>
${results}`;
}

/* Reset Quiz */
function resetQuiz(){
document.getElementById("quizForm").reset();
document.getElementById("results").innerHTML="";
}