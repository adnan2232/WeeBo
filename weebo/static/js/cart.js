var updateBtns = document.getElementsByClassName('update-cart');

for(var i=0;i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log("productId: ",productId," action: ",action);
        if(user==="AnonymousUser"){
            console.log("User is not authenticate");
        }
        else{
            UpdateUserOrder(productId,action);
        }
    });
}





function UpdateUserOrder(productId,action){
    fetch('/update_item',{
        method: 'POST',
        headers:{
            'CONTENT-TYPE':'application/json',
            'X-CSRFToken' :csrftoken,
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    }).then((response) =>{
        return response.json()
    }).then((data)=> {console.log('data: ',data)})
}