// send user email to deactivate own profile
async function deactivate_own_profile() {
    try {
        url = window.location.href
        url_split = url.split("/")
        deactivate_key = url_split[url_split.length - 1] //få det sidste element fra array

        const frm = event.target.form

        const conn = await fetch(`/self-deactivate-profile/${deactivate_key}`, {
            method: "POST",
            body: new FormData(frm)
        })
        const data = await conn.json()

        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }

        const infoText = document.getElementById("infoText")
        infoText.innerHTML = "A confirmation mail has been sent"
        infoText.classList.remove("hidden")
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}


async function confirm_deactivate_account() {
    url = window.location.href
    url_split = url.split("/")

    deactivate_key = url_split[url_split.length - 1] //få det sidste element fra array

    const frm = event.target.form
    const conn = await fetch(`/confirm-self-deactivate-profile/${deactivate_key}`, {
        method: "POST",
        body: new FormData(frm)
    })
    const data = await conn.json()
    console.log(data)

    if(conn.ok && data.info == "ok") {
        console.log("ok")
        // redirect to login
    } else {
        console.log("data ikke ok")
    }
}