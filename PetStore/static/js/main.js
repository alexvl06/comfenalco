var products =  document.getElementsByClassName('count')
var quantities =  new Array(products.length).fill(0)

function addProduct(id){
    quantities[Number(id)-1] +=1 
    document.getElementById("input"+id).value = String(quantities[Number(id)-1])
    localStorage.setItem("Cantidades", quantities)

}

function cleanAll(){
    document.getElementById('form').reset()
    localStorage.setItem("Productos", JSON.stringify(products))
}

function clean(name){
    quantities[Number(name)-1] =0
    document.getElementById("input"+name).value = String(quantities[Number(name)-1])
}

function table(){
    var quantities =  localStorage.getItem("Cantidades").split(',')
    quantities = quantities.map(str=>{
        return parseInt(str)
    })
    var count = 0
    var subtotal = new Array(quantities.lenght).fill(0)
    if(quantities.findIndex((element)=>element != 0)>-1){
        for(var i = 0; i< quantities.length; i++){
             if(quantities[i] != 0){
 
                 document.getElementById("Cantidad"+String(i+1)).innerHTML = quantities[i]
                precio = document.getElementById("Price"+String(i+1)).innerHTML
                subtotal[i] = (parseInt(precio)*parseInt(quantities[i]))
                document.getElementById("Subtotal"+String(i+1)).innerHTML=String(subtotal[i])
                
             }
             else{
                subtotal[i] = 0
                document.getElementById("tr"+String(i+1)).style.display = "none"
             }
           }
    
          var total = 0
        for(var j = 0; j<subtotal.length;j++){
             total += subtotal[j]
         }

         var totalArticulos = 0
         for(var j = 0; j<quantities.length;j++){
            totalArticulos += quantities[j]
        }

         console.log("Total: ", total, "Subtotal: ", subtotal)
         var strTotal = ""
        if(total >1000000){
            strTotal = String(parseInt(total)/1000000)+"'"+String(parseInt(total)/1000)+"."+ String(total).slice(-3) 
        }
        else if(total>1000){
            strTotal = String(parseInt(total)/1000)+"."+ String(total).slice(-3)  
         }else{
           strTotal = String(total)+" pesos"  
      }
      document.getElementById("total").innerHTML = String(totalArticulos)+" articulos por $"+strTotal+ " pesos"
         
    }
    else{
        console.log("Cantidades desde local: ", quantities)
        console.log("Cantidades desde window",window.quantities)
        alert("Debe al menos escoger un producto para continuar")
        window.location.href = '/'
    }

 

}

