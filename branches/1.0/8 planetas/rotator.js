/**
* Rotator.js by will jessup
* will -at- willjessup.com or AIM "xdionysisx"
* This is a demo of jQuery and a bit of fun javaScript - released under creative commons
* IE fixes for previous versions by Krzysztof Finowicki
*/


var de;
var w;
var h;
var xm=0;
var ym=0;
var ay=2;
var sin=Math.sin(ay*Math.PI/180);
var cos=Math.cos(ay*Math.PI/180); 
var angle = 0;
var k=0;
var elem = [];
var camDist = 400;
var scale = .07;
var vpsi = 0;
var fontScale = .0005;
var psi = -.2;


// not using $() here to recude # of query calls since onmousemove gets called so often that it needs optimization
document.onmousemove = function(e) {
	if (window.event) e = window.event;
	xm = (e.x || e.clientX);
      ym = (e.y || e.clientY);

//kff: I'm not sure if it is necessary to repeat these calculations on each mousemove
// maybe in onresize (if you want to optimize)? but I will not change it
	var de = document.documentElement;
      var w = window.innerWidth || self.innerWidth || (de&&de.clientWidth) || document.body.clientWidth;
      var h = window.innerHeight || self.innerHeight || (de&&de.clientHeight) || document.body.clientHeight;


      /**
	*set the amplitude of the function equal to height of the browser, shifted by 180 degrees (half browser height).
	*returns value between 90 and 0 degrees for any mouse movement on the screen
	*/
      //psi=(ym-h*.5)/h*Math.PI;
      //vpsi= Math.sin((ym-h*.5)/h*Math.PI)*90;
	sin=Math.sin((-xm+w*.5)/w*Math.PI);
	cos=Math.cos((-xm+w*.5)/w*Math.PI);

}
$.fn.cartesianToSphereical = function() {

    //with each link element, convert it and store it in elements
    for(i=0; i<this.length; i++) {
                      if ( !elem[i] ) elem[i] = {};


                      x = this[i].getAttribute("posX");
                      y = this[i].getAttribute("posY");
                      z = this[i].getAttribute("posZ");

                      r = parseInt(Math.abs(Math.sqrt(x*x+y*y+z*z)));
                      rr = parseInt(Math.abs(Math.sqrt(x*x+y*y)));

                      //angle from 0 between -pi/pi  , need to add 180 degrees for anything in 2,3 quadrant
                      if(x<0)
                         theta= (Math.atan(y/x)*180/Math.PI)+180;
                      else
                         theta= (Math.atan(y/x)*180/Math.PI);


                      psiElement= (Math.atan(z/rr)*180/Math.PI);

                      //sphereical is r, theta, and psi (psie here because psi is the system, psie is individual)
                      elem[i].theta = theta;           //rotational angle
                      elem[i].r = r;                   //total radius
                      elem[i].psie = psiElement;        //vertical angle

                      //lets do this Z calculation here so its not repeated below
                      elem[i].z = z;

                      //radius of x-y sphere, used to calculate distance later
                      elem[i].rr = rr;
                      elem[i].html = this[i].innerHTML;


    }
}
$.fn.rotate = function () {
        for(i=0; i<this.length; i++) {
                      if (!elem[i]) elem[i] = {};

                      //angle of the system
                      angle += sin*scale;

                      //uncomment below line to rotate 1/r^2
                      // elem[i].angle = (angle + elem[i].theta)*(400/(elem[i].r^2));
                      elem[i].angle = (angle + elem[i].theta);

                      //psi from -.99 to .99
                      X = elem[i].r*Math.cos(elem[i].angle*Math.PI/180)*Math.cos(elem[i].psie*Math.PI/180);
                      Y = elem[i].r*Math.sin(elem[i].angle*Math.PI/180)*Math.cos(elem[i].psie*Math.PI/180)*Math.sin(psi) + elem[i].z*Math.cos(psi);


                      elem[i].dist = parseInt( elem[i].r*Math.cos((vpsi + elem[i].psie)*Math.PI/180) +
                          elem[i].rr*Math.sin(elem[i].angle*Math.PI/180)*Math.cos(vpsi*Math.PI/180) + camDist);


                      size = (elem[i].dist - 00)/700;


                          this[i].style.top = -Y + "px";
                          this[i].style.left = X + "px";
                          this[i].style.fontSize = size + "em";
                          this[i].style.opacity  = (size*10)/5;
                          this[i].style.zIndex  = elem[i].dist;


	}
}



var items,links;
var rotate = false;

function run(){
        items.rotate();
        if(rotate) setTimeout("run()", 16);
}




