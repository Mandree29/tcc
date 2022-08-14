lista_val = []
lista_val2 = []
var selecao2 = document.querySelector(".rel_class")

document.querySelector('.campo_selecao2').addEventListener('click', ()=>{
    document.querySelector('.lista2').classList.toggle('show2');
    document.querySelector('.seta_baixo2').classList.toggle('rotate1802');
})


let rel1 = document.getElementById('rel1')
rel1.addEventListener('change', ()=>{
    if(rel1.checked){
        lista_val.push(rel1.getAttribute('value'))
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))
    }

    else{
        let x = rel1.getAttribute('value')
        lista_val.forEach((element) => {
            if(element != x){
                lista_val2.push(element)
            }
        });
        lista_val = lista_val2
        lista_val2 = []
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))

    }

})

let rel2 = document.getElementById('rel2')
rel2.addEventListener('change', ()=>{
    if(rel2.checked){
        lista_val.push(rel2.getAttribute('value'))
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))
    }

    else{
        let x = rel2.getAttribute('value')
        lista_val.forEach((element) => {
            if(element != x){
                lista_val2.push(element)
            }
        });
        lista_val = lista_val2
        lista_val2 = []
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))

    }

})

let rel3 = document.getElementById('rel3')
rel3.addEventListener('change', ()=>{
    if(rel3.checked){
        lista_val.push(rel3.getAttribute('value'))
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))
    }

    else{
        let x = rel3.getAttribute('value')
        lista_val.forEach((element) => {
            if(element != x){
                lista_val2.push(element)
            }
        });
        lista_val = lista_val2
        lista_val2 = []
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))

    }

})

let rel4 = document.getElementById('rel4')
rel4.addEventListener('change', ()=>{
    if(rel4.checked){
        lista_val.push(rel4.getAttribute('value'))
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))
    }

    else{
        let x = rel4.getAttribute('value')
        lista_val.forEach((element) => {
            if(element != x){
                lista_val2.push(element)
            }
        });
        lista_val = lista_val2
        lista_val2 = []
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))

    }

})


let rel5 = document.getElementById('rel5')
rel5.addEventListener('change', ()=>{
    if(rel5.checked){
        lista_val.push(rel5.getAttribute('value'))
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))
    }

    else{
        let x = rel5.getAttribute('value')
        lista_val.forEach((element) => {
            if(element != x){
                lista_val2.push(element)
            }
        });
        lista_val = lista_val2
        lista_val2 = []
        selecao2.setAttribute('placeholder', lista_val)
        selecao2.setAttribute('value', lista_val)
        console.log(selecao2.getAttribute('value'))

    }

})