var i=0;
function read(){
    if(!i){
        document.getElementById("more").style.display = "inline";
        document.getElementById("dots").style.display = "none";
        document.getElementById("read").style.innerHTML="Read less"
        i=1;
    }
    else{
        document.getElementById("more").style.display = "none";
        document.getElementById("dots").style.display = "inline";
        document.getElementById("read").style.innerHTML="Read more"
        i=0;
    }
}
