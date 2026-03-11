let a = 'hello';
a='hello2';
const b=0.8;
console.log(b);
console.log(a);

let hairetu=[1,2,3,'uo'];
console.log(hairetu);
console.log(hairetu[3]);

c=0;
while(c<hairetu.length/*4*/){
    console.log(hairetu[c]);
    c++;

}
console.log(c);
d=0;

if(c==5){
    d=9;
}
else console.log('else');
console.log(d);

const test=(x)=>{
    if(x==5){
        d=9;
    }
    else console.log('else');
    console.log(d);
    
};
test(5);

const uo2={
    prize:2,
    name:'koke',
    test:(arg)=>{
        console.log('hello3',arg);
    }
    
};
user=uo2;
console.log(user.prize);
console.log(user.name);
console.log(user.test(5));

console.log(window.innerWidth);
window.alert('hello2222');


console.log(document.getElementsByTagName('h1')[0]);
console.log(document);
document.getElementsByTagName('h1')[0].addEventListener('click',()=>{
    window.alert('kontya');
})