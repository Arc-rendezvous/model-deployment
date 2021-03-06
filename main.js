var feature1_ ,feature2_, feature3_, feature4_, feature5_, prediction;

$(document).ready(function(){
  // fetch all DOM elements for the input
  feature1_ = document.getElementById("feature1");
  feature2_ = document.getElementById("feature2");
  feature3_ = document.getElementById("feature3");
  feature4_ = document.getElementById("feature4");
  feature5_ = document.getElementById("feature5");
})

$(document).on('click','#submit',function(){
    // on clicking submit fetch values from DOM elements and use them to make request to our flask API
    var feature1 = feature1_.value;
    var feature2 = feature2_.value;
    var feature3 = feature3_.value;
    var feature4 = feature4_.options[feature4_.selectedIndex].value;
    var feature5 = feature5_.options[feature5_.selectedIndex].value;

    if(feature1 == "" || feature2 == "" || feature3 == "" || feature4 == "" || feature5 == ""){
      alert("empty fields not allowed");
    }
    else{
      var requestURL = "https://gunawangaol.pythonanywhere.com/prediction?feature1="+feature1+"&feature2="+feature2+"&feature3="+feature3+"&feature4="+feature4+"&feature5="+feature5;
      
      d3.json(requestURL, function(data) {
        console.log(data); // log the data for troubleshooting
        if (data['pred'] == 1) {
            prediction = "approved"
            $("#result").html("Your application is: " + "<span style='color:green;'>"+prediction+"</span>");
        } else {
            prediction = "rejected"
            $("#result").html("Your application is: " + "<span style='color:red;'>"+prediction+"</span>");
        }
      });
    }
  });