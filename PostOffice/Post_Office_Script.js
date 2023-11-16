// # Program Name: GCDS Rust Removal AKA the GCDS Post Office
// Student Name: Chris Suy
// Course: CS II
// Instructor: Mr. Campbell
// Date: 10/6/23
// I pledge my honor

function main() {
    /*

    This function runs the functions that calculate and determine the price
    of postage.

    l - the length of the postage
    h - the height of the postage
    t - the thickness of the postage
    zipto - the starting 
    zipfrom - 

    */

        // Get the values entered by the user
        var l = document.getElementById("l").value;
        var h = document.getElementById("h").value;
        var t = document.getElementById("t").value;
        var zipto = document.getElementById("zipto").value;
        var zipfrom = document.getElementById("zipfrom").value;

        // Turn each inputted value into a number instead of a string
        l = parseFloat(l);
        h = parseFloat(h);
        t = parseFloat(t);
        zipto = parseFloat(zipto);
        zipfrom = parseFloat(zipfrom);

        // Sets variables to a returned function value
        var size = get_size(l, h, t);                                       // Sets size to the returned value of get_size
        var zone_list = get_zone(zipto, zipfrom);                           // Sets zones to the returned value of get_zone
        var start_zones = Math.floor(zone_list[0]);                         // Sets startzone as a variable from the tuple returned from the function
        var end_zones = Math.floor(zone_list[1]);                           
        var travelled_zones = Math.abs(end_zones - start_zones);            
        var total = post_cost(size, travelled_zones);                       
                                                                                
        // Convert a_number to a string
 
        // A regular expression that removes the leading numbers/zeroes in the decimals after a "restraining" number of places
        const toFixedWithoutZeros = (num, precision) =>
        num.toFixed(precision).replace(/\.0+$/, '');                                      // In this case, this expression removes all numbers after the 2nd decimal place                
             
        
        if (total.substring(0,1) == "0")
            toFixedWithoutZeros(total, 2);                                       
            const message = document.getElementById("message");         // Sets message as a variable and looks for its title ID in the HTML
            message.innerHTML = total;                                  // Sets the HTML to the value of total (after being )

};

function get_size(l, h, t) {
    /*
    l - variable for length
    h - variable for the height
    t - variable for the thickness

    This function is a simple algorithm that determines 

    */
    if ((l >= 3.5 && l <= 4.25) && (h >= 3.5 && h <= 6)
         && (t >= 0.007 && t <= 0.016)) {
            postclass = 1;
         }                                                                      
    else if ((l >= 4.25 && l <= 6) && (h >= 6 && h <= 11.5)                                                     
        && (t >= 0.007 && t <= 0.15)) {
            postclass = 2;
        }                                                                                         
    else if ((l >= 3.5 && l <= 6.125) && (h >= 5 && h <= 11.5) 
        && (t >= 0.16 && t <= 0.25)) {                                                             
            postclass = 3;
        }                                                                                          
    else if ((l >= 6.125 && l <= 24) && (h >= 11 && h <= 18)                                                    
        && (t >= 0.25 && t <= 0.5)) {
            postclass = 4;               
        }                                                                        
    else if ((l >= 24 && h >= 18 && t >= 0.5 && (l + (t + h))) <= 84) {
            postclass = 5
    }                                                                  
    else if  ((l + (h + t)) >= 84 || (l + (h + t)) <= 130) {
            postclass = 6;
   } else {                                                                                                      
            postclass = "Unmailable";
   };                                                                                      
   return postclass                                                    
}

function get_zone(zipfrom, zipto) {
    /*
    */
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
        zone1 = "Unmailable"                                                                               
    if ((zipto >= 85000) && (zipto <= 99999)) {zone2 = 6} 
    else if ((zipto >= 63000) && (zipto <= 84999)) {zone2 = 5}
    else if ((zipto >= 36000) && (zipto <= 62999)) {zone2 = 4}                                                  
    else if ((zipto >= 20000) && (zipto <= 35999)) {zone2 = 3}                                                        
    else if ((zipto >= 7000) && (zipto <= 19999)) {zone2 = 2}
    else if ((zipto >= 1) && (zipto <= 6999)) {zone2 = 1}
    else {
        zone2 = "Unmailable"
    };                                                                   
    return [zone1, zone2];
};

function post_cost(postclass, zonestravelled) {
    /*
    */
    if (postclass == 1) {
        cost = ((zonestravelled) * 0.03) + 0.20;
    }                                    
    else if (postclass == 2) {
        cost = (((zonestravelled) * 0.03) + 0.37) 
    }                                   
    else if (postclass == 3) {
        cost = (((zonestravelled) * 0.04) + 0.37)
    }                                      
    else if (postclass == 4) {
        cost = (((zonestravelled) * 0.05) + 0.60)
    }
    else if (postclass == 5) {
        cost = ((zonestravelled * 0.25) + 2.95)
    }
    else if (postclass == 6) {
        cost = (((zonestravelled) * 0.35) + 3.95)
    }
    else {
        cost = "Unmailable";
    }                                                                                       
    return cost
};