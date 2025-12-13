const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const Width=document.getElementById("overcnv").clientWidth;
const Height=document.getElementById("overcnv").clientHeight;
document.getElementById("canvas").width=Width;
document.getElementById("canvas").height=Height;

mission=""
grabbing=false;
const unit_horizontal=Width/8;
const unit_vertical=Height/8;
ctx.clearRect(0, 0, Width, Height);

    // Objet dessiné:
function Bloc(X,Y) {
  ctx.strokeStyle = "black";
  ctx.lineWidth=3;
  ctx.fillStyle = "lightblue";
  ctx.beginPath();
  ctx.roundRect(X-unit_horizontal/2,Y-unit_horizontal/2,unit_horizontal,unit_horizontal,10);
  ctx.stroke();ctx.fill();
}
function circle(X,Y,) {
  ctx.strokeStyle = "black";
  ctx.lineWidth=3;
  ctx.fillStyle = "lightgreen";
  ctx.beginPath();
  ctx.arc(X,Y,unit_horizontal/2,0,2*Math.PI);
  ctx.stroke();ctx.fill();
}


templates_missions=[["reco",unit_horizontal,unit_vertical],["surv",3*unit_horizontal,unit_vertical]]
console.log(templates_missions)
Bloc(templates_missions[0][1],templates_missions[0][2]);
circle(templates_missions[1][1],templates_missions[1][2]);


function MouseClickDown(e){
  // Coordonnées du click, qui va ensuite lancer le déplacement
  Xclick=e.pageX-canvas.offsetLeft;Yclick=e.pageY-canvas.offsetTop;
  // On ne lance le déplacement onmousemove que si
  // le click est dans l'objet
  for (let i=0; i<templates_missions.length; i++){
    if (Math.abs(Xclick-templates_missions[i][1])<unit_horizontal/2 && Math.abs(Yclick - templates_missions[i][2])<unit_horizontal/2) {
      document.getElementById("canvas").style.cursor="grabbing";
      grabbing=true;
      mission=templates_missions[i][0];
    }}
  for (let i = 0; i < missoverlay.length; i++) {
    if (Math.abs(Xclick-missoverlay[i][1])<unit_horizontal/2 && Math.abs(Yclick - missoverlay[i][2 ])<unit_horizontal/2) {
      document.getElementById("canvas").style.cursor="grabbing";
      grabbing=true;
      mission=missoverlay[i][0];
      missoverlay.splice(i,1,);
    }
}}
missoverlay=[]
function MouseClickUp(e){
  ctx.clearRect(0, 0, Width, Height);
  if(grabbing===true){
    XB=e.pageX-canvas.offsetLeft;
    YB=e.pageY-canvas.offsetTop;
    console.log(XB,YB)
    missoverlay.push([mission,XB,YB]);
  }
  for (let i = 0; i < missoverlay.length; i++) {
    console.log(missoverlay[i])

    if(missoverlay[i][0]==='reco'){
      Bloc(missoverlay[i][1],missoverlay[i][2]);
    }
    else if (missoverlay[i][0]==='surv'){
      circle(missoverlay[i][1],missoverlay[i][2]);
    }
  };
  grabbing=false;
  Bloc(templates_missions[0][1],templates_missions[0][2]);
  circle(templates_missions[1][1],templates_missions[1][2]);
  console.log(missoverlay);
}
	 
canvas.onmousedown = MouseClickDown;
canvas.onmouseup = MouseClickUp;