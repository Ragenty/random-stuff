let screen = document.getElementById("screen");
let expression = "";

function appendToScreen(value) {
	expression += value;
  screen.textContent = expression
}

function clearScreen() {
	expession = "";
  screen.textContent = "0";
}

function calculate() {
	try {
  	let result = eval(expression);
    screen.textContent = result
    expression = "";
  } catch (error) {
  	screen.textContent = "Error";
    expression = "";
  }
}
