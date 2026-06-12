let selected=null;
let offsetX=0;
let offsetY=0;
let connectStart=null;

function makeDraggable(el,node){
el.onmousedown=(e)=>{
selected=node;
offsetX=e.clientX-node.x;
offsetY=e.clientY-node.y;
};
}

document.onmousemove=(e)=>{
if(!selected)return;
selected.x=e.clientX-offsetX;
selected.y=e.clientY-offsetY;
render();
};

document.onmouseup=()=>{selected=null;};

function enableConnect(el,node){
el.onclick=(e)=>{
e.stopPropagation();
if(!connectStart){connectStart=node;return;}
edges.push({from:connectStart.id,to:node.id});
connectStart=null;
render();
};
}