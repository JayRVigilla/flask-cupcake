$(async function() {

  let $form = $("#new-cupcake-form");
  let $flavorFlaves = $("#flavors");
  let flavorList = [];

  $form.on("submit", function(event){
    event.preventDefault();
    SendNewCupcake();
  });

  async function SendNewCupcake(){
    
    let flavor = $("#form-flavor").val();
    let size = $("#form-size").val();
    let rating = $("#form-rating").val();
    let image = $("#form-image").val();
    
    let response = await axios.post('/api/cupcakes', data={
      flavor,
      size,
      rating,
      image
    });

    flavorList.push(flavor);
    addFlavorsToHTML(flavorList);

    $( '#new-cupcake-form' ).trigger("reset");
  };
  

  async function getAllCupcakes(){
      response = await axios.get('/api/cupcakes');
      return response.data.cupcakes;
  }

  async function ListOfUsefulCupCakeData(){
      cupcakes = await getAllCupcakes();


      // for each JSONcupcake in AllCupcakes
      // append to arr the flavor
      for( let cake of cupcakes){
          flavorList.push(cake.flavor)
      }
      return flavorList
  }

  function addFlavorsToHTML(flavorList){
      // for loop of flavors
          // create <li> with .text of "flavor"
          // add to list
      $flavorFlaves.empty();
      for ( let flav of flavorList){
          let $flavor = $("<li>")
                      .text(flav);
          $flavorFlaves.append($flavor);
      };
  }

  flavorList = await ListOfUsefulCupCakeData();
  addFlavorsToHTML(flavorList);

});