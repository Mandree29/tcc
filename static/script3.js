var p = document.getElementById('prop')
console.log(p.getAttribute('value'))

var v = document.getElementById('val')
console.log(v)

var m = document.querySelector('.msg')
console.log(m)
v.addEventListener('focus', ()=>{
    if(p.getAttribute('value') == null){
        m.style.display = "block"
    }
})

v.addEventListener('blur', ()=>{
    m.style.display = "none"
})

