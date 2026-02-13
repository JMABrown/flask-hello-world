//document.write("Hello World from javascript ")

document.getElementById("output").innerHTML = "Hello World from javascript";

document.getElementById("bye_button").onclick = function () {
    alert('Goodbye!'); //<- what does this do
    document.getElementById("output").innerHTML = "Goodbye!";
};