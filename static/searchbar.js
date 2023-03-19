var barra = document.getElementById('nomes')
var nomes


barra.addEventListener('focus', foco_ajax)
barra.addEventListener('keyup', search_bar)




function foco_ajax(){
    //  console.log('foco_event')
    //  let xhr = new XMLHttpRequest()
    //  xhr.open('GET', 'http://127.0.0.1/pesquisa/nomes', true)
    //  xhr.setRequestHeader
    // xhr.onload = function(){
    //  if(this.status == 200){
    //         console.log('sucesso')
    //     }
    //  }
    //  xhr.send()

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
                console.log(element.nome)
            });
        })
    })

}



function search_bar(){
    console.log('ok')
}