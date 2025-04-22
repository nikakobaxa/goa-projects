const div = document.getElementById("container");

let p = document.createElement("p");
let textnode1 = document.createTextNode('Hello world');
p.appendChild(textnode1)
div.appendChild(p)

let button = document.createElement('button');
let textnode2 = document.createTextNode('click me');
button.appendChild(textnode2);
div.appendChild(button)

let img = document.createElement('img');
img.src =  'https://images.search.yahoo.com/images/view;_ylt=AwrFNufuNfpn2uMpmB.JzbkF;_ylu=c2VjA3NyBHNsawNpbWcEb2lkAzI3OTQyN2Q3MDJkM2Q4YmE4YjI3MTIyMTVkNjY0N2VmBGdwb3MDMgRpdANiaW5n?back=https%3A%2F%2Fimages.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dronaldo%26type%3DE210US91215G0%26fr%3Dmcafee%26fr2%3Dpiv-web%26tab%3Dorganic%26ri%3D2&w=4419&h=2946&imgurl=st1.uvnimg.com%2F4d%2F97%2F870bcb42452ebf7bfa0c609b90bd%2Fcristiano-ronaldo-portugal.jpg&rurl=https%3A%2F%2Fclubedopancreas.pt%2Fcristiano-ronaldo-leva-portugal-ao-euro-2024%2F&size=1569KB&p=ronaldo&oid=279427d702d3d8ba8b2712215d6647ef&fr2=piv-web&fr=mcafee&tt=Cristiano+Ronaldo+leva+Portugal+ao+Euro+2024+-+clubedopancreas.pt&b=0&ni=21&no=2&ts=&tab=organic&sigr=P_JMO.H65vBT&sigb=o6pVPwu78enP&sigi=ms.jRLKbe.Ij&sigt=W4dD2cVQnyKv&.crumb=nO.LS/z5vBH&fr=mcafee&fr2=piv-web&type=E210US91215G0';
img.alt = 'surati'
div.appendChild(img)


div.removeChild(button)

let p1 = document.createElement("p");
let textnode3 = document.createTextNode('Hello world');
p1.appendChild(textnode3)
div.replaceChild(p1, img)


setTimeout(() => {
    console.log(2);
}, 0);
setTimeout(() => {
    console.log(3);
}, 0);
console.log(1);
