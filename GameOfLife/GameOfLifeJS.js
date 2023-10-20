function removeAllChildNodes(parent){
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

function getInput() {
    let promptInput = prompt('Enter a whole number between 1 and 100', '');
    return promptInput;
}

function createArray(promptInput){
    const square = [];

    for(i = 0; i < promptInput; i++) {
        square[i] += `${i}`;
    }
    return square;
}

let uniqueClass = 0;
function createUniqueClass(){
    
    uniqueClass += 1;
    return uniqueClass;
    
}

function addOpacity(element) {
    let numElement = +(element.style.opacity);
    if (numElement === 1){
        return numElement;
    }
    numElement += 0.10;
    return numElement;
}

function addColor(div){
    div.addEventListener('mouseover', (event) => {
        const element = document.getElementsByClassName(event.target.classList);
        console.log(event.target);
        element[0].style.background = `#${(Math.floor(Math.random()*16777215).toString(16))}`
        element[0].style.opacity = `${addOpacity(element[0])}`;
    });
}

const container = document.querySelector('#container');
container.setAttribute('style', 'display: flex; flex: 1 1 0; height: 960px; width: 960px; margin: auto; border: solid black 1px; flex-wrap: wrap;');

function createGrid(grid){

    grid.forEach(() => {
        const div = document.createElement('div');
        div.setAttribute('style', 'box-sizing: border-box; border: 1px solid black;');
        div.classList.add(`box${createUniqueClass()}`);
        container.appendChild(div);
        div.style.height = `${960 / promptInput + 0.01}px`; 
        div.style.width = `${960 / promptInput}px`;    
        addColor(div);
    });
}

let promptInput = '';
let array = [''];
const button = document.querySelector('button');
    
button.addEventListener('click', () => {
    removeAllChildNodes(container);
    promptInput = getInput();
    grid = createArray(promptInput * promptInput);
    createGrid(grid);
    })