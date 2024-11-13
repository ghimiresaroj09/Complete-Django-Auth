var x = document.getElementById("form-login");
var y = document.getElementById("form-signup");
var z = document.getElementById("btn");
var xx = document.getElementById("span-login");
var yy = document.getElementById("span-signup");
var zz = document.getElementById("formbox");

function signup() {
    x.style.left = "-400px";
    y.style.left = "50px";
    z.style.left = "150px";
    xx.style.color = "#E7272C";
    yy.style.color = "#F7F7FF";
    zz.style.height = "600px";
    z.style.background="linear-gradient(to right, #E7272C, #000000)";

}
function login() {
    x.style.left = "50px";
    y.style.left = "450px";
    z.style.left = "0px";
    xx.style.color = "#F7F7FF";
    yy.style.color = "#E7272C";
    zz.style.height = "400px";
    z.style.background="linear-gradient(to left, #E7272C, #000000)";
}

