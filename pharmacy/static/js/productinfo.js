/**for quantity increment decrement**/

document.addEventListener("DOMContentLoaded", function(event){
    const minusBtn = document.getElementById("minusBtn");
    const plusBtn = document.getElementById("plusBtn");
    const qty = document.getElementById("qty");
    const pid = document.getElementById("pid");
    const btnCart = document.getElementById("btnCart");
    const tkn=document.querySelector('[name="csrfmiddlewaretoken"]').value;

    plusBtn.addEventListener("click", function(){
        // alert("hello");
        let q=parseInt(qty.value,10);
        q=isNaN(q)?0:q;
        if(q<10){
            q++;
            qty.value=q;
            
        }
    });

    minusBtn.addEventListener("click", function(){
        // alert("hello");
        let q=parseInt(qty.value,10);
        q=isNaN(q)?0:q;
        if(q>1){
            q--;
            qty.value=q;
            
        }
    });

    btnCart.addEventListener("click", function(){
        
        let q=parseInt(qty.value,10);
        q=isNaN(q)?0:q;
        if(q>0){
            
            let postObj = {
                product_qty: q,
                pid: pid.value,
                token: tkn
            }
            console.log(postObj);

        }else{
            alert("enter qty");
        }
    });

});
       