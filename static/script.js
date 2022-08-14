var valores = []
var valores2 = []
var selecao = document.querySelector(".seletor_input")

document.querySelector('.campo_selecao').addEventListener('click',()=>{
   document.querySelector('.lista').classList.toggle('show');
    document.querySelector('.seta_baixo').classList.toggle('rotate180');
})

let vert1 = document.getElementById('vert1')
vert1.addEventListener('change', ()=>{
    if(vert1.checked){
        valores.push(vert1.getAttribute('value'))
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))
    }

    else{
        let x = vert1.getAttribute('value')
        valores.forEach((element) => {
            if(element != x){
                valores2.push(element)
            }
        });
        valores = valores2
        valores2 = []
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))

    }

})

let vert2 = document.getElementById('vert2')
vert2.addEventListener('change', ()=>{
    if(vert2.checked){
        valores.push(vert2.getAttribute('value'))
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))

    }
    else{
        let x = vert2.getAttribute('value')
        valores.forEach((element) => {
            if(element != x){
                valores2.push(element)
            }
        });
        valores = valores2
        valores2 = []
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))
    }
    
})

let vert3 = document.getElementById('vert3')
vert3.addEventListener('change', ()=>{
    if(vert3.checked){
        valores.push(vert3.getAttribute('value'))
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))

    }
    else{
        let x = vert3.getAttribute('value')
        valores.forEach((element) => {
            if(element != x){
                valores2.push(element)
            }
        });
        valores = valores2
        valores2 = []
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))
    }
    
})

let vert4 = document.getElementById('vert4')
vert4.addEventListener('change', ()=>{
    if(vert4.checked){
        valores.push(vert4.getAttribute('value'))
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))
    }
    else{
        let x = vert4.getAttribute('value')
        valores.forEach((element) => {
            if(element != x){
                valores2.push(element)
            }
        });
        valores = valores2
        valores2 = []
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))
    }
    
})

let vert5 = document.getElementById('vert5')
vert5.addEventListener('change', ()=>{
    if(vert5.checked){
        valores.push(vert5.getAttribute('value'))
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))
    }
    else{
        let x = vert5.getAttribute('value')
        valores.forEach((element) => {
            if(element != x){
                valores2.push(element)
            }
        });
        valores = valores2
        valores2 = []
        selecao.setAttribute('placeholder', valores)
        selecao.setAttribute('value', valores)
        console.log(selecao.getAttribute('value'))
    }
    
})



