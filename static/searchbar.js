var barra = document.getElementById('nomes')
var caixa_nomes = document.getElementById('caixa_nomes')
var nomes
var lista_nomes = []
var valor = ''


window.onload = foco_ajax()
barra.addEventListener('keyup', search_bar)



function foco_ajax(){
    fetch(`${window.origin}/pesquisa/nomes`, {
        method:"GET",
        body:JSON.stringify(nomes),
        cache:"no-cache",
        headers:new Headers({
            "content-type":"aplication/json"
        })

    })
    .then(function(response){
        if(response.status != 200){
            console.log(`A resposta não foi 200: ${response.status}`)
            return 

        }
        response.json().then(function(data){
            data.forEach(element => {
                lista_nomes.push(element.nome)
            });
        
        })
    })

}



function search_bar(letras){
    var itens = document.querySelectorAll('ul > li')
    console.log(itens)
    for(elementos of itens){
        caixa_nomes.removeChild(elementos)
    }
    letras = barra.value
    if(letras == ""){
        caixa_nomes.style.display = 'none'
    }
    console.log(letras)  
    for(palavra of lista_nomes){
        palavra = palavra.toLowerCase()
        letras = letras.toLowerCase()

        if(palavra.slice(0,letras.length) == letras){
            if(letras == ""){
                break
            }
            caixa_nomes.style.display = 'block'
            let element = document.createElement('li')
            element.addEventListener('click', valor_pesquisa)
            let texto = document.createTextNode(palavra)
            element.appendChild(texto)
            caixa_nomes.appendChild(element)
        }
    }


 }


 const valor_pesquisa = (e) =>{
    let x = e.target
    console.log(x.firstChild)
    barra.value = x.innerHTML
 }