/**
 * Lav et request til vores api om at ændre brugerens password
 */
async function change_password_confirm() {
    try {
        url = window.location.href
        url_split = url.split("/")
        user_key = url_split[url_split.length - 1] //få det sidste element fra array

        // Hent event target som i vores tilfælde er en form
        const frm = event.target

        // Lav reqeust til vores API om at confirm-new-password
        const conn = await fetch(`/confirm-new-password/${user_key}`, {
            method: "POST",
            body: new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()
        
        // Hvis brugen ikke opfylder vores validation kriterier, hvis en fejlbesked til brugeren
        if (conn.status == 400){
            const infoText = document.getElementById("infoText")
            infoText.innerHTML = data.info
            infoText.classList.add("bg-red-400")
            return
        }

        // Hvis ikke password blev opdateret, hvis en fejlbesked til brugeren
        if( !conn.ok || data.info != "ok" ) {
            const infoText = document.getElementById("infoText")
            infoText.innerHTML = data.info
            infoText.classList.add("bg-red-400")
            throw new TypeError(400, "Something went wrong. Cannot change password");
        }

        // Redirect til login siden
        location.href = `/login`
       
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
        
    }
}