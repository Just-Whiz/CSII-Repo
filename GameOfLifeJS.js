// :When the size is submitted by the user, call the loadGrid() function to generate the grid
// based on those parameters

function makeGrid() {
    let tbl = document.getElementById("gridCanvas")

    for(let i= 0; i < 11; i++) {
        let myRow = document.createElement("tr")
        myRow.id = "row" + i;

        tbl.appendChild(myRow);
        let rowW = document.getElementById("row" + i);

        for(let j= 0; j < 11; j++) {
            let myCell = document.getElementById("td");

            rowW.appendChild(myCell)
        }
    }
}

