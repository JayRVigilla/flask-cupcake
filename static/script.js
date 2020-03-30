$(document).ready( function() {

    async function getAllCupcakes(){
        response = await axios.get('/api/cupcakes');
        return response.data.cupcakes;
    }

    async function ListOfUsefulCupCakeData(){
        cupcakes = await getAllCupcakes();
        flavorList = [];

        // for each JSONcupcake in AllCupcakes
        // append to arr the flavor
        for( let cake in cupcakes){
            flavorList.push(cake.flavor)
        }
        return flavorList
    }

    function addFlavorsToHTML(flavorList){
        // for loop of flavors
            // create <li> with .text of "flavor"
            // add to list
        $flavorFlaves = $("#flavors");
        flavorList.forEach(element => {
            let $flavor = $("<li>")
                        .text(element);
            $flavorFlaves.append($flavor);
        });
    }

    flavorlist = ListOfUsefulCupCakeData();
    addFlavorsToHTML(flavorList);

});