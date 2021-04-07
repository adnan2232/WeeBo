var views = document.getElementsByClassName('view');

for (let i=0;i<views.length;i++){
    views[i].addEventListener("click",function(){
        let pop = document.getElementsByClassName("pops");
        pop[i].classList.remove('hidden');
    });
}

var closebtn = document.getElementsByClassName('closebtn');

for(let i=0;i<views.length;i++)
{
    closebtn[i].addEventListener("click",function(){
        let pop = document.getElementsByClassName("pops");
        pop[i].classList.add("hidden");
    })
}