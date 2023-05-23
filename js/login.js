
// ##############################
function showTip(message){
    const tip_id = Math.random()
    let tip = `
    <div data-tip-id="${tip_id}" class="flex justify-center w-fit px-8 lg:w-1/3 mx-auto py-4 text-white bg-purple-500 rounded-md">
      Invalid credentials. Try again
    </div>
    `
    document.querySelector("#tips").insertAdjacentHTML("afterbegin", tip)
    setTimeout(function(){
        document.querySelector(`[data-tip-id='${tip_id}']`).remove()
    }, 3000)
}

// ##############################
async function login(){
    const btn = event.target
    btn.disabled = true
    btn.innerText = btn.getAttribute("data-await")
    const frm = event.target.form
    const conn = await fetch("/login", {
        method : "POST",
        body : new FormData(frm)
    })
    btn.disabled = false
    btn.innerText = btn.getAttribute("data-default")
    if( !conn.ok ){
        console.log("Cannot login")
        showTip()        
        return
    }
    // Success
    location.href = `/`

    // const data = await conn.json() //bruges til at få fat i username - for at kunne logge ind på profile   -->   /username
    // location.href = `/${data.login_username}`  --> hænger sammen med linje 34
}
