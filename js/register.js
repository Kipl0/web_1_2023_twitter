async function register(){
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target
       
        // Lav reqeust til vores API om at write tweet comment for det valgte tweet
        const conn = await fetch("/register", {
            method : "POST",
            body : new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()
        if (conn.status == 400){
            const infoText = document.getElementById("infoText")
            infoText.innerHTML = data.info
            infoText.classList.remove("hidden")
            return
        }

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        else if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }
        const infoText = document.getElementById("infoText")
        infoText.innerHTML = "A verification mail has been set to you!"
        infoText.classList.remove("hidden")
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}
