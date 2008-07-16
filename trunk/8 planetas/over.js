$(document).ready(function(){
   $("#rotation_control").click( function() {
     (rotate) ? rotate = false : rotate = true;
    (rotate) ? $(this).children().src("stop.png") :  $(this).children().src("rotate.png");
     run();
   });
   items = $("#links .name");
   items.cartesianToSphereical();
   rotate = true;
   run();
   de = document.documentElement;
   w = window.innerWidth || self.innerWidth || (de && de.clientWidth) || document.body.clientWidth;
   h = window.innerHeight || self.innerHeight || (de && de.clientHeight) || document.body.clientHeight;
   items.hover(function(){ 
     $(this).addClass("over");

   },function(){
     $(this).removeClass("over");

   });
});