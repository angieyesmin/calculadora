let expression = '';

function appendToDisplay(value) {
    if (expression === '0') {
        expression = value;
    } else {
        expression += value;
    }
    document.getElementById('expression').innerText = expression;
}

function clearDisplay() {
    expression = '';
    document.getElementById('expression').innerText = '';
    document.getElementById('display').innerText = '0';
}

function calculateResult() {
    try {
        let result = eval(expression);
        document.getElementById('display').innerText = result;
    } catch (error) {
        document.getElementById('display').innerText = 'Error';
    }
}
