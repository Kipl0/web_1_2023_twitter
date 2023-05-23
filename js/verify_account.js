

async function verify_account() {

    url = window.location.href
    url_split = url.split("/")

    verification_key = url_split[url_split.length - 1] //få det sidste element fra array

    //TODO
    // hent id fra h1, p og spinner
    // gør h1 til succes text
    // gør p tag til login knap 
    // gør spinner til succes ikon

    const conn = await fetch(`/verify-email/${verification_key}`,{
        method: "POST"
    })
    const data = await conn.json()

    if(conn.ok && data.info == "ok") {
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


    } else {
        verify_header.innerHTML = "Cannot verify your accout!"
        verify_text.innerHTML = "Please, try again later"
        verify_spinner.classList.add("hidden")
    }
}

// timer for load, vent på at langsom pc er loaded  //lidt ekstra, så man kan se det for projektets skyld
setTimeout(verify_account, 3000);

