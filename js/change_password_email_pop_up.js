

/**
 * Åbn & Luk popup 
 */
function open_change_password_pop_up() {
    // Hent popup elemented
    const change_password_pop_up = document.getElementById("change_password_pop_up")
    
    // Toggle popup elemenets synlighed til det modsatte af hvad det er 
    if(change_password_pop_up.classList.contains("hidden")) {
        change_password_pop_up.classList.remove("hidden")
        change_password_pop_up.classList.add("flex")  
    } else {
        change_password_pop_up.classList.add("hidden")
        change_password_pop_up.classList.remove("flex")
    }
}

/**
 * Luk popup ved klik uden for form element
 * @param {MouseEvent} event - On click mouse event.
 */ 
function close_change_password_pop_up(event) {
    const change_password_form = document.getElementById("change_password_form")
    const target = event.target

  // Check if the target is outside the form
  if (!change_password_form.contains(target)) {
    const change_password_pop_up = document.getElementById("change_password_pop_up")
    change_password_pop_up.classList.add("hidden")
    change_password_pop_up.classList.remove("flex")
  }
}


/**
 * Sender en mail til brugeren med et link de kan bruge til at ændre deres password
 */ 
async function change_password_submit(){
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target
        // Lav reqeust til vores API om at change-password-send-email
        const conn = await fetch("/change-password-send-email", {
            method: "POST",
            body: new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet var succesfuldt
        if( !conn.ok || data.info != "ok" ) {
            const chanage_password_error_message = document.getElementById("chanage_password_error_message")
            chanage_password_error_message.innerHTML = "Cannot send email to change password"
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }

        // Toggle popup
        open_change_password_pop_up()
    }
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
        
    }
}

/**
 * Initialiser event listeners
 */ 
function init(){
    // DOMContentLoaded = a specific event name recognized by browsers to indicate that the initial HTML document has finished loading
    document.addEventListener("DOMContentLoaded", function() {
        // Hent elementer
        const x_change_password_pop_up = document.getElementById("x_change_password_pop_up")
        const change_password_pop_up = document.getElementById("change_password_pop_up")

        // Tilføl event listeners
        x_change_password_pop_up.addEventListener("click", open_change_password_pop_up)
        change_password_pop_up.addEventListener("click", close_change_password_pop_up)
    })

}

// Kald init funktion en gang når js filen bliver importeret
init()
