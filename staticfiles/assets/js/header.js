const fixed = document.querySelector(".header-fixed");
const up = document.querySelector(".header-up");
const down = document.querySelector(".header-down");
const html = document.querySelector("html");
document.addEventListener('scroll', function(e) {
    if(html.scrollTop >= up.scrollHeight) down.setAttribute("style","position:fixed; left:0;right:0;top:0;");
    else down.removeAttribute("style");
});

document.addEventListener('scroll', function(e) {
    if(html.scrollTop >= up.scrollHeight) fixed.setAttribute("style","height:75px;");
    else fixed.removeAttribute("style");
});