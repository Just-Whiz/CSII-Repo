// Post Office JavaScript

function main() {
    // Get the values entered by the user
        var length = document.getElementById("l").value;
        var height = document.getElementById("h").value;
        var thickness = document.getElementById("t").value;
        var zipto = document.getElementById("zipto").value;
        var zipfrom = document.getElementById("zipfrom").value;

        // Send debug alert messages showing the values of each submitted value
        console.log("DEBUG: " + length);
        console.log("DEBUG: " + height);
        console.log("DEBUG: " + thickness);
        console.log("DEBUG: " + zipto);
        console.log("DEBUG: " + zipfrom);

        var postsize = get_size(l, h, t);
        let zonelist = get_zone(zipto, zipfrom);
        var startzone = Math.floor(Number(zonelist[0]));
        var endzone = Math.floor(Number(zonelist[1]));
        var zonestravelled = Math.floor(Number(Math.abs(endzone - startzone)));
        var totalpostcost = Math.floor(Number(post_cost(postsize, zonestravelled)));

        console.log(startzone + " is the value of startzone");
        console.log(endzone + " is the value of endzone");
        console.log(postclass + " is the value of postclass")
        console.log(cost + " is the value of postcost")

        totalpostcost = Math.floor(Number(Math.round(totalpostcost * 100) / 100).toFixed(2));

        document.getElementById('message').innerText  = `${totalpostcost}`;
        console.log(`${totalpostcost} is your postcost.`);

        alert(`${totalpostcost} is your final product`);
};

function get_size(l, h, t) {
    if ((l >= 3.5 && l <= 4.25) && (h >= 3.5 && h <= 6)
         && (t >= 0.007 && t <= 0.016)) {
        postclass = 1 
         }                                                                      
    else if ((l >= 4.25 && l <= 6) && (h >= 6 && h <= 11.5)                                                     
        && (t >= 0.007 && t <= 0.15)) {
            postclass = 2
        }                                                                                         
    else if ((l >= 3.5 && l <= 6.125) && (h >= 5 && h <= 11.5) 
        && (t >= 0.16 && t <= 0.25)) {                                                             
        postclass = 3
        }                                                                                          
    else if ((l >= 6.125 && l <= 24) && (h >= 11 && h <= 18)                                                    
        && (t >= 0.25 && t <= 0.5)) {
        postclass = 4                  
        }                                                                        
    else if ((l >= 24 && h >= 18 && t >= 0.5 && (l + (t + h))) <= 84) {
        postclass = 5
    }                                                                  
    else if  ((l + (h + t)) >= 84 || (l + (h + t)) <= 130) {
        postclass = 6
   } else {                                                                                                      
         postclass = "None"
   };                                                                                      
                                                                    
};

function get_zone(zipfrom, zipto) {
    if ((zipfrom >= 1) && (zipfrom <= 6999)) {
        zone1 = 1
    }
    else if ((zipfrom >= 7000) && (zipfrom <= 19999)) {
        zone1 = 2
    }
    else if ((zipfrom >= 20000) && (zipfrom <= 35999)) {
        zone1 = 3
    }
    else if ((zipfrom >= 36000) && (zipfrom <= 62999)) {
        zone1 = 4
    } 
    else if ((zipfrom >= 63000) && (zipfrom <= 84999)) {
        zone1 = 5
    }                                            
    else if ((zipfrom >= 85000) && (zipfrom <= 99999)) {
        zone1 = 6
    }  
    else 
        zone1 = "Unreachable"                                                                               
    if ((zipto >= 85000) && (zipto <= 99999)) {zone2 = 6} 
    else if ((zipto >= 63000) && (zipto <= 84999)) {zone2 = 5}
    else if ((zipto >= 36000) && (zipto <= 62999)) {zone2 = 4}                                                  
    else if ((zipto >= 20000) && (zipto <= 35999)) {zone2 = 3}                                                        
    else if ((zipto >= 7000) && (zipto <= 19999)) {zone2 = 2}
    else if ((zipto >= 1) && (zipto <= 6999)) {zone2 = 1}
    else {
        zone2 = "Unreachable"
    };                                                                   
    return [zone1, zone2];
};

function post_cost(postclass, zonestravelled) {
    if (postclass == 1) {
        (cost = 0.20 + (0.03 * Number.parseFloat(zonestravelled)))
    }                                    
    else if (postclass == 2) {
        (cost = 0.37 + (0.03 * Number.parseFloat(zonestravelled)))
    }                                   
    else if (postclass == 3) {
        (cost = 0.37 + (0.04 * Number.parseFloat(zonestravelled)))
    }                                      
    else if (postclass == 4) {
        (cost = 0.60 + (0.05 * Number.parseFloat(zonestravelled)))
    }
    else if (postclass == 5) {
        (cost = 2.95 + (0.25 * Number.parseFloat(zonestravelled)))
    }
    else if (postclass == 6) {
        (cost = 3.95 + (0.35 * Number.parseFloat(zonestravelled)))
    }
    else if (postclass == "None") {
        (cost = "None")
    }
    else {
        cost = "None"
    }                                                                                       
    return cost
}