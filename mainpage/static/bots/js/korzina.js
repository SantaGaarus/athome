const aaa=JSON.parse(localStorage.getItem('a'));
const ab=JSON.parse(localStorage.getItem('ab'));
const abc=JSON.parse(localStorage.getItem('abc'));
var sum=0;

function generateList(arg,arg1,arg2){
    let items="";
    for (let i=0; i<arg.length;i++){
        console.log(arg1[i])
        items+=`<li>${arg[i]} </br> ${arg1[i]}</br> <img class="mebel_img" src=${window.location.href.replace('korzina','media/'+arg2[i])}></li>`;
        sum+=Number(arg1[i]);
        
        document.querySelector("ula").innerHTML=`${sum}`
    }
    return items;
    
}





function Freak(){
    localStorage.clear()

  }  
document.querySelector("main").innerHTML=`
<ul>
${generateList(aaa,ab,abc)}
</ul>
`;


