/**
 * Send user email to deactivate own profile
 */
async function deactivate_own_profile() {
    try {
        // Get the deactivation key from the url 
        url = window.location.href
        url_split = url.split("/")
        deactivate_key = url_split[url_split.length - 1] // Få det sidste element fra array

        // Hent event target som i vores tilfælde er en form
        const frm = event.target.form

        // Lav reqeust til vores API om at deactivate profile
        const conn = await fetch(`/self-deactivate-profile/${deactivate_key}`, {
            method: "POST",
            body: new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
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

/**
 * Deactivate own profile
 */
async function confirm_deactivate_account() {
    try {
        // Get the deactivation key from the url 
        url = window.location.href
        url_split = url.split("/")
        deactivate_key = url_split[url_split.length - 1] // Få det sidste element fra array

        // Hent event target som i vores tilfælde er en form
        const frm = event.target.form

        // Lav reqeust til vores API om at deactivate profile
        const conn = await fetch(`/confirm-self-deactivate-profile/${deactivate_key}`, {
            method: "POST",
            body: new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }
        location.href = `/`
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}