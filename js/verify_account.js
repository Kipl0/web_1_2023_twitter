/**
 * Verificer en brugers konto 
 */
async function verify_account() {
    try {
        // Hent verification nøglen fra url
        url = window.location.href
        url_split = url.split("/")
        verification_key = url_split[url_split.length - 1] // Få det sidste element fra array

        //TODO
        // hent id fra h1, p og spinner
        // gør h1 til succes text
        // gør p tag til login knap 
        // gør spinner til succes ikon

        // Lav reqeust til vores API om at verify email
        const conn = await fetch(`/verify-email/${verification_key}`,{
            method: "POST"
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            verify_header.innerHTML = "Cannot verify your accout!"
            verify_text.innerHTML = "Please, try again later"
            verify_spinner.classList.add("hidden")
            throw new TypeError("Something went wrong");
        }

        
        const verify_header = document.getElementById("verify_header")
        const verify_text = document.getElementById("verify_text")
        const verify_login_btn = document.getElementById("verify_login_btn")
        const verify_spinner = document.getElementById("verify_spinner")
        const verify_succes = document.getElementById("verify_succes")

        verify_header.innerHTML = "Cheers! your account is now verified"
        verify_text.classList.add("hidden")

        verify_login_btn.classList.remove("hidden")
        verify_login_btn.classList.add("flex")

        verify_spinner.classList.add("hidden")

        verify_succes.classList.remove("hidden")
        verify_succes.classList.add("flex")
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

// timer for load, vent på at langsom pc er loaded  //lidt ekstra, så man kan se det for projektets skyld
setTimeout(verify_account, 3000);

